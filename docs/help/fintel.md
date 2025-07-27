
# Fintel institutional transaction detail 
  * To fetch fintel institutional transaction detail  from https://fintel.io/so/us/ticker , filter out share count less than 1k

## Sample fetch steps to show condensed result
  * run fintel command 
    ~~~bash
    fintel rily
    ~~~
    - condensed result from new to old, only display top 50 lines , Type S=share, P=put, C=call
    ~~~bash
    FintelTutesTrans >1ksTop50L
    date,type,shares,investor
    250725,S,224282,FNDA-SchwabFundamentalUSSmallCompanyIndexETF
    250725,S,1088,Cwm
    250725,S,28373,WeAreOneSeven
    250725,S,82707,SCHA-SchwabUSSmall-CapETF
    250724,S,29430,FSKAX-FidelityTtlMktIdxFund
    250724,S,21153,FNCMX-FidelityNasdaqCompositeIdxFund
    250724,S,27609,FCFMX-FidelitySeriesTtlMktIdxFund
    250724,S,93796,FSMAX-FidelityExtMktIdxFund
    250723,S,1904,RMGWealthManagement
    250722,C,107300,IMC-Chicago
    250715,S,5416,PublicEmployeesRetirementSystemOfOhio
    25074,S,1500,RidgewoodInvestments
    ......................
    ~~~
  

[Back to MainMenu](/docs/helpmain.md)