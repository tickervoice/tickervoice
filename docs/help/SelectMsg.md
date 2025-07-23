
# selectmsg
[Back to MainMenu](/docs/helpmain.md)
   * to select from main message list, display at most 79 lines of menus,select anyone needed and save, optional memo content can be applied , this is a must step for global message type filter
     ~~~bash
     selectmsg 
     ~~~
     
     - set memo content = global use
     ~~~bash
     selectmsg  global use    
     ~~~
     - config sample: AllowedMsgID(global use)=CC1-16CD1-12CS1-2EM1-4,11-14ER1-10KD1-10KR1-4MA1-6RC1RS1-10
          
   * to set sub message type list, 1 to 9 only, select and save
     ~~~bash
     selectmsg 1
     ~~~
   
     - set memo content = sub bullish list , select and save
     ~~~bash
     selectmsg 7 sub bullish list
     ~~~
     - config sample: AllowedMsgID7(sub bullish list)=CC4,6,8CD7EM3,13ER8,10KD3,9-10RC1
   
[Back to MainMenu](/docs/helpmain.md)