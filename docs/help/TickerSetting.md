
# Ticker Setting  
[Back to MainMenu](/docs/helpmain.md)
## TickerSettingMenu   
   * command demo:  ticker symbol all case insensitive
   * [/help_TickerMarketFormat](/docs/help/TickerSetting#tickermarketformat)
   * [/help_TickerAddRemoveView](/docs/help/TickerSetting#tickeraddremoveview)
   * [/help_TickerStatusChange](/docs/help/TickerSetting#tickerstatuschange)
   * [/help_TickerWarningPrice](/docs/help/TickerSetting#tickerwarningprice)
   * [/help_TickerRegularPrice](/docs/help/TickerSetting#tickerregularprice)
   * [/help_TickerStopLimit](/docs/help/TickerSetting#tickerstoplimit)
   * [/help_TickerShiftedStop](/docs/help/TickerSetting#tickershiftedstop)
   * [/help_TickerMovingAverage](/docs/help/TickerSetting#tickermovingaverage)
   * [/help_TickerTrailingStop](/docs/help/TickerSetting#tickertrailingstop)
   * [/help_TickerDayPercentageStop](/docs/help/TickerSetting#tickerdaypercentagestop)
   * [/help_ChangeRawTickerSetting](/docs/help/ChangeCommand#changerawtickersetting)
   * [/help_AutoTrade](/docs/help/MockTrading#automocktrading)
   * [/help_TickerSilent](/docs/help/TickerSetting#tickersilent)
## TickerMarketFormat
   * live Support US, Canada,Taiwan
   * yahoo US :  AAPL (live data)
   * yahoo Canada :   AC.TO  (live data)
   * yahoo Taiwan  :   0000.TW   (live data)
   * Currency:  USDCAD  (live data)
   * Commodity:  USOIL or OILUSD, XAUUSD,BTCUSD (live)   
   
   [TickerSettingMenu](/docs/help/TickerSetting#tickersettingmenu)
## TickerAddRemoveView
   * show one or multiple or all ticker
     ~~~bash
     show ticker aapl 
     show ticker aapl,amd
     show all ticker
     ~~~
   * add one or multiple ticker  
     ~~~bash
     add ticker aapl
     add stock aapl,amd  
     add tickers aapl
     add stocks aapl,amd
     add ticker aapl,amd
     insert aapl,amd
     ~~~
   * tickers limit including disabled ones  
   * remove ticker will also unapply allowed msglist
     ~~~bash
     remove aapl
     aapl remove
     remove aapl,amd
     aapl,amd  remove    
     remove all ticker
     remove all tickers
     remove any ticker
     remove any tickers
     ~~~

   [TickerSettingMenu](/docs/help/TickerSetting#tickersettingmenu)
## TickerStatusChange

   * to keep setting but disable ticker(s)
     ~~~bash
     pause aapl,amd
     disable aapl,amd
     ~~~
   * set price warning only no candle/indicator reminder
     ~~~bash     
     aapl price only - set price warning only no candle/indicator reminder
     aapl warning only - same as price only
     ~~~
   * to monitor candle/ indicator only no price 
     ~~~bash     
     aapl monitor only - to monitor candle/ indicator only no price 
     ~~~
   * remove all action code, set to be both candle/indicator and price available
     ~~~bash     
     resume aapl,amd
     enable aapl
     ~~~

   [TickerSettingMenu](/docs/help/TickerSetting#tickersettingmenu)
## TickerWarningPrice

   * to add positive warning price for a ticker, negative price to remove
     ~~~bash     
     aapl warning price 200,210
     aapl warning price -200,220
     ~~~
   * to remove warning price
     ~~~bash        
     aapl remove warning price
     aapl no warning price
     no warning price to aapl,amd
     no warning price to all
     ~~~

   [TickerSettingMenu](/docs/help/TickerSetting#tickersettingmenu)
## TickerRegularPrice
   * to notify price regularly 2 to 3 times per minute
     ~~~bash           
     aapl regular price
     ~~~
   * to remove regular price waring      
     ~~~bash
     aapl no regular price
     aapl,amd no regular price
     no regular price to aapl,amd
     no regular price to all
     ~~~

   [TickerSettingMenu](/docs/help/TickerSetting#tickersettingmenu)
## TickerStopLimit

   * Note: no=(no,del,delete,rm,remove,-)  ,  to=for, +/new/add/replace optional
   * to set stop limit price one price only 
     ~~~bash
     aapl stoploss 180
     aapl stopgain 250
     aapl stopbuy 250
     aapl +/new/add/replace stopbuy 250 
     ~~~
   * to remove stop loss/buy/gain,  to/for is to = for
     ~~~bash
     aapl,amd no stoploss
     aapl no stopbuy
     aapl no stopgain     
     no stop loss to/for all 
     no stop buy to/for all 
     no stop gain to/for all 
     ~~~
   * to remove both stop loss and stop gain
     ~~~bash   
     aapl no stop
     aapl no stoplimit
     no stop to/for all
     no stoplimit to/for all
     ~~~

   [TickerSettingMenu](/docs/help/TickerSetting#tickersettingmenu)
## TickerShiftedStop

   * Note: +/new/add/replace optional ,no=(no,del,delete,rm,remove,-)  ,  to=for
   * to set one shifted (last finished) candle low as stoploss 
     ~~~bash   
     aapl shifted stoploss 2
     ~~~      
   * to set one shifted (last last finished) candle high as stopgain
     ~~~bash   
     aapl shifted stopgain 3
     aapl shifted stopbuy 3
     aapl +/new/add/replace shifted stopbuy 3     
     ~~~      
   * to remove both shifted stoploss and gain
     ~~~bash      
     aapl,amd no shifted stop
     aapl no shifted stopbuy
     aapl no shifted stopgain
     no shifted stop loss to/for all
     no shifted stop buy to/for all
     no shifted stop gain to/for all
     no shifted stop to/for all
     no shifted stoplimit to/for all
     ~~~

   [TickerSettingMenu](/docs/help/TickerSetting#tickersettingmenu)
## TickerDayPercentageStop

   * this percentage stop is based on last day 4pm market closing price , float with or without % all means %
   * Note: +/new/add/replace optional , no=(no,del,delete,rm,remove,-)  ,  to=for     
     ~~~bash      
     aapl percentage stoploss 2.99 
     aapl percentage stoploss -3.99%
     aapl percentage stopgain 3
     aapl percentage stopbuy 3
     aapl +/new/add/replace percentage stopbuy 3
     ~~~
   * to remove both percentage stoploss and gain
     ~~~bash
     aapl,amd no percentage stop
     no percentage stop to/for all
     no percentage stoplimit to/for all
     ~~~
   * to remove percentage stoploss or gain
     ~~~bash
     aapl no percentage stopbuy
     aapl no percentage stopgain
     aapl no percentage stoploss
     no percentage stop loss to/for all
     no percentage stop buy to/for all
     no percentage stop gain to/for all
     ~~~

   [TickerSettingMenu](/docs/help/TickerSetting#tickersettingmenu)
## TickerTrailingStop
   * Note: +/new/add/replace optional , no=(no,del,delete,rm,remove,-)  ,  to=for     
   * to set % trailing stoploss or gain
     ~~~bash   
     aapl trailing stoploss 2.99
     aapl trailing stoploss -3.99%
     aapl trailing stopgain 3
     aapl trailing stopbuy 3
     aapl +/new/add/replace Trailing stopbuy 3
     ~~~
   * to remove both trailing stoploss and gain
     ~~~bash
     aapl,amd no trailing stop
     no trailing stop to/for all
     no trailing stoplimit to/for all
     ~~~          
   * to remove trailing stopbuy or gain
     ~~~bash
     aapl no trailing stopbuy
     aapl no trailing stopgain
     no trailing stop loss to/for all
     no trailing stop buy to/for all
     no trailing stop gain to/for all
     ~~~        

   [TickerSettingMenu](/docs/help/TickerSetting#tickersettingmenu)
## TickerMovingAverage
   * To set interested moving average and get price warning or MA cross up or down info, or confirmed up above MA or below,if no MA number set, will show selection menu, negative to remove , positive to add
     ~~~bash
     aapl moving average   -  this triggers ma selection menu
     aapl moving average 5,20,30
     aapl moving average 60,-30
     aapl remove moving average
     ~~~
     -![ma selection menu](/img/docs/mamenu.png)
     
   [TickerSettingMenu](/docs/help/TickerSetting#tickersettingmenu)
## TickerSilent
   
   - to set ticker to silent, either way, single or multiple
    ~~~bash
    change silent = AAPL,AMD
    AAPL silent
    AAPL enable silent
    TSLA,AMD silent
    ~~~
    
   - apply silent with needed one or multiple interval 
    ~~~bash
    change silent = AAPL:5m,AMD:1h  
    TSLA:5m,AMD:1h,MU:5m:1h silent
    ~~~
   
   - to remove silent for ticker, single or multiple
    ~~~bash
    AAPL remove silent      - to remove silent for ticker
    AAPL,AMD disable silent - to disable silent/make it unsilent for ticker
    ~~~
     
   [TickerSettingMenu](/docs/help/TickerSetting#tickersettingmenu) 

   [Back to MainMenu](/docs/helpmain.md)