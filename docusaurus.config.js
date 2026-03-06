// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import { themes as prismThemes } from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'ITsMagic',
  tagline: 'We Made The Impossible',
  url: 'https://itsmagic.com.br',
  baseUrl: '/documentation/',
  onBrokenLinks: 'throw',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
      onBrokenMarkdownImages: 'throw'
    },
    format: "detect"
  },
  favicon: 'img/favicon.ico',
  organizationName: 'ITsMagic',
  projectName: 'ITsMagic',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Remove this to remove the "edit this page" links.
          editUrl: 'https://github.com/ITsMagic-Software/Documentation/tree/main/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],
  plugins: [
    [
      require.resolve('@cmfcmf/docusaurus-search-local'),
      {
        indexDocs: true,
        indexPages: false,
        indexBlog: false,
        language: ['en', 'pt'],
      },
    ],
  ],
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'pt'],
    localeConfigs: {
      en: {
        htmlLang: 'en-GB',
        direction: 'ltr',
      },
      // You can omit a locale (e.g. fr) if you don't need to override the defaults
      pt: {
        direction: 'ltr',
      },
    },
  },

  themeConfig:
  /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: true,
        respectPrefersColorScheme: false,
      },
      navbar: {
        title: 'ITsMagic Documentation',
        logo: {
          alt: 'ITsMagic Documentation Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'doc',
            docId: 'intro',
            position: 'left',
            label: 'Documentation',
          },
          {
            type: 'localeDropdown',
            position: 'left',
          },
          /*{
            to: '/store',
            label: 'Store',
            position: 'left'
          },*/
          {
            href: 'https://play.google.com/store/apps/details?id=com.itsmagic.enginestable',
            label: 'Download',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Documentation',
                to: '/docs/intro',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'Discord',
                href: 'https://discord.gg/64wdG6gZdx',
              },
              {
                label: 'Whatsapp',
                href: 'https://chat.whatsapp.com/Ctgdap8YVRs07QfNaGvLLJ',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'ITsMagic 1.0',
                href: 'https://play.google.com/store/apps/details?id=com.itsmagic.enginestable',
              },
              {
                label: 'ITsMagic 2.0',
                href: 'https://play.google.com/store/apps/details?id=com.itsmagic.engine2',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} ITsMagic Engine, Inc.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.nightOwl,
        additionalLanguages: ['java']
      },
    }),
};

export default config;
