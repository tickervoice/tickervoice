import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Easy to Use',
    Svg: require('@site/static/img/botqrcode.svg').default,
    description: (
      <>
        1) Scan QRcode in telegram app or just add <a href='https://t.me/mptmsgbot'>MPTMsgBot</a> 2) book with valid authcode, follow help instructions make your ticker settings 3) Download and run PC voice terminal program built with python. 4) Paid user will have access to relay version of PC voice terminal and android app 
      </>
    ),
  },
  {
    title: 'Join demo support group',  
    Svg: require('@site/static/img/demogroup.svg').default,
    description: (
      <>
        Scan QRcode in telegram app or just add <a href='https://t.me/tickervoicegroup'>TickerVoiceGroup</a> to get technical support also anybody can play around this bot without adding it privately, admin can do command demo and provide support.
      </>
    ),
  },
  {
    title: 'Plans',
    Svg: require('@site/static/img/plans.svg').default,
    description: (
      <>
        Current free tele private chat plan offer 30 days in a row with full feature. No payment method required.
        Free plan can be extended upon request after evaluation of first month use , donation accepted.
        Paid plan : Channel , Group 
        All type of accounts with reasonable limited ticker settings.
        Valid free trial authcode :        tickervoice      
        For paid authcode : contact <a href='https://t.me/tickervoice'>Sales</a>
        
      </>
    ),
  },
  
];

function Feature({title, Svg, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
