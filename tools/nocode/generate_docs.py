from __future__ import annotations

import argparse
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path


ROOT_CATEGORY = {
    "label": "NoCode",
    "position": 2,
}

PT_ROOT_CATEGORY = {
    "label": "NoCode",
    "position": 2,
}


@dataclass
class Slot:
    name: str
    type_name: str
    default: str = ""
    details: str = ""


@dataclass
class NodeDoc:
    class_name: str
    serialized_name: str
    title: str
    menu: str
    source_path: Path
    inputs: list[Slot] = field(default_factory=list)
    outputs: list[Slot] = field(default_factory=list)
    top_flow_input: bool = True
    top_flow_output: bool = True
    notes_en: list[str] = field(default_factory=list)
    notes_pt: list[str] = field(default_factory=list)


@dataclass
class JavaClass:
    name: str
    path: Path
    text: str
    parent: str | None


REGULAR_NODE_RE = re.compile(
    r'getDisplayMenu\(\)\s*\{\s*return\s+"([^"]+)";\s*\}'
    r'.*?getDisplayTitle\(\)\s*\{\s*return\s+"([^"]+)";\s*\}'
    r'.*?displayOnMenu\(\)\s*\{\s*return\s+(true|false);\s*\}',
    re.S,
)
MATERIAL_NODE_RE = re.compile(
    r'MaterialPropertyNodeRegistration\.register\('
    r'([A-Za-z0-9_]+)\.class,\s*SERIALIZED_NAME,\s*"([^"]+)",\s*"([^"]+)"\s*\)'
)
CLASS_RE = re.compile(
    r'public\s+(?:final\s+|abstract\s+)?class\s+([A-Za-z0-9_]+)\s+extends\s+([A-Za-z0-9_\.]+)'
)
SERIALIZED_RE = re.compile(
    r'(?:public|protected|private)?\s*static\s+final\s+String\s+SERIALIZED_NAME\s*=\s*"([^"]+)"'
)
CONST_INDEX_RE = re.compile(r'private\s+static\s+final\s+int\s+([A-Z0-9_]+)\s*=\s*(\d+)\s*;')
RETURN_FALSE_INPUT_RE = re.compile(r'boolean\s+showInputBranch\(\)\s*\{\s*return\s+false;\s*\}', re.S)
RETURN_FALSE_OUTPUT_RE = re.compile(r'boolean\s+showOutputBranch\(\)\s*\{\s*return\s+false;\s*\}', re.S)


def split_args(argument_text: str) -> list[str]:
    args: list[str] = []
    current: list[str] = []
    depth = 0
    in_string = False
    escape = False
    for ch in argument_text:
        if in_string:
            current.append(ch)
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
            current.append(ch)
            continue
        if ch in "([{":
            depth += 1
            current.append(ch)
            continue
        if ch in ")]}":
            depth -= 1
            current.append(ch)
            continue
        if ch == "," and depth == 0:
            part = "".join(current).strip()
            if part:
                args.append(part)
            current = []
            continue
        current.append(ch)
    tail = "".join(current).strip()
    if tail:
        args.append(tail)
    return args


def clean_java_string(value: str) -> str:
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    return value


def extract_class_map(engine_root: Path) -> dict[str, JavaClass]:
    result: dict[str, JavaClass] = {}
    for path in engine_root.rglob("*.java"):
        text = path.read_text(encoding="utf-8")
        match = CLASS_RE.search(text)
        if not match:
            continue
        result[match.group(1)] = JavaClass(
            name=match.group(1),
            path=path,
            text=text,
            parent=match.group(2).split(".")[-1],
        )
    return result


