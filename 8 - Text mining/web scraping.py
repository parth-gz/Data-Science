# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 08:59:06 2024

@author: ADMIN
"""

from bs4 import BeautifulSoup as bs
soup=BeautifulSoup(open("C:/Users/ADMIN/8-Text Mining/Text Mining/sample_doc.html"),"html.parser")
#It is going to show all all the html contents extracted
soup.text
#it will show only text
soup.contents
#it is going to show all the html text extracted
soup.find('address')
soup.find_all('address')
soup.find_all('q')
soup.find_all('b')
table=soup.find('table')
table
for row in table.find_all('tr'):
    columns=row.find_all('td')
    print(columns)

#it will show all the rows wxcept first row
#Now we want to display M.tech which is located 
#in the third row
#I need to give [3][2]
    table.find_all('tr')[3].find_all('td')[2]




import requests
link="https://sanjivanicoe.org.in/index.php/contact"
page=requests.get(link)
page
#<Response [200]> means  that the connection is successfully established
page.content
#you will get html sours=ce code but very crowdy text
#let us apply html parser
soup=bs(page.content,'html.parser')
soup
#now the text is clean but not uptio the exceptation
#now lwt us apply pretiffy method
print(soup.prettify())
#the text is neat and clean
list(soup.children)
#finding all contents using tab
soup.find_all('p')
#supppose you want to extract content from first row