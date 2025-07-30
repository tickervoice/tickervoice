
# Use cases
      
## 1) voice remind me ticker price, do not send other messages about this ticker
   - Sample regular price msg received
     ~~~bash
     TSLA $320.60 0729101921-0458f0
     ~~~
   * option 1,at least two commands to set , prerequisite to selectmsg for global use to include RC01
     ~~~bash
     selectmsg 9        - select only RC01 and save list
     tsla apply msglist 9
     ~~~ 
     ~~~bash
     insert tsla
     tsla regular price
     ~~~ 
   * option two, make the commands to be a batch command set
     ~~~bash
     selectmsg 9  - select only RC01 and save list
     batch 9 content=insert [tickers] :: [tickers] regular price :: [tickers] apply msglist 9  
     ~~~
     - run batch to receive regular price voice reminder , the 'tickers' is a variable can be changed to any string key
     ~~~bash
     batch 9 tickers=tsla     - if multiple ticker separate by comma  
     ~~~
   * option 3,if do not set sub msglist filter, also need to filter out non price message, set (interval key one or many separate with comma) in notcare list, 
     ~~~bash 
     change notcare=5 minute,1 hour   -- all messages contain these two string will not be sent to user  
     ~~~
     ~~~bash
     insert tsla
     tsla regular price
     ~~~     

## 2) holding stock , only care about when to sell 
   * make a sub msglist with only negative confirmed signal , such as kdj death cross, emacd death cross, kdj down from top, ......
     ~~~bash
     selectmsg 2 this is bearish memo   - select from menu and save , the content after index is memo
     ~~~
     ~~~bash
     tsla:5m apply msglist 2   - :5m is optional , means only apply 5m signal to tsla
     ~~~
   - sample msglist 2 in config text(this is compressed text, not readable, need to view in selectmsg 2 command) : 
     ~~~bash   
     AllowedMsgID2[TSLA:5m](this is bearish memo)=CC1,3,5,7CD8,10CS1-2EM4,14ER7,9KD4,7RC1RS7,9
     ~~~   

## 3) holding cash , monitoring stocks , care about when to buy
   * make a sub msglist with only positive confirmed signal , such as kdj golden cross, emacd golden cross, kdj up from bottom, ......
     ~~~bash
     selectmsg 1 this is bullish memo   - select from menu and save , the content after index is memo
     ~~~
     ~~~bash
     tsla:1h apply msglist 1   - :1h is optional , means only apply 1h signal to tsla
     ~~~
   - sample msglist 1 in config text(this is compressed text, not readable, need to view in selectmsg 1 command) : 
     ~~~bash   
     AllowedMsgID1[TSLA:1h](this is bullish memo)=CC4,6,8CD7EM3,13ER8,10KD3,9-10RC1
     ~~~   
    
## 4) more to come     
     
     
     