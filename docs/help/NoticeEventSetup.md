
# NoticeEventSetup
[Back to MainMenu](/docs/helpmain.md)
   * each user with 10 events to book , main event and index from 1 to 9
   * supported date format YYYY-MM-DD , YY-MM-DD, YYYY/MM/DD, YY/MM/DD,  YYYYMMDD ,   YYMMDD     
     - to show remaining event report
      ~~~bash
      event
      ~~~
     - To setup main event with no index
      ~~~bash 
      event 2025-04-25 2:30pm your event content   
      event 20250425 14:30 your event content   
      event 2025/04/25 2:30p your event content   
      ~~~
     - To setup onetime event at index 1 
      ~~~bash 
      event 5 2025-04-25 2:30pm your event content   
      ~~~
     - To setup recurrence event on Mon,Tue at index 2 
      ~~~bash
      event 2 3:30pm w12  your event content
      ~~~
     - To setup recurrence event everyday
      ~~~bash
      event 3 1:30pm w1234567  your event content   
      ~~~
     - To setup recurrence event on weekdays
      ~~~bash
      event 3 4:30pm w12345  your event content   
      ~~~
     - To setup recurrence event every month day 5,10
      ~~~bash
      event 3 4:30pm m5,10  your event content   
      ~~~
     - To play message with customized sound play, make sure sound file in UserMedia folder ,
      ~~~ bash
      event 7:00 wake up :play(zml.mp3)
      ~~~
     - to remove main event, either one
      ~~~bash
      event remove 
      remove event 
      event remove 0
      ~~~
     - to remove event 1 to 9
      ~~~bash
      event remove 1
      event remove 1,2
      remove event 1,2
      ~~~
     
   [Back to MainMenu](/docs/helpmain.md)