def parse_registered_nodes(classes: dict[str, JavaClass]) -> list[NodeDoc]:
    nodes: list[NodeDoc] = []
    for cls in classes.values():
        normalized_path = cls.path.as_posix()
        if "/Engine/NoCode/" not in normalized_path:
            continue
        serialized_match = SERIALIZED_RE.search(cls.text)
        serialized_name = serialized_match.group(1) if serialized_match else cls.name.removesuffix("Node")

        match = REGULAR_NODE_RE.search(cls.text)
        if match:
            nodes.append(
                NodeDoc(
                    class_name=cls.name,
                    serialized_name=serialized_name,
                    title=match.group(2),
                    menu=match.group(1),
                    source_path=cls.path,
                )
            )
            continue

        material_match = MATERIAL_NODE_RE.search(cls.text)
        if material_match:
            nodes.append(
                NodeDoc(
                    class_name=cls.name,
                    serialized_name=serialized_name,
                    title=material_match.group(2),
                    menu=f"Actions/Material/{material_match.group(3)}",
                    source_path=cls.path,
                )
            )
    nodes.sort(key=lambda item: (item.menu.lower(), item.title.lower(), item.serialized_name.lower()))
    return nodes


def extract_named_slots(text: str, slot_name: str) -> list[Slot] | None:
    patterns = [
        re.compile(rf'\b{slot_name}\s*=\s*new\s+NoCodeSlot\[\]\s*\{{(.*?)\}}\s*;', re.S),
        re.compile(rf'this\.{slot_name}\s*=\s*new\s+NoCodeSlot\[\]\s*\{{(.*?)\}}\s*;', re.S),
    ]
    for pattern in patterns:
        match = pattern.search(text)
        if not match:
            continue
        block = match.group(1)
        slots = re.findall(r'new\s+NoCodeSlot\(\s*"([^"]+)"\s*,\s*ValueType\.([A-Z0-9_]+)', block)
        if slots:
            return [Slot(name=name, type_name=type_name) for name, type_name in slots]
    return None


def first_constructor_super_args(java_class: JavaClass) -> list[str]:
    constructor_re = re.compile(
        rf'public\s+{re.escape(java_class.name)}\s*\([^)]*\)\s*\{{(.*?)\}}',
        re.S,
    )
    constructor_match = constructor_re.search(java_class.text)
    if not constructor_match:
        return []
    body = constructor_match.group(1)
    super_match = re.search(r'super\((.*?)\)\s*;', body, re.S)
    if not super_match:
        return []
    return split_args(super_match.group(1))


def extract_index_constants(text: str) -> dict[str, int]:
    return {name: int(index) for name, index in CONST_INDEX_RE.findall(text)}


def extract_defaults(java_class: JavaClass) -> dict[int, str]:
    defaults: dict[int, str] = {}
    method_match = re.search(
        r'public\s+String\s+getDefaultValue\s*\(\s*int\s+inputIndex\s*,\s*ValueType\s+desiredType\s*\)\s*\{(.*?)\n\s*\}',
        java_class.text,
        re.S,
    )
    if not method_match:
        return defaults
    body = method_match.group(1)
    indices = extract_index_constants(java_class.text)
    for name, value in indices.items():
        literal_match = re.search(
            rf'if\s*\(\s*inputIndex\s*==\s*{re.escape(name)}\s*\)\s*return\s*"([^"]*)"\s*;',
            body,
        )
        if literal_match:
            defaults[value] = literal_match.group(1)
    for literal_match in re.finditer(
        r'if\s*\(\s*inputIndex\s*==\s*(\d+)\s*\)\s*return\s*"([^"]*)"\s*;',
        body,
    ):
        defaults[int(literal_match.group(1))] = literal_match.group(2)
    ternary_match = re.search(
        r'return\s+inputIndex\s*==\s*(\d+)\s*\?\s*"([^"]*)"\s*:\s*"([^"]*)"\s*;',
        body,
    )
    if ternary_match:
        defaults[int(ternary_match.group(1))] = ternary_match.group(2)
    return defaults


