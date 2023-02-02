# import requests
import urllib.request
import bs4 as bs
# import time
# import numpy as np
import pandas as pd
# from urllib.request import urlopen



# fetch wiki page from beautifulSoup
url = 'https://en.wikipedia.org/wiki/Going_Seventeen_(web_series)'
source = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(source,'html.parser')

# get all the tables from the page
tables = soup.find_all('table', {'class':'wikitable'})

# get the values of title holder:
tables = tables[1:6]
# print(tables)

# for url in soup.find_all('table'):
#     print(url.get('href'))


# Now when you closely observe the above HTML code, you understand that the row tags are given with <tr> and the columns tags are with<td>. We retrieve all the rows and columns using the find_all() method. For example table.find_all(‘tr’) this collects all the rows from the table.

# We create a list named movie_list to store all the names.
# We iterate through the entire table from 2nd row to collect the names.

num_tables = 1
df = pd.DataFrame([])
df_list = []
df_headers = []

for table in tables:
    pd_to_tables = []
    
    table = table.find('tbody')
    
    if (num_tables == 1):
        for t in table.find_all('tr')[0]:
            df_headers.append(t.text)
        df_headers.append('Descriptions')
    
    # Descending adding rows to the table to combine occasional description
    # by delaying the addition until all the information included
    row = []
    for tr in table.find_all('tr')[1:]:
        ep_num = tr.contents[0].text
        
        # delay device, adding and resetting the row
        if (ep_num.isdigit()):            
            pd_to_tables.append(row)
            row = []
        
        for e in tr:
            if (len(row) >= 7):
                continue
            row.append(e.text)
    
    # adding the last row manually
    pd_to_tables.append(row)
    
    pd_to_tables = pd.DataFrame(pd_to_tables)
    pd_to_tables.columns = df_headers
    df = pd_to_tables.copy()
    
    if (num_tables == 1):
        df_list = df.copy()
    else:
        df_list = pd.concat([df_list, df])
    
    
    num_tables += 1

df_list.to_csv('tables.csv', encoding='utf-8', index=False)



