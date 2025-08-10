
# Mock Trading Test Cases margin rate 50%
[Back to MainMenu](/docs/helpmain.md)

## Initial 
    * reset balance , view holding, pending order
    ~~~bash
    resume balance 
    ~~~
    ~~~bash
    cash balance resumed, holding, pending order and trading history removed
    ~~~
    ~~~bash
    holding
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $1,000,000.00
    🟢 Buying Power: $2,000,000.00

    🗃 No holdings.

    💼 Total Net Value:      $1,000,000.00         0.00%
    ~~~
    ~~~bash
    pending order
    ~~~
    ~~~bash
    💰 Cash Balance: $1,000,000

    📋 No pending orders.
    ~~~

##  order buy full amount 
    ~~~bash
    order  buy crwv 10000 100
    ~~~
    ~~~bash
    order taken. buying power 1000000.00
    ~~~
    ~~~bash
    holding
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $1,000,000.00
    🔒 Order locked balance: $1,000,000.00
    🟢 Buying Power: $1,000,000.00

    🗃 No holdings.

    💼 Total Net Value:      $1,000,000.00         0.00%
    ~~~
    ~~~bash
    pending order
    ~~~
    ~~~bash
    💰 Cash Balance: $1,000,000

    📋 Pending Orders:
    🛒[1,A]buy CRWV 10000@$100=$1,000,000 e250811 0301

    🧾 Total Funds locked:  $1,000,000
    🟢 Buying Power: $1,000,000
    ~~~
    
## double order to run out of margin
    ~~~bash
    order  buy crwv 10000 100
    ~~~
    ~~~bash
    order taken. buying power 1000000.00
    ~~~
    ~~~bash
    holding
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $1,000,000.00
    🔒 Order locked balance: $2,000,000.00
    🟢 Buying Power: $0.00

    🗃 No holdings.

    💼 Total Net Value:      $1,000,000.00         0.00%    ~~~
    ~~~bash
    pending order
    ~~~
    ~~~bash
    💰 Cash Balance: $1,000,000

    📋 Pending Orders:
    🛒[1,A]buy CRWV 10000@$100=$1,000,000 e250811 0301
    🛒[2,A]buy CRWV 10000@$100=$1,000,000 e250811 0306

    🧾 Total Funds locked:  $2,000,000
    🟢 Buying Power: $0
    ~~~
    - raw setting
    ~~~bash
    PendingOrder=1:A:buy:CRWV:10000:100.0:100.0:1754881566,2:A:buy:CRWV:10000:100.0:100.0:1754881566
    OrderId=2
    CashBalance=1000000
    Holding=
    TradesDone=    
    ~~~
    
## 2 buy orders processed
    -send_udp_message("CRWV", "100","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    ~~~bash
    order filled bought CRWV 10000 shares at $100.00,bought CRWV 10000 shares at $100.00  0810125049-046ce6
    ~~~   
    ~~~bash
    holding
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $-1,000,000.00
    🟢 Buying Power: $0.00

    🗃 Holdings: (market value vs cost base) 
    💸 CRWV 20000s M$100.0 = $2,000,000.00 C$100.000, 0.00%

    📦 Long Holding Value: $2,000,000.00
    💼 Total Net Value:      $1,000,000.00         0.00%
    ~~~
    ~~~bash
    pending order
    ~~~
    ~~~bash
    💰 Cash Balance: $-1,000,000

    📋 No pending orders.
    ~~~
    - raw setting
    ~~~bash
    PendingOrder=
    OrderId=2
    CashBalance=-1000000.0
    Holding=CRWV:20000:100.0
    TradesDone=1:F:buy:CRWV:10000:100.00:20250810125049,2:F:buy:CRWV:10000:100.00:20250810125049 
    ~~~

## price drop to 80
    -send_udp_message("CRWV", "80","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    ~~~bash
    holding
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $-1,000,000.00
    🔴 Margin Call: $-800,000.00

    🗃 Holdings: (market value vs cost base) 
    💸 CRWV 20000s M$80.0 = $1,600,000.00 C$100.000, -20.00%

    📦 Long Holding Value: $1,600,000.00
    💼 Total Net Value:      $600,000.00         -40.00%
    ~~~

## price rise to 120
    -send_udp_message("CRWV", "120","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    ~~~bash
    holding
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $-1,000,000.00
    🟢 Buying Power: $800,000.00

    🗃 Holdings: (market value vs cost base) 
    💸 CRWV 20000s M$120.0 = $2,400,000.00 C$100.000, +20.00%

    📦 Long Holding Value: $2,400,000.00
    💼 Total Net Value:      $1,400,000.00         +40.00%
    ~~~

## sell 10000 share 
    ~~~bash
    order sell crwv 10000 110
    ~~~
    ~~~bash
    order taken. buying power 800000.00
    ~~~
    -send_udp_message("CRWV", "130","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    ~~~bash
    order filled sold CRWV 10000 shares at $130.00  0810132939-046ce6
    ~~~
    ~~~bash
    holding
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $300,000.00
    🟢 Buying Power: $2,500,000.00

    🗃 Holdings: (market value vs cost base) 
    💸 CRWV 10000s M$130.0 = $1,300,000.00 C$70.000, +85.71%

    📦 Long Holding Value: $1,300,000.00
    💼 Total Net Value:      $1,600,000.00         +60.00%
    ~~~    
    - raw setting
    ~~~bash
    PendingOrder=
    OrderId=3
    CashBalance=300000.0
    Holding=CRWV:10000:70.0
    TradesDone=1:F:buy:CRWV:10000:100.00:20250810125049,2:F:buy:CRWV:10000:100.00:20250810125049,3:F:sell:CRWV:10000:130.00:20250810132939 
    ~~~        

## sell last 10000 share 
    ~~~bash
    order sell crwv 10000 150
    ~~~
    ~~~bash
    order taken. buying power 2500000.00
    ~~~
    -send_udp_message("CRWV", "160","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    ~~~bash
    order filled sold CRWV 10000 shares at $160.00  0810133619-046ce6
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $1,900,000.00
    🟢 Buying Power: $3,800,000.00

    🗃 No holdings.

    💼 Total Net Value:      $1,900,000.00         +90.00%
    ~~~
    ~~~bash
    PendingOrder=
    OrderId=4
    CashBalance=1900000.0
    Holding=
    TradesDone=1:F:buy:CRWV:10000:100.00:20250810125049,2:F:buy:CRWV:10000:100.00:20250810125049,3:F:sell:CRWV:10000:130.00:20250810132939,4:F:sell:CRWV:10000:160.00:20250810133619
    ~~~

    
[Back to MainMenu](/docs/helpmain.md)