def special_slots(node: NodeDoc, classes: dict[str, JavaClass]) -> tuple[list[Slot], list[Slot], list[str], list[str]] | None:
    java_class = classes[node.class_name]
    parent = java_class.parent
    args = first_constructor_super_args(java_class)

    if node.class_name == "MultiGateNode":
        return (
            [],
            [Slot("Out 1..N", "BRANCH", details="Configurable amount of branch outputs.")],
            ["The number of branch outputs is configured by the node card field `Outputs`."],
            ["A quantidade de saídas de branch e configurada pelo campo `Outputs` do card do node."],
        )

    if node.class_name == "FirstWinsNode":
        return (
            [Slot("In 1..N", "BRANCH", details="Configurable amount of branch inputs.")],
            [],
            ["The number of branch inputs is configured by the node card field `Inputs`."],
            ["A quantidade de entradas de branch e configurada pelo campo `Inputs` do card do node."],
        )

    if node.class_name == "SemaphoreNode":
        return (
            [Slot("In 1..N", "BRANCH", details="Configurable amount of branch inputs.")],
            [],
            ["The number of branch inputs is configured by the node card field `Inputs`."],
            ["A quantidade de entradas de branch e configurada pelo campo `Inputs` do card do node."],
        )

    if node.class_name == "PickComponentNode":
        return (
            [Slot("Object", "GAME_OBJECT", default="owner")],
            [
                Slot("Found", "BRANCH"),
                Slot("Missing", "BRANCH"),
                Slot("Component", "Selected component type"),
            ],
            ["The `Component` output type depends on the component selected in the node card."],
            ["O tipo da saida `Component` depende do componente selecionado no card do node."],
        )

    if node.class_name == "AttributeAccessNode":
        return (
            [],
            [Slot("Value", "Selected attribute type")],
            ["The `Value` output type depends on the attribute selected in the node card."],
            ["O tipo da saida `Value` depende do atributo selecionado no card do node."],
        )

    if node.class_name == "SetAttributeNode":
        return (
            [Slot("Value", "Selected attribute type")],
            [],
            ["The `Value` input type depends on the attribute selected in the node card."],
            ["O tipo da entrada `Value` depende do atributo selecionado no card do node."],
        )

    if node.class_name == "ComponentMethodNode":
        return (
            [Slot("Component", "Selected component type", default="Pick first component")],
            [Slot("Return", "Method return type", details="Only shown when the selected method returns a supported value.")],
            [
                "This node is configured from a Java component method.",
                "Additional inputs are created from the selected method parameters.",
                "The output only exists when the selected method returns a supported value.",
            ],
            [
                "Este node e configurado a partir de um metodo de componente Java.",
                "Entradas adicionais sao criadas a partir dos parametros do metodo selecionado.",
                "A saida so existe quando o metodo selecionado retorna um valor suportado.",
            ],
        )

    if parent == "BaseCollisionValueNode" and len(args) >= 4:
        return (
            [Slot("Collision", "COLLISION")],
            [Slot(clean_java_string(args[2]), args[3].split(".")[-1])],
            [],
            [],
        )

    if parent == "BaseCollisionIndexedValueNode" and len(args) >= 4:
        return (
            [Slot("Collision", "COLLISION"), Slot("Index", "NUMBER", default="0.0")],
            [Slot(clean_java_string(args[2]), args[3].split(".")[-1])],
            [],
            [],
        )

    if parent == "BaseContactValueNode" and len(args) >= 4:
        return (
            [Slot("Contact", "CONTACT")],
            [Slot(clean_java_string(args[2]), args[3].split(".")[-1])],
            [],
            [],
        )

    if parent == "BaseGetMaterialPropertyNode" and len(args) >= 4:
        return (
            [Slot("Material", "MATERIAL", default="Owner")],
            [Slot(clean_java_string(args[2]), args[3].split(".")[-1])],
            [],
            [],
        )

    if parent == "BaseSetMaterialPropertyNode" and len(args) >= 5:
        return (
            [
                Slot("Material", "MATERIAL", default="Owner"),
                Slot(clean_java_string(args[2]), args[3].split(".")[-1], default=clean_java_string(args[4])),
            ],
            [],
            [],
            [],
        )

    if parent == "BaseCustomEventArgNode" and len(args) >= 4:
        return (
            [],
            [Slot("Then", "BRANCH"), Slot(clean_java_string(args[2]), args[3].split(".")[-1])],
            ["The event name is configured in the node card."],
            ["O nome do evento e configurado no card do node."],
        )

    return None


