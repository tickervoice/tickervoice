
# Batch Command
[Back to MainMenu](/docs/helpmain.md)
   * batch index from 0  to 9 only, if omit equal zero
   
   * Sample batch content  separate commands with ::
   
     - BatchID1(insert msglist8 autotrade silent)=insert [tickers] :: [tickers] apply msglist 8 :: [tickers] autotrade :: [tickers] silent
     
     - to run batch 1 with ticker list, tickers is key in ontent
       ~~~bash
       batch 1 tickers=nvda,amd       
       ~~~
     
     - to edit memo 
       ~~~bash
       batch 1 memo=new memo content
       ~~~
     
     - to create batch 1 commands either content= or cmds= or commands=
       ~~~bash
       batch 1 content=insert [tickers] :: [tickers] regular price    
       batch 1 tickers=aapl,amd
       ~~~

     - to remove batch 1, either one of two
       ~~~bash
       batch 1 content=    
       batch 1 remove  
       ~~~
     
     - if there is no items to be replaced in commads
       ~~~bash
       batch 4 content=change ticker=amd|[0] :: amd autotrade
       ~~~
     
     - batch run with no parameter specified, as there is no param set in content, pick either one of two
       ~~~bash
       batch 4 run 
       batch 4     
       ~~~
     
     
     
   [Back to MainMenu](/docs/helpmain.md)