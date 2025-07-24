
# TickerVoice Q & A

## General Q & A
   * Q: Why I develop and use stock voice alert?
     - I have lots stock to monitor,but I do not have enough monitors, I need voice alert program to keep an eye on other cared tickers no matter price or key indicator signal
     - I am watching a focused stock, but I may miss some key signal if I did not pay attention at key signal moment
     - I feel tedious as current price action not exciting, I watch movies or news to have fun, meanwhile I have my alert system to notify me if anything comes up
     - I am not at my desk but I still need to know the price and key signals in case I can stop my handy work and do necessary trades ,current only support wifi area via android app or where ever if you can hear from your computer speaker.
     - typical case while I am in kitchen, toilet, in bed, or doing other housework
     
## Backend logic Q & A
   * Q: What data source ticker voice is processing from?
     - A: Core program fetching live stock quotes from yahoo finance web via yfinance python API, there maybe couple seconds delay.
   
   * Q: How frequent this program refreshing quotes?
     - A: different interval refresh data at a different frequency, for 5 minute interval, will fetch data every 20s, for 1 hour interval , will fetch data every 30s, then program process data and distribute to user will take another 2 to 3 seconds. frequency can be adjusted anytime upon request
   
   * Q: Will user receive duplicated message?
     - Yes and no. For each message type in every interval window will only send once to user, which means if there is another same indicator message coming, will not send during this interval time window , similar to regular price warning, if in one interval window, price no change, then will not send again. But if time window finished and new window begin, if same messages comes, will still be sent out. User may feel duplicated, but actually from different time window.  
   
   