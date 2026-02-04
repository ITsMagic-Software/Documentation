# Publicando Pacotes no ITsMagic Marketplace (GitHub)

Este guia explica, passo a passo, como publicar seu pacote no **ITsMagic Marketplace**.

Todas as submissões de pacotes são feitas criando um **Pull Request (PR)** para o repositório oficial de manifestos:

```
https://github.com/ITsMagic-Software/Packages-Manifest
```

---

## Visão geral (o que você fará)

1. Criar um repositório público no GitHub com o conteúdo do seu pacote.  
2. Fazer um fork (cópia) do repositório do Marketplace.  
3. Criar um **arquivo de manifesto** para o seu pacote dentro da pasta correta.  
4. Carregar seus **arquivos de mídia** (thumbnail + imagens) na pasta `media/`.  
5. Abrir um **Pull Request** com suas alterações.

---

## Etapa 1: Criar um repositório público no GitHub

O conteúdo do seu pacote deve estar em um **repositório público no GitHub**.

- Crie um novo repositório público no GitHub.  
- Envie todos os arquivos do pacote (cenas, scripts, assets, exemplos).  
- Copie a URL do repositório — você usará essa URL no manifesto.

---

## Etapa 2: Fazer o fork do repositório do Marketplace

1. Abra o repositório de manifestos:
```
https://github.com/ITsMagic-Software/Packages-Manifest
```
2. Clique em **Fork** para criar uma cópia no seu GitHub.  
3. Clone o fork para sua máquina local.

---

## Etapa 3: Criar o manifesto do pacote

Dentro do seu fork, crie a estrutura de pasta:

```
packages/seunomeusuario/seupacote/
```

Depois, crie um arquivo chamado:

```
packages/seunomeusuario/seupacote/manifest.json
```

### Exemplo de manifesto

```json
{
    "titleB64": "U2lzdGVtYSBkZSBzaW11bGHDp8OjbyBkZSBwYW5vIHBhcmEgSXRzIE1hZ2ljIEVuZ2luZS4=",
    "descriptionB64": "U2lzdGVtYSBkZSBzaW11bGHDp8OjbyBkZSBwYW5vIHNpbXBsZXMgcGFyYSBJdHMgTWFnaWMgRW5naW5lLiBwb3NzdWkgc2lzdGVtYSBkZSBjb2xpc29lcyBzaW1wbGVzLHZhcmlhcyBjb25maWd1cmHDp29lcyBlIHVtIHNpc3RlbWEgZGUgZWRpdG9yLHBvc3N1aSBIT1dfVE9fVVNF",
    "tags": "cloth,mesh,physics,malha,pano,fisica",
    "version": 1,
    "repositoryURL": "https://github.com/Vitg1/Mesh-Simulation-System-v1",
    "isTemplate": false,
    "date": "02/02/2026",
    "thumbnail": "capa.png",
    "images": [
        "img2.png",
        "img3.png",
        "img4.png",
        "img5.png",
        "img6.png",
        "img7.png",
        "img8.png"
    ]
}
```

---

## Explicação dos campos do manifesto

- **`titleB64`**  
  O título do pacote codificado em Base64.

- **`descriptionB64`**  
  A descrição do pacote codificada em Base64.

- **`tags`**  
  Palavras-chave separadas por vírgula para melhorar a busca pelo pacote.

- **`version`**  
  A versão do seu pacote. Comece em `1` e aumente quando publicar novas versões.

- **`repositoryURL`**  
  A URL do repositório público no GitHub contendo os arquivos do pacote.

- **`isTemplate`**  
  Defina como `true` se o pacote for um template de projeto; caso contrário, use `false`.

- **`date`**  
  A data da submissão no formato `dd/mm/aaaa`.

- **`thumbnail`**  
  Nome do arquivo principal de imagem do pacote (capa).

- **`images`**  
  Lista de nomes de arquivos de imagens adicionais (ex.: screenshots).

---

## Base64: Por que e como fazer

Os campos `titleB64` e `descriptionB64` precisam ser **codificados em Base64**.  
Isso assegura que o texto seja armazenado e exibido de forma segura pelo sistema.

### Como codificar texto em Base64

Você pode usar qualquer ferramenta de codificação Base64 (online ou local).

**Exemplo (texto simples):**

```
Sistema de simulação de pano para Its Magic Engine.
```

Convertido para Base64:

```
U2lzdGVtYSBkZSBzaW11bGHDp8OjbyBkZSBwYW5vIHBhcmEgSXRzIE1hZ2ljIEVuZ2luZS4=
```

Realize este processo para o título e descrição do pacote.

---

## Etapa 4: Adicionar arquivos de mídia

Dentro do seu fork do repositório do Marketplace, crie:

```
media/seunomeusuario/seupacote/
```

Exemplo:
```
media/Vitg1/Mesh-Simulation-System-v1/
```

Coloque suas imagens nessa pasta:

- A imagem `thumbnail` (conforme listado no manifesto).  
- Todas as imagens listadas em `images[]` no manifesto.

### Regras para imagens

- Tamanho máximo: **1 MB** por imagem  
- Formatos aceitos: **JPG ou PNG**  
- Recomendado: uma thumbnail + até **8 screenshots**

O nome da pasta deve corresponder exatamente ao valor que você usou em `mediaFolder` no manifesto.

---

## Etapa 5: Comitar e abrir um Pull Request

1. Comite o arquivo `manifest.json` em `packages/...`.  
2. Comite os arquivos de mídia em `media/...`.  
3. Envie as alterações para o seu fork.  
4. Abra um Pull Request:
   - **Repositório base:** `ITsMagic-Software/Packages-Manifest`
   - **Branch base:** `main`

Na descrição do PR, inclua:
- O nome do pacote
- Uma breve explicação do que o pacote contém

Os mantenedores do Marketplace revisarão o PR e o aprovarão quando estiver pronto.

---

## Atualizando seu pacote

Quando criar uma nova versão:

- Atualize o campo **`version`** no manifesto.  
- Atualize quaisquer imagens que tenham sido alteradas.  
- Envie um novo Pull Request com as mudanças.

---

## Revisão e aprovação

Todas as submissões são revisadas por moderadores.

- PRs aprovados serão mesclados e publicados.  
- Se forem necessárias mudanças, os moderadores deixarão feedback no Pull Request.

---

## Resumo

- Cada pacote tem um **manifesto JSON** em:
  ```
  packages/<seunomeusuario>/<seupacote>/manifest.json
  ```
- **Título e descrição** devem ser **codificados em Base64**.  
- As imagens ficam em:
  ```
  media/<seunomeusuario>/<seupacote>/
  ```
- As submissões são feitas por **Pull Request no GitHub**.