def inherited_flag(classes: dict[str, JavaClass], class_name: str, flag: str) -> bool:
    current = class_name
    while current in classes:
        java_class = classes[current]
        if flag == "input" and RETURN_FALSE_INPUT_RE.search(java_class.text):
            return False
        if flag == "output" and RETURN_FALSE_OUTPUT_RE.search(java_class.text):
            return False
        if not java_class.parent or java_class.parent == current:
            break
        current = java_class.parent
    return True


def resolve_slots(node: NodeDoc, classes: dict[str, JavaClass]) -> None:
    special = special_slots(node, classes)
    notes_en: list[str] = []
    notes_pt: list[str] = []
    if special is not None:
        inputs, outputs, extra_en, extra_pt = special
        node.inputs = inputs
        node.outputs = outputs
        notes_en.extend(extra_en)
        notes_pt.extend(extra_pt)
    else:
        current = node.class_name
        found_inputs: list[Slot] | None = None
        found_outputs: list[Slot] | None = None
        while current in classes and (found_inputs is None or found_outputs is None):
            java_class = classes[current]
            if found_inputs is None:
                found_inputs = extract_named_slots(java_class.text, "inputs")
            if found_outputs is None:
                found_outputs = extract_named_slots(java_class.text, "outputs")
            if not java_class.parent or java_class.parent == current:
                break
            current = java_class.parent
        node.inputs = found_inputs or []
        node.outputs = found_outputs or []

    defaults = extract_defaults(classes[node.class_name])
    for index, slot in enumerate(node.inputs):
        if not slot.default and index in defaults:
            slot.default = defaults[index]

    node.top_flow_input = inherited_flag(classes, node.class_name, "input")
    node.top_flow_output = inherited_flag(classes, node.class_name, "output")
    if any(slot.type_name == "BRANCH" for slot in node.outputs):
        node.top_flow_output = False

    if node.class_name in {"OnForwardSpeedNode", "OnMovementSpeedNode", "OnSideSpeedNode"}:
        notes_en.append("The comparison mode is configured in the node card.")
        notes_pt.append("O modo de comparacao e configurado no card do node.")
    if node.class_name.startswith("CustomEvent"):
        notes_en.append("The event name is configured in the node card.")
        notes_pt.append("O nome do evento e configurado no card do node.")

    node.notes_en.extend(notes_en)
    node.notes_pt.extend(notes_pt)


def flow_label(value: bool, language: str) -> str:
    if language == "pt":
        return "`Sim`" if value else "`Nao`"
    return "`Yes`" if value else "`No`"


