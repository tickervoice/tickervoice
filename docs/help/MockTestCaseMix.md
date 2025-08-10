
# Mock Trading Test Cases margin rate 50%
[Back to MainMenu](/docs/helpmain.md)

## Calculation of buying power 
   buying_power = (total_long_value + cash_balance - total_short_value ) * (1/MARGIN_RATE) - total_long_cost-total_short_cost - order_locked_amount(buy and short order)
## Initial 
    * reset balance , view holding, pending order
    ~~~bash
    holding
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $1,200,000.00
    🟢 Buying Power: $2,400,000.00

    🗃 No holdings.

    💼 Total Net Value:      $1,200,000.00         +20.00%
    ~~~
    ~~~bash
    pending order
    ~~~
    ~~~bash
    💰 Cash Balance: $1,200,000

    📋 No pending orders.
    ~~~
    ~~~bash
    insert aapl,tsla,nvda,amzn
    ['AAPL', 'TSLA', 'NVDA', 'AMZN'] added
    ~~~

    ~~~bash
    order buy aapl 3000s 150
    order taken. buying power 1950000.00
    order buy tsla 2000s 300
    order taken. buying power 1350000.00
    order short nvda 1500s 400
    order taken. buying power 750000.00
    order short amzn 1000s 140
    order taken. buying power 610000.00
    ~~~
    
    ~~~bash
    holding
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $1,200,000.00
    🔒 Order locked balance: $1,790,000.00
    🟢 Buying Power: $610,000.00

    🗃 No holdings.

    💼 Total Net Value:      $1,200,000.00         +20.00%
    ~~~
    ~~~bash
    pending order
    ~~~
    ~~~bash
    💰 Cash Balance: $1,200,000

    📋 Pending Orders:
    🛒[1,A]buy AAPL 3000@$150=$450,000 e250811 0738
    🛒[2,A]buy TSLA 2000@$300=$600,000 e250811 0738
    🔻[3,A]short NVDA -1500@$400=$-600,000 e250811 0738
    🔻[4,A]short AMZN -1000@$140=$-140,000 e250811 0739

    🧾 Total Funds locked:  $1,790,000
    🟢 Buying Power: $610,000
    ~~~
    
    -send_udp_message("AAPL", "150","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    -send_udp_message("TSLA", "300","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    -send_udp_message("NVDA", "400","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    -send_udp_message("AMZN", "140","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00") 
    
    ~~~bash
    order filled bought AAPL 3000 shares at $150.00  0810154231-046ce6
    order filled bought TSLA 2000 shares at $300.00  0810154232-046ce6
    order filled shorted NVDA -1500 shares at $400.00  0810154232-046ce6
    order filled shorted AMZN -1000 shares at $140.00  0810154237-046ce6	
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $890,000.00
    🔒 Short Pos locked balance: $805,000.00
    🟢 Buying Power: $610,000.00

    🗃 Holdings: (market value vs cost base) 
    💸 AAPL 3000s M$150.0 = $450,000.00 C$150.000, 0.00%
    💸 TSLA 2000s M$300.0 = $600,000.00 C$300.000, 0.00%
    💸 NVDA -1500s M$400.0 = $-600,000.00 C$400.000, 0.00%
    💸 AMZN -1000s M$140.0 = $-140,000.00 C$140.000, 0.00%

    📦 Total Holdings Value: $310,000.00
        📦 Long Holding Value: $1,050,000.00
        📦 Short Holding Value: $-740,000.00
    💼 Total Net Value:      $1,200,000.00         +20.00%
    ~~~
    
    
    ~~~bash
    pending order
    ~~~
    ~~~bash
    💰 Cash Balance: $890,000

    📋 No pending orders.
    ~~~
    
    ~~~bash
    trades done
    📊 Trade History:
    1,F) buy AAPL 3000@$150.00 on 2025-08-10 15:42:31
    2,F) buy TSLA 2000@$300.00 on 2025-08-10 15:42:32
    3,F) short NVDA -1500@$400.00 on 2025-08-10 15:42:32
    4,F) short AMZN -1000@$140.00 on 2025-08-10 15:42:37
    ~~~
    - raw setting
    ~~~bash
    PendingOrder=
    OrderId=4
    CashBalance=890000.0
    Holding=AAPL:3000:150.0,TSLA:2000:300.0,NVDA:-1500:400.0,AMZN:-1000:140.0
    TradesDone=1:F:buy:AAPL:3000:150.00:20250810154231,2:F:buy:TSLA:2000:300.00:20250810154232,3:F:short:NVDA:-1500:400.00:20250810154232,4:F:short:AMZN:-1000:140.00:20250810154237
    ~~~
    
    -send_udp_message("AAPL", "180","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    -send_udp_message("TSLA", "250","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    -send_udp_message("NVDA", "450","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    -send_udp_message("AMZN", "130","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00") 
    
    ~~~bash
    holding
    💰 Cash Balance(short inc): $890,000.00
    🔒 Short Pos locked balance: $805,000.00
    🟢 Buying Power: $460,000.00

    🗃 Holdings: (market value vs cost base) 
    💸 AAPL 3000s M$180.0 = $540,000.00 C$150.000, +20.00%
    💸 TSLA 2000s M$250.0 = $500,000.00 C$300.000, -16.67%
    💸 NVDA -1500s M$450.0 = $-675,000.00 C$400.000, -12.50%
    💸 AMZN -1000s M$130.0 = $-130,000.00 C$140.000, +7.14%

    📦 Total Holdings Value: $235,000.00
        📦 Long Holding Value: $1,040,000.00
        📦 Short Holding Value: $-805,000.00
    💼 Total Net Value:      $1,125,000.00         +12.50%
    ~~~
    ~~~bash
    💰 Cash Balance: $890,000

    📋 No pending orders.
    ~~~
    ~~~bash
    order cover nvda 500s 470
    order taken. buying power 460000.00
    ~~~
    ~~~bash
    💰 Cash Balance(short inc): $890,000.00
    🔒 Short Pos locked balance: $805,000.00
    🟢 Buying Power: $460,000.00

    🗃 Holdings: (market value vs cost base) 
    💸 AAPL 3000s M$180.0 = $540,000.00 C$150.000, +20.00%
    💸 TSLA 2000s M$250.0 = $500,000.00 C$300.000, -16.67%
    💸 NVDA -1500s M$450.0 = $-675,000.00 C$400.000, -12.50%
    💸 AMZN -1000s M$130.0 = $-130,000.00 C$140.000, +7.14%

    📦 Total Holdings Value: $235,000.00
        📦 Long Holding Value: $1,040,000.00
        📦 Short Holding Value: $-805,000.00
    💼 Total Net Value:      $1,125,000.00         +12.50%
    
    
    pending order
    
    💰 Cash Balance: $890,000

    📋 Pending Orders:
    🛒[5,A]cover NVDA -500@$470=$-235,000 e250811 0757

    🧾 Total Funds locked:  $740,000
    🟢 Buying Power: $460,000
    
    ~~~
    
    ~~~bash
    send_udp_message("NVDA", "450","5m", "RC01xxxx,current=444,lastdayclose=521,testmsg","2025-06-03 03:49:42-04:00")  
    
    order filled covered NVDA -500 shares at $450.00  0810161100-046ce6
    
    💰 Cash Balance(short inc): $665,000.00
    🔒 Short Pos locked balance: $580,000.00
    🟢 Buying Power: $685,000.00

    🗃 Holdings: (market value vs cost base) 
    💸 AAPL 3000s M$180.0 = $540,000.00 C$150.000, +20.00%
    💸 TSLA 2000s M$250.0 = $500,000.00 C$300.000, -16.67%
    💸 NVDA -1000s M$450.0 = $-450,000.00 C$375.000, -20.00%
    💸 AMZN -1000s M$130.0 = $-130,000.00 C$140.000, +7.14%

    📦 Total Holdings Value: $460,000.00
        📦 Long Holding Value: $1,040,000.00
        📦 Short Holding Value: $-580,000.00
    💼 Total Net Value:      $1,125,000.00         +12.50%
    ~~~
    
    
[Back to MainMenu](/docs/helpmain.md)