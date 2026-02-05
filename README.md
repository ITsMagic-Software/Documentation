# ITsMagic Documentation

Official repository for the ITsMagic Engine documentation.

- Documentation site: https://itsmagic.com.br/documentation
- Repository & contribution guide: https://itsmagic.com.br/documentation/docs/topics/documentation-repository

## How to contribute

1. Fork the repository.
2. Create or edit files in `docs/` (or `docs/topics/`).
3. Keep translations in sync under `i18n/pt/docusaurus-plugin-content-docs/current/`.
4. Commit and open a Pull Request.

## Requirements

- Node.js + npm

## Local build

```bash
npm install
npm run build
```

## Useful scripts

- `npm run start` — local dev server
- `npm run build` — production build

## Structure

- `docs/` — English documentation (source of truth)
- `i18n/pt/docusaurus-plugin-content-docs/current/` — Portuguese documentation
- `tools/` — build and deploy scripts
