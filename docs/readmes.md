
# TickerVoice  

   * a telegram based real-time stock price, indicator, candle formation voice alert and mock trading platform
   * Telegram bot name:  MPTMsgBot , free service register code :   tickervoice

## Support Market
   * Support Martket  :   [US](/docs/help/USTickers),Canada,[fx](/docs/help/NonStockTickers#currency),[Commodity](/docs/help/NonStockTickers#commodity),[crypto](/docs/help/NonStockTickers#crypto) (live data)  other market upon request
   * Support Interval  :  5m,1h  # other interval upon request 1m,15m ,30m flexible
   * Support Telegram chat type:  Private , channel, group   (channel, group with no free service except demo group by admin)

## Service Time Window
   * live data processed on Trading days 7am to 17pm, other time can do any offline setting via botservice
   
## Tech support 
   * add bot MPTMsgBot online within chat box, run command : /msg support messagebody (optional your alias)
   * talk to admin https://t.me/tickervoice
   * join demo group https://t.me/tickervoicegroup
   * or send email : tickervoice@gmail.com

## Message Types
   * all alert based on a set of accepted message types
   * each user maintains a global message types list, as well as other 9 sub message types list be used to do auto trading or alert filter for tickers

## stock price alert
   * multiple warning price met
   * price stop limit met , 1 for both way, auto remove limit after more than 3m triggered 
   * shifted candle stop alert
   * day change % met
   * candle trailing % met 
   * MA price met , ma cross alert
   
## stock indicator alert
   * KDJ,EMACD,RSI,ERSI
   
## stock candle formation alert
   * multiple white/red soldier as well as reversal alert
   * grave stone doji alert
   * beyond morning high or low alert
   * and many more......

## Mock trading
   * optional can apply ticker to a customized sub message type list
   * auto mock trading demo based on score of alert message type (not a source to be followed for real trading)
   * auto trading can be set for certain intervals signal only 
   * manual mock trading to record and confirm user's intention 
   * margin rate set to be 50%
   * holding position avg cost recorded , funds amount locked the same way as real brokers do
   * for manual trading OTA, OCO, OOTA, OOCO provided
   * all order can be applied expired time from 1 minute to 99 days
   * historical trade kept for 50 records only

## batch command
   * each user can maintian 9 batch command list, make it easy to repeat running pre-set commands, parameters can be replaced if any,this can help to remember your existing complex setting in case you need to switch back and forth

## silent message
   * alert messages for ticker can be silent for certain interval or all interval with no voice reading, or voice reading

## message filter
   * user with 4 global filter string setting to filter out certain message content 
     only care key, only care excepted tickers, not care key, not care excepted tickers

## service pause / resume
   * alert service can be globally paused when user don't want to receive msg, and can resume any time
   * each ticker can be individually disabled or enabled withnot removing setting

## voice terminal
   * voice reading terminal provided to run at user's terminal computer  (python source code provided for free)
   * paid user get android app provided to do wifi network voice and message relay 
     app communicates with pc terminal program automatically sync dynamic ip address as well as ports change if any, if not for relay voice alert, app can be used to relay computer stereo sound to cellphone, for entertainment use such as warching movies, listen to music
          
## event alert message
   * event (10) alert  provided to schedule personal alert message, also support play local sound file       

## message between accounts
   * user can communicate with admin to get support:   message support  YOUR questions  (your alias)
   * You can also message other member if you know their alias or chatid, you have multiple alias to set , you can tell different friend different alias, but if they send message to you , you will receive in your only chatbox with the alias your friend know of you, when you reply message to your friend, you can also only specify the alias they know of you

## plans
   * 30 days free trial period upon request , can be extended 30 days in a row if needed, no payment method required, all type of accounts with maxtimum certain limited tickers be configured into setting but all full functional, free account accept donation, who ever donated may be qualified to register with paid offer code and get more tickers limit and android media relay app, and full support and analysis accordingly. Only private chat service with bot is free , paid plan for channel and group service.  

