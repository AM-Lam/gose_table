# Going Seventeen Episode Table
## Displaying all the Going Seventeen episodes on one table(Credit to Wiki)
Combine and generate a combination of going seventeen episodes from multiple tables dated from 2019 to the current(as long as they are updated on the wiki page), with the information of year and number of episodes. 
- Fetch data from Wiki
- Data cleaning
- Merge multiple datasets

## How to make 
Fetch the data tables from Wikipedia page [here](https://en.wikipedia.org/wiki/Going_Seventeen_(web_series)#Episodes). 
Proceed and combine the provided tables from different years(2020, 2021, 2022) by using the Pandas library.
Edit the row of information in dataframe, including combining the description with the corresponding episode.
Output the result table to a CSV file. 
The resulting database can be modified for further research.


## development 
1. run `python3 gose_wiki.py`
2. produce a CSV file, called tables.csv, with the updated information. 

## Library
Beautiful Soup: for web scraping tables in the wiki page
Pandas: Proceeding the HTML information to dataframe, which allows further data analysis or manipulation