def describe_node(title: str, menu: str, language: str) -> str:
    lower_title = title.lower()
    if language == "pt":
        if menu.startswith("Events"):
            if lower_title.startswith("on "):
                return f"Evento que dispara quando a condicao `{title}` acontece."
            if lower_title == "loop":
                return "Evento que dispara continuamente enquanto o grafo estiver ativo."
            return f"Evento do sistema NoCode para `{title}`."
        if lower_title.startswith("get "):
            return f"Le um valor relacionado a `{title[4:]}` e disponibiliza o resultado nas saidas do node."
        if lower_title.startswith("set "):
            return f"Atualiza `{title[4:]}` usando os valores recebidos nas entradas."
        if lower_title.startswith("is "):
            return f"Verifica a condicao `{title[3:]}` e encaminha o fluxo conforme o resultado."
        if lower_title.startswith("add "):
            return f"Adiciona um novo valor ou elemento relacionado a `{title[4:]}`."
        if lower_title.startswith("remove "):
            return f"Remove o valor ou elemento relacionado a `{title[7:]}`."
        if lower_title.startswith("find "):
            return f"Procura o elemento ou recurso relacionado a `{title[5:]}`."
        if lower_title.startswith("swap "):
            return f"Troca a ordem ou a posicao dos itens envolvidos em `{title}`."
        if lower_title.startswith("load "):
            return f"Executa a operacao `{title}` dentro do fluxo NoCode."
        if menu.startswith("Flow"):
            return f"Controla o fluxo de execucao usando a logica de `{title}`."
        if menu.startswith("Math"):
            return f"Aplica a operacao matematica `{title}` sobre os valores conectados."
        if menu.startswith("Input"):
            return f"Fornece um valor de entrada para uso em outros nodes por meio de `{title}`."
        if menu.startswith("Actions"):
            return f"Executa a acao `{title}` dentro do fluxo NoCode."
        return f"Node NoCode responsavel por `{title}`."

    if menu.startswith("Events"):
        if lower_title.startswith("on "):
            return f"Event node that fires when `{title}` happens."
        if lower_title == "loop":
            return "Event node that fires continuously while the graph is active."
        return f"NoCode event node for `{title}`."
    if lower_title.startswith("get "):
        return f"Reads the value related to `{title[4:]}` and exposes the result on the node outputs."
    if lower_title.startswith("set "):
        return f"Updates `{title[4:]}` with the values received from the inputs."
    if lower_title.startswith("is "):
        return f"Checks the condition `{title[3:]}` and routes the flow based on the result."
    if lower_title.startswith("add "):
        return f"Adds a new value or element related to `{title[4:]}`."
    if lower_title.startswith("remove "):
        return f"Removes the value or element related to `{title[7:]}`."
    if lower_title.startswith("find "):
        return f"Searches for the element or resource related to `{title[5:]}`."
    if lower_title.startswith("swap "):
        return f"Swaps the order or position of the items involved in `{title}`."
    if lower_title.startswith("load "):
        return f"Executes the `{title}` operation inside the NoCode flow."
    if menu.startswith("Flow"):
        return f"Controls execution flow using the `{title}` logic."
    if menu.startswith("Math"):
        return f"Applies the `{title}` math operation to the connected values."
    if menu.startswith("Input"):
        return f"Provides an input value for other nodes through `{title}`."
    if menu.startswith("Actions"):
        return f"Executes the `{title}` action inside the NoCode flow."
    return f"NoCode node responsible for `{title}`."


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def render_slots(slots: list[Slot], language: str) -> str:
    if not slots:
        return "Nenhuma." if language == "pt" else "None."
    headers = ["Nome", "Tipo", "Padrao", "Detalhes"] if language == "pt" else ["Name", "Type", "Default", "Details"]
    rows: list[list[str]] = []
    for slot in slots:
        rows.append(
            [
                f"`{slot.name}`",
                f"`{slot.type_name}`",
                f"`{slot.default}`" if slot.default else "-",
                slot.details if slot.details else "-",
            ]
        )
    return markdown_table(headers, rows)


def render_notes(notes: list[str], language: str) -> str:
    if not notes:
        return ""
    heading = "## Observacoes" if language == "pt" else "## Notes"
    lines = [heading, ""]
    for note in notes:
        lines.append(f"- {note}")
    return "\n".join(lines)


