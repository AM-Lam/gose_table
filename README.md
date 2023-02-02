# Going Seventeen episode list based on wiki
Generate a list of going seventeen episodes from 2019 to the current day(as long as they are updated in the wiki page), with the information of year and number of episodes. 

## How to make 
Fetch the data tables from wikipedia page [here](https://en.wikipedia.org/wiki/Going_Seventeen_(web_series)#Episodes). 
Combine the provided tables from different years(2020, 2021, 2022) by using the library pandas or sql(TODO: hasn't decided yet).
Modify the result database for my research uses and output it to a csv file. 


## development 
The project will produce a csv file, called tables.csv, with the updated information. 
1. run `python3 gose_wiki.py` and pray that it will work

It is meant for integrated with notions or my own web pages. 
