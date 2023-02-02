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
# # add to pd
# # print(table_title)
# # print(pd_to_tables[1][1])
# # print(df)
# # result = pd.concat(df_list)
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print (df_list)
# # print(df_list)
# # df_list.head(3)

# # Finally, we’re able to solve this by collecting the title attribute and get the required output.

# # We collected all the rows except the 1st row from the req_table using find_all(‘tr’)[1:].
# # Then collected all the column data for each row using tr.find_all(‘td’).
# # The movie title is ialln the anchor tag with the name ‘title’. As there is only one title for each <a> we using find() method to grab the title and append it to the list.
# mylist = []
# for tr in tables.find_al numpy as np
# import pandas as pdl('tr')[1:]:
#     tds = tr.find_all('td')
#     name = tds[1].contents# Get the attribute of all the tables from the first tables
    # for tr_t in tr:
    #     table_title.append(tr_t.text)
#     ##print(tds) 
#     ##print(name)
#     ##print("---")
#     a = name.find('a') 
#     mylist.append(a.get('title'))
# print(my_list)


