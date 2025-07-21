
# SubAllowedMsgForTicker
[Back to MainMenu](/docs/helpmain.md)
* each user with 1 to 9 allowed msg list to build apart from global main one
* each ticker can only be applied to one sub allowed msg type list
* if already applied to one list , then try to apply to another, the previous one will be unapplied automatically
* deselect all and save will remove the list
* remove ticker will also do unapply 
* /selectmsg     - to build global main one applied to all tickers by default
    - to build sub spare list index 1
    ~~~bash 
    selectmsg  1    
    ~~~
    - selectmsg  0  - same as selectmsg
    - apply (global memo) for this list setting
    ~~~bash 
    selectmsg global memo 
    ~~~
    - apply (bulish msg) as memo for this list setting 
    ~~~bash 
    selectmsg  1  bullish msg
    ~~~    
* /listmsg          - to view all message types 
* apply and unapply ticker to allowed msg type list
    - to apply one stock to allowed msg type list 1
    ~~~bash 
    intc apply msglist 1 
    ~~~
    - to apply multiple stock to allowed msg type list 2
    ~~~bash 
    amd,nvda apply msglist 2 
    ~~~
    - to unapply ticker from sub allowed msg list
    ~~~bash 
    intc,amd unapply msglist 
    ~~~
[Back to MainMenu](/docs/helpmain.md)