def render_page(node: NodeDoc, language: str) -> str:
    title = node.title
    description = describe_node(title, node.menu, language)
    menu_label = "**Menu:**" if language == "pt" else "**Menu:**"
    input_flow_label = "**Fluxo de entrada superior:**" if language == "pt" else "**Top flow input:**"
    output_flow_label = "**Fluxo de saida superior:**" if language == "pt" else "**Top flow output:**"
    function_heading = "## Funcao" if language == "pt" else "## Purpose"
    inputs_heading = "## Entradas" if language == "pt" else "## Inputs"
    outputs_heading = "## Saidas" if language == "pt" else "## Outputs"
    notes = node.notes_pt if language == "pt" else node.notes_en

    parts = [
        f"# {title}",
        "",
        f"{menu_label} `{node.menu}`",
        "",
        f"{input_flow_label} {flow_label(node.top_flow_input, language)}",
        "",
        f"{output_flow_label} {flow_label(node.top_flow_output, language)}",
        "",
        function_heading,
        "",
        description,
        "",
        inputs_heading,
        "",
        render_slots(node.inputs, language),
        "",
        outputs_heading,
        "",
        render_slots(node.outputs, language),
    ]
    rendered_notes = render_notes(notes, language)
    if rendered_notes:
        parts.extend(["", rendered_notes])
    parts.append("")
    return "\n".join(parts)


def write_category(path: Path, data: dict[str, object]) -> None:
    lines = ["{"]
    items = list(data.items())
    for index, (key, value) in enumerate(items):
        rendered_value = str(value) if isinstance(value, int) else f'"{value}"'
        suffix = "," if index + 1 < len(items) else ""
        lines.append(f'  "{key}": {rendered_value}{suffix}')
    lines.append("}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def ensure_clean_directory(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def generate_docs(repo_root: Path, engine_root: Path) -> list[NodeDoc]:
    docs_root = repo_root / "docs" / "nocode"
    pt_root = repo_root / "i18n" / "pt" / "docusaurus-plugin-content-docs" / "current" / "nocode"
    ensure_clean_directory(docs_root)
    ensure_clean_directory(pt_root)
    write_category(docs_root / "_category_.json", ROOT_CATEGORY)
    write_category(pt_root / "_category_.json", PT_ROOT_CATEGORY)

    java_root = engine_root / "app" / "src" / "main" / "java"
    classes = extract_class_map(java_root)
    nodes = parse_registered_nodes(classes)
    for node in nodes:
        resolve_slots(node, classes)
        relative_dir = Path(*node.menu.split("/"))
        docs_dir = docs_root / relative_dir
        pt_dir = pt_root / relative_dir
        docs_dir.mkdir(parents=True, exist_ok=True)
        pt_dir.mkdir(parents=True, exist_ok=True)
        docs_path = docs_dir / f"{node.serialized_name}.mdx"
        pt_path = pt_dir / f"{node.serialized_name}.mdx"
        docs_path.write_text(render_page(node, "en"), encoding="utf-8")
        pt_path.write_text(render_page(node, "pt"), encoding="utf-8")
    return nodes


def validate_pairs(repo_root: Path) -> tuple[int, int]:
    docs_root = repo_root / "docs"
    pt_root = repo_root / "i18n" / "pt" / "docusaurus-plugin-content-docs" / "current"
    docs_files = {
        path.relative_to(docs_root).as_posix()
        for path in docs_root.rglob("*")
        if path.is_file() and path.suffix in {".md", ".mdx"}
    }
    pt_files = {
        path.relative_to(pt_root).as_posix()
        for path in pt_root.rglob("*")
        if path.is_file() and path.suffix in {".md", ".mdx"}
    }
    return len(docs_files - pt_files), len(pt_files - docs_files)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate NoCode documentation pages.")
    parser.add_argument("--engine-root", required=True, help="Path to the ITsMagic engine repository root.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    engine_root = Path(args.engine_root).resolve()
    nodes = generate_docs(repo_root, engine_root)
    missing_docs, extra_docs = validate_pairs(repo_root)
    print(f"Generated {len(nodes)} NoCode pages.")
    print(f"I18n validation delta: missing={missing_docs} extra={extra_docs}")
    return 0 if missing_docs == 0 and extra_docs == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
