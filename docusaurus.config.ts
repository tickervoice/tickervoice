import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Ticker Voice',
  tagline: 'A telegram based real-time stock price, indicator, candle formation voice alert and mock trading platform',
  favicon: 'img/logo.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://tickervoice.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  //baseUrl: '/',
  baseUrl: '/tickervoice/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  //organizationName: 'facebook', // Usually your GitHub org/user name.
  //projectName: 'docusaurus', // Usually your repo name.
  organizationName: 'tickervoice',
  projectName: 'tickervoice', 
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          //editUrl:
            //'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
          editUrl:
            'https://github.com/tickervoice/tickervoice/tree/main/',  
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          //editUrl:
            //'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
          editUrl:
            'https://github.com/tickervoice/tickervoice/tree/main/',  
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    //image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'Ticker Voice',
      logo: {
        alt: 'Ticker Voice Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Help',
        },
        {to: '/docs/install', label: 'Installation', position: 'left'},
        {to: '/docs/readmes', label: 'Readme', position: 'left'},
        {to: '/docs/usecase', label: 'Usecase', position: 'left'},
        {to: '/docs/qanda', label: 'Q & A', position: 'left'},
        {
          href: 'https://t.me/tickervoicegroup',
          label: 'Telegram demo group',
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
              label: 'Readme', 
              to: '/docs/readmes',
            },
            {
              label: 'Help',
              to: '/docs/helpmain',
            },
            {
              label: 'Installation', 
              to: '/docs/install',
            },
            {
              label: 'Usecase', 
              to: '/docs/usecase',
            },
            {
              label: 'Q & A', 
              to: '/docs/qanda',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Youtube',
              href: 'https://www.youtube.com/@TickerVoice',
            },
            {
              label: 'Telegram demo group',
              href: 'https://t.me/tickervoicegroup',
            },
            {
              label: 'X',
              href: 'https://x.com/tickervoice',
            },
          ],
        },
        {
          title: 'More',
          items: [
            
            {
              label: 'Support & Sales',
              href: 'https://t.me/tickervoice',
            },
            {
              label: 'Disclaimer',
              href: '/docs/disclaimer',
            },
            {
              label: 'Donation & Payment',
              href: '/docs/payment',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Ticker Voice Project in Ontario Canada. All Copyrights Reserved `,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
