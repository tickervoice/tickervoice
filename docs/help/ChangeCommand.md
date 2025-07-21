
# ChangeCommands
[Back to MainMenu](/docs/helpmain.md)
## ChangeCommandMenu
   * [/help_ChangeRawTickerSetting](/docs/help/ChangeCommand#changerawtickersetting)
   * [/help_ChangeIndicatorInterest](/docs/help/ChangeCommand#changeindicatorinterest)
   * [/help_ChangeInterval](/docs/help/ChangeCommand#changeinterval)
   * [/help_ChangeFilter](/docs/help/ChangeCommand#changefilter)

## ChangeRawTickerSetting

   * Always run other friendly commands unless you've already saved previous raw settings 
   * raw ticker setting sample:  
     - change ticker=aapl|Apple Inc|[200,201:0:10002:-2:-10180:20230]|W,amd
     - AAPL - monitor stock , no price alert
     - AAPL|[0] - monitor stock , regular price alert
     - AAPL|N - to monitor stock , no price alert , disabled
     - AAPL|[220,230] or AAPL|[220:230]- monitor stock , do price alert
     - AAPL|[220,230]|N - monitor stock , do price alert, disabled
     - AAPL|[220,230]|M - monitor stock indicator only 
     - AAPL|[220,230,0]|W - just do price alert including any price 0
     - AAPL|[-2] - shiftedcandle stoploss alert always from -2, as -1 is current candle
     - AAPL|[10002] - shiftedcandle stopbuy alert always from 10002 or up, 2,3 to check the shifted last candle 
     - AAPL|[-10200]- stoploss alert from abs10k or up, abs minus 10k is the stoploss $200
     - AAPL|[20250]- stopbuy alert from 20k or up, minus 20k is the stock price $250
     - AAPL|Apple Inc|[220:230] - to monitor stock show company name , do price alert
     - AAPL|Apple Inc|[220:230]|N - same as above but disabled
     - AAPL,AMD|[100],NFLX - multiple tickers 
     - AAPL|[100],AAPL,NFLX - Duplicate ticker latter one will overwrite prior one
   * If multiple price alert, separate price with : or , if there are multiple lines for tickers, you still need comma at line end 
     ~~~bash
     /change ticker = 
       AMD|[101,100],
       AAPL,BB,
       AAL,DAL
     ~~~  
   * Ticker can contain . such as Canada stock   AC.TO , 2330.TW 
   * Company name should be more than one char after first ticket str followed with |
   * B is what so ever not necessary and equal to no B followed , M is what so ever not necessary if only ticker there
   * Company like nick name can be changed in what ever way without comma inside
   * all ticker setting mode can add |N to do temp disable , remove |N to reactivate
   * Ticker length max 9 , ABCDE.XX the longest allowed in [] over 30000 for moving average combination, no need to prepare manually unless you already know
        
   * raw ticker change samples :
     ~~~bash 
     /change ticker add nvda ,goog|google|[155]     
     /change ticker del (or delete or remove or rm) nvda ,goog
     /change ticker disable (or pause or deactivate)  nvda 
     /change ticker enable (or resume or activate) nvda 
     /change ticker revise (or rev or modify or mod or rv or md or ch) nvda|N
     ~~~

    [ChangeCommandsMenu](/docs/help/ChangeCommand#changecommandmenu)
## ChangeIndicatorInterest

    ~~~bash
    /change kdj/rsi/macd = on/yes/y/1 - to make it true to enable 
                         = 5m         - just make it active for 5m interval 
                         = 5m,1h      - to make it active for 5m,1h intervals
    ~~~               

## ChangeInterval

    ~~~bash
    /change interval=1m,5m,1h,1d
    ~~~

## ChangeFilter

    ~~~bash
    /change
        OnlyCareMsgFilter or onlycarefilter or onlycare =aa&bb,ccc   (comma for or, & for and)
        OnlyCareExceptedTickers or exceptedtickers or excepted or except or ocexcept = ABCD,EFGH
        NotCareMsgFilter or notcarefilter or notcare = dd&ee,ff (comma for or, & for and) 
                         when above onlycare effective, notcare logic will be added on top
        NotCareExceptedTickers or notcareexcepted or ncexcept or ncticker = EFGH 
        Silent or silent or silentticker = ABCD,EFGH 
        Silent or silent or silentticker = ABCD:5m,EFGH:1h   - silent on 5m signal or 1h signal only
        change silent = AAPL,MU  - change ticker message to be silent , do not voice read
        change silent = AAPL:5m,MU  - change ticker message to be silent , do not voice read
        AMD silent
        AMD:5m silent
        AMD:5m:1h update silent
        AMD remove silent
    ~~~
    
    [ChangeCommandsMenu](/docs/help/ChangeCommand#changecommandmenu)
    
    [Back to MainMenu](/docs/helpmain.md)