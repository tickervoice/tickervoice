
# MockTrading
[Back to MainMenu](/docs/helpmain.md)
## To resume balance (either way) initial 1000k
    
    ~~~bash
    resume balance 
    resume cash balance
    resume cashbalance
    ~~~
## Regular Order 
  * to trade share, ticker must be in setting
  * all order optionally can be followed with expire duration, be default 12h from current time ordered,dutaion to last could be 30m or 2h or 2d or 90d etc
    - to buy share , optional s after share acount, followed with optional expire time
      ~~~bash
      order buy amd 100s 116 
      order buy amd 100s 116 24h
      order buy amd 100  116 5d
      ~~~
    - to stopbuy share , optional s after share acount, optional limit price can be applied, followed with optional expire time , if only triggered price with no limit, then limit equal triggered price
      ~~~bash
      order stopbuy amd 100 126
      order stopbuy amd 100 126 128
      ~~~
    - to sell share, optional s after share acount, followed with optional expire time
      ~~~bash
      order sell amd 100s 116 
      order sell amd 100  116 
      ~~~
    - to stoploss share , optional s after share acount, optional limit price can be applied, followed with optional expire time , if only triggered price with no limit, then limit equal triggered price
      ~~~bash
      order stoploss amd 100 86 85
      order stoploss amd 100 86 85
      ~~~  
    - to short share, optional s after share acount, followed with optional expire time
      ~~~bash
      order short amd 100s 116 
      order short amd 100  116 
      ~~~
    - to stopshort share , optional s after share acount, optional limit price can be applied, followed with optional expire time , if only triggered price with no limit, then limit equal triggered price
      ~~~bash
      order stopshort amd 100 86 85
      order stopshort amd 100 86 85
      ~~~  
    - to cover share , optional s after share acount, followed with optional expire time
      ~~~bash
      order cover amd 100s 116 
      order cover amd 100s 116 24h
      order cover amd 100  116 5d
      ~~~
    - to stopcover share , optional s after share acount, optional limit price can be applied, followed with optional expire time , if only triggered price with no limit, then limit equal triggered price
      ~~~bash
      order stopcover amd 100 126
      order stopcover amd 100 126 128
      ~~~

## To remove order       

  * to remove specific order id or any order for ticker , need to sell off related holding  or just do resume cash balance to remove hoding , pending order and trading history
    ~~~bash
    order remove 2 amd  
    remove order 2 amd  
    remve order any amd 
    order remove all amd 
    ~~~

## Strategy order

  * OTA - One Tiggers Another , 2 orders only by comma 
    ~~~bash
    order ota buy crwv 200 150 48h, stopbuy crwv 200 160 161 48h
    order ota stopshort crwv 200 150 149 , stopcover crwv 200 160 161
    order ota buy crwv 1000 146 5d, sell crwv 1000 147 5d
    order ota buy crwv 100 180,stoploss crwv 100 90 88
    ~~~
    
  * OCO - One Cancels Another , 2 orders only by comma 
    ~~~bash
    order oco buy crwv 300 150 , stopbuy crwv 300 160 161
    order oco stopshort crwv 300 150 149 , short crwv 300 165
    order oco sell crwv 300 180 , stoploss crwv 300 140 135
    order oco buy crwv 100 180, stopbuy crwv 100 200 201    
    ~~~

  * OOTA - One Triggeres (OTA) , 3 orders only by comma     
    ~~~bash
    order oota buy crwv 100 180, sell crwv 100 200, buy crwv 100 190
    ~~~

  * OOCO - One Triggeres (OCO) , 3 orders only by comma     
    ~~~bash
    order ooco buy crwv 100 180,sell crwv 100 200,stoploss crwv 100 90 88
    ~~~
    
    buy order will be filled if market price got equal or below ordered price
    sell order will be filled if market price got equal or above ordered price
    stopbuy order will be filled if market price got equal or above ordered price
    stoploss order will be filled if market price got equal or below ordered price
    
## View pending order    
  * to view pending order (optional item)
    ~~~bash  
    order pending
    pending order
    ~~~
    
## View holding
    ~~~bash  
    holding
    ~~~

## View trades done
  * to view trading history record, either one,Trades history record keep 50 at most
    ~~~bash
    trades done
    trade done
    trading history
    trading record/rec
    trading rec
    trading summary
    ~~~
    
## Margine rate and funds locked
  * there is 50% margin , 50% deposit locked
  * mixed account of long and short, double funds locked for cover

## AutoMockTrading

   - to set autotrade tickers, either way, single or multiple
    ~~~bash
    change autotrade = AAPL,AMD
    AAPL (enable) auto trade
    TSLA,AMD autotrade
    TSLA,AMD enable auto trade
    ~~~
    
   - apply auto trade with needed one or multiple interval 
    ~~~bash
    change autotrade = AAPL:5m,AMD:1h  
    TSLA:5m,AMD:1h,MU:5m:1h autotrade  
    ~~~
   
   - to remove auto trade for ticker, single or multiple
    ~~~bash
    AAPL remove auto trade      - to remove auto trade for ticker
    AAPL,AMD disable auto trade      - to disable auto trade for ticker
    ~~~

   [Back to MainMenu](/docs/helpmain.md)