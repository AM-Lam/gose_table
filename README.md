# Going Seventeen ep Table
## Displaying all the Going Seventeen episode on one table(Credit to Wiki and whoever upload the info!)
Generate a list of going seventeen episodes from 2019 to the current day(as long as they are updated in the wiki page), with the information of year and number of episodes. 

## How to make 
Fetch the data tables from wikipedia page [here](https://en.wikipedia.org/wiki/Going_Seventeen_(web_series)#Episodes). 
Proceed and combine the provided tables from different years(2020, 2021, 2022) by using the pandas library.
Edit the row of information in dataframe, including combining description to the corresponding episode.
Output the result table to a csv file. 
The result database can be modified for further research.


## development 
1. run `python3 gose_wiki.py`
2. produce a csv file, called tables.csv, with the updated information. 

## Library
Beautiful Soup: for web scraping tables in wiki page
Pandas: Proceeding the HTML information to dataframe, which allows further data analysis or manipulation

It is meant for integrated with notions or my own web pages. 
