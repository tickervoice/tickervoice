
# select msg 
[Back to MainMenu](/docs/helpmain.md)

## selectmsgb for series B 
   * to select from series B main [message list b](/docs/help/MsgListB.md), display at most 79 lines of menus,select anyone needed and save, optional memo content can be applied , this is a must step for global message type filter
     ~~~bash
     selectmsgb
     ~~~
     
     - set memo content = global use
     ~~~bash
     selectmsgb  global use    
     ~~~
     - config sample: AllowedMsgIDB(global use)=CC1-16CD1-12CS1-2EM1-4,11-14ER1-10KD1-10KR1-4MA1-6RC1RS1-10
          
     - to delete memo
     ~~~bash
     selectmsgb *
     selectmsgb delete memo
     selectmsgb remove memo
     ~~~
          
   * to set sub message type list in series B , 1 to 9 only, select and save
     ~~~bash
     selectmsgb 1
     ~~~
   
     - set memo content = sub bullish list , select and save
     ~~~bash
     selectmsgb 7 sub bullish list
     ~~~
     - config sample: AllowedMsgIDB7(sub bullish list)=CC4,6,8CD7EM3,13ER8,10KD3,9-10RC1
     
     - to delete memo
     ~~~bash
     selectmsgb 7 *
     selectmsgb 7 delete memo
     selectmsgb 7 remove memo
     ~~~
     
   
[Back to MainMenu](/docs/helpmain.md)