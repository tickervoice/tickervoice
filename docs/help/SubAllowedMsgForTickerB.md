
# SubAllowedMsgForTicker Series B
[Back to MainMenu](/docs/helpmain.md)
* each user with 1 to 9 allowed msg list to build apart from global main one
* each ticker can only be applied to one sub allowed msg type list
* if already applied to one list , then try to apply to another, the previous one will be unapplied automatically
* deselect all and save will remove the list
* remove ticker will also do unapply 
* /selectmsgb     - to build global main one applied to all tickers by default
    - to build sub spare list index 1
    ~~~bash 
    selectmsgb  1    
    ~~~
    - selectmsgb  0  - same as selectmsg
    - apply (global memo) for this list setting
    ~~~bash 
    selectmsgb global memo 
    ~~~
    - apply (bulish msg) as memo for this list setting 
    ~~~bash 
    selectmsgb  1  bullish msg
    ~~~    
* /listmsgb          - to view all message types 
* apply and unapply ticker to allowed msg type list
    - to apply one stock to allowed msg type list 1
    ~~~bash 
    intc apply msglistb 1 
    ~~~
    - to apply one stock with certain interval only to allowed msg type list 1
    ~~~bash 
    intc:5m apply msglistb 1 
    ~~~
    ~~~bash 
    intc:5m:1h apply msglistb 1 
    ~~~
    - to apply multiple stock to allowed msg type list 2
    ~~~bash 
    amd,nvda apply msglistb 2 
    ~~~
    - to unapply ticker from sub allowed msg list
    ~~~bash 
    intc,amd unapply msglistb 
    ~~~
    - to unapply ticker from sub allowed msg list, here will ignore interval, just apply all about this ticker
    ~~~bash 
    intc:5m,amd:1h unapply msglistb   - equal to intc,amd unapply msglist 
    ~~~
[Back to MainMenu](/docs/helpmain.md)