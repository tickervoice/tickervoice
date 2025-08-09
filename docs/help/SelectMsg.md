
# select msg 
[Back to MainMenu](/docs/helpmain.md)

## selectmsg for series A 
   * to select from series A main [message list a](/docs/help/MsgList.md), display at most 79 lines of menus,select anyone needed and save, optional memo content can be applied , this is a must step for global message type filter
      
     ~~~bash
     selectmsg   --  this will trigger menu confirm and save
     ~~~
     ![menu](/img/docs/selectmsgmenu.png) 
     - set memo content = global use
     ~~~bash
     selectmsg  global use  --  this will trigger menu confirm and save  
     ~~~
     - config sample: AllowedMsgIDA(global use)=CC1-16CD1-12CS1-2EM1-4,11-14ER1-10KD1-10KR1-4MA1-6RC1RS1-10

     - to delete memo 
     ~~~bash
     selectmsg *             --  this will trigger menu confirm and save  
     selectmsg delete memo   --  this will trigger menu confirm and save  
     selectmsg remove memo   --  this will trigger menu confirm and save  
     ~~~
          
   * to set sub message type list in series A , 1 to 9 only, select and save
     ~~~bash
     selectmsg 1   --  this will trigger menu confirm and save  
     ~~~
   
     - set memo content = sub bullish list , select and save
     ~~~bash
     selectmsg 7 sub bullish list --  this will trigger menu confirm and save  
     ~~~
     - config sample: AllowedMsgIDA7(sub bullish list)=CC4,6,8CD7EM3,13ER8,10KD3,9-10RC1

     - to delete memo
     ~~~bash
     selectmsg 7 *  --  this will trigger menu confirm and save  
     selectmsg 7 delete memo --  this will trigger menu confirm and save  
     selectmsg 7 remove memo --  this will trigger menu confirm and save  
     ~~~
[Back to MainMenu](/docs/helpmain.md)