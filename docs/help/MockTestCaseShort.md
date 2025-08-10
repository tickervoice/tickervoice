
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

##  order short full amount 
    ~~~bash
    order  short crwv 10000 100
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
    🔻[1,A]short CRWV -10000@$100=$-1,000,000 e250811 0545

    🧾 Total Funds locked:  $1,000,000
    🟢 Buying Power: $1,000,000
    ~~~
    
## double order to run out of margin
    ~~~bash
    order  short crwv 10000 100
    ~~~
    ~~~bash
    order taken. buying power 0.00
    ~~~
    ~~~bash
    holding
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $1,000,000.00
    🔒 Order locked balance: $2,000,000.00
    🟢 Buying Power: $0.00

    🗃 No holdings.

    💼 Total Net Value:      $1,000,000.00         0.00%
    ~~~
    ~~~bash
    pending order
    ~~~
    ~~~bash
    💰 Cash Balance: $1,000,000

    📋 Pending Orders:
    🔻[1,A]short CRWV -10000@$100=$-1,000,000 e250811 0545
    🔻[2,A]short CRWV -10000@$100=$-1,000,000 e250811 0546

    🧾 Total Funds locked:  $2,000,000
    🟢 Buying Power: $0
    ~~~
    - raw setting
    ~~~bash
    PendingOrder=1:A:short:CRWV:-10000:100.0:100.0:1754891130,2:A:short:CRWV:-10000:100.0:100.0:1754891203
    OrderId=2
    CashBalance=1000000
    Holding=
    TradesDone=
    ~~~
    
## 2 buy orders processed
    -send_udp_message("CRWV", "100","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    ~~~bash
    order filled shorted CRWV -10000 shares at $100.00,shorted CRWV -10000 shares at $100.00  0810134938-046ce6
    ~~~   
    ~~~bash
    holding
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $3,000,000.00
    🔒 Short Pos locked balance: $2,000,000.00
    🟢 Buying Power: $0.00

    🗃 Holdings: (market value vs cost base) 
    💸 CRWV -20000s M$100.0 = $-2,000,000.00 C$100.000, 0.00%

    📦 Short Holding Value: $-2,000,000.00
    💼 Total Net Value:      $1,000,000.00         0.00%
    ~~~bash
    pending order
    ~~~
    ~~~bash
    💰 Cash Balance: $3,000,000

    📋 No pending orders.
    ~~~
    - raw setting
    ~~~bash
    PendingOrder=
    OrderId=2
    CashBalance=3000000.0
    Holding=CRWV:-20000:100.0
    TradesDone=1:F:short:CRWV:-10000:100.00:20250810134937,2:F:short:CRWV:-10000:100.00:20250810134937
    ~~~
    

## price drop to 80
    -send_udp_message("CRWV", "80","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    ~~~bash
    holding
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $3,000,000.00
    🔒 Short Pos locked balance: $1,600,000.00
    🟢 Buying Power: $800,000.00

    🗃 Holdings: (market value vs cost base) 
    💸 CRWV -20000s M$80.0 = $-1,600,000.00 C$100.000, +20.00%

    📦 Short Holding Value: $-1,600,000.00
    💼 Total Net Value:      $1,400,000.00         +40.00%
    ~~~

## price rise to 120
    -send_udp_message("CRWV", "120","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    ~~~bash
    holding
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $3,000,000.00
    🔒 Short Pos locked balance: $2,400,000.00
    🔴 Margin Call: $-800,000.00

    🗃 Holdings: (market value vs cost base) 
    💸 CRWV -20000s M$120.0 = $-2,400,000.00 C$100.000, -20.00%

    📦 Short Holding Value: $-2,400,000.00
    💼 Total Net Value:      $600,000.00         -40.00%
    ~~~

## cover 10000 share 
    ~~~bash
    order cover crwv 10000 110
    ~~~
    ~~~bash
    adjusted buying power -900000.00 negative but adjusted_total_net_value still positive 500000.0
    order taken. buying power -800000.00
    holding
    💰 Cash Balance(short inc): $3,000,000.00
    🔒 Short Pos locked balance: $2,400,000.00
    🔴 Margin Call: $-800,000.00

    🗃 Holdings: (market value vs cost base) 
    💸 CRWV -20000s M$120.0 = $-2,400,000.00 C$100.000, -20.00%

    📦 Short Holding Value: $-2,400,000.00
    💼 Total Net Value:      $600,000.00         -40.00%
    ~~~
    
    -send_udp_message("CRWV", "110","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    ~~~bash
    order filled sold CRWV 10000 shares at $130.00  0810132939-046ce6
    ~~~
    ~~~bash
    holding
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $1,900,000.00
    🔒 Short Pos locked balance: $1,100,000.00
    🟢 Buying Power: $700,000.00

    🗃 Holdings: (market value vs cost base) 
    💸 CRWV -10000s M$110.0 = $-1,100,000.00 C$90.000, -22.22%

    📦 Short Holding Value: $-1,100,000.00
    💼 Total Net Value:      $800,000.00         -20.00%
    ~~~    
    - raw setting
    ~~~bash
    PendingOrder=
    OrderId=3
    CashBalance=1900000.0
    Holding=CRWV:-10000:90.0
    TradesDone=1:F:short:CRWV:-10000:100.00:20250810134937,2:F:short:CRWV:-10000:100.00:20250810134937,3:F:cover:CRWV:-10000:110.00:20250810150446
    ~~~        

## sell last 10000 share 
    ~~~bash
    order cover crwv 10000 110
    ~~~
    ~~~bash
    order taken. buying power 700000.00
    ~~~
    -send_udp_message("CRWV", "100","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    ~~~bash
    order filled covered CRWV -10000 shares at $100.00  0810150842-046ce6
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $900,000.00
    🟢 Buying Power: $1,800,000.00

    🗃 No holdings.

    💼 Total Net Value:      $900,000.00         -10.00%
    ~~~
    ~~~bash
    PendingOrder=
    OrderId=4
    CashBalance=900000.0
    Holding=
    TradesDone=1:F:short:CRWV:-10000:100.00:20250810134937,2:F:short:CRWV:-10000:100.00:20250810134937,3:F:cover:CRWV:-10000:110.00:20250810150446,4:F:cover:CRWV:-10000:100.00:20250810150842
    ~~~

[Back to MainMenu](/docs/helpmain.md)