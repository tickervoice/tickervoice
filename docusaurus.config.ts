import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Ticker Voice',
  tagline: 'A Telegram-based real-time stock price, indicator, candle formation voice alert and mock trading platform',
  favicon: 'img/logo.ico',

  future: {
    v4: true,
  },

  
  url: 'https://tickervoice.github.io',
  baseUrl: '/tickervoice/',

  organizationName: 'tickervoice', 
  projectName: 'tickervoice',    

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

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
          editUrl:
            'https://github.com/tickervoice/tickervoice/tree/main/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          editUrl:
            'https://github.com/tickervoice/tickervoice/tree/main/',
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
              label: 'Help',
              to: '/tickervoice/docs/helpmain',
            },
            {
              label: 'Installation',
              to: '/tickervoice/docs/install',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'YouTube',
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
              to: '/tickervoice/docs/disclaimer',
            },
            {
              label: 'Donation & Payment',
              href: 'https://www.paypal.com/donate', 
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Ticker Voice Project. All Copyrights Reserved`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
