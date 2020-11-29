"""

If you want to scrape a website you can :-

1. Use the API

2. HTML Web Scraoing using a tool like BS4


There are 3 basic steps we need to know to scrape data from the web :-

1. Get the HTML

2. Parse the HTML 

3. HTML Tree Traveral

Step 0 for Web Scraping install all the requirements:-

1. pip install requests

2. pip install html5 

3. pip install bs4

"""

import requests

from bs4 import BeautifulSoup

url = "https://codewithharry.com"


# Step 1 : Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2 : Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)
# print(soup.prettify)

# Step3 : HTML Tree Traversal
title = soup.title
print(title)
print(title.string)

'''
Commonly used types of Objects:-
1. Tag:-
# print(type(title))

2. NavigableString:-
# print(type(title.string))

3. BeautifulSoup:-
# print(type(soup))

4. Comment:-
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p)
print(soup2.p.string)
print(type(soup2.p.string)) this is a comment object
exit()
'''

# Get all the paragraphs from the page
paragraphs = soup.find_all('p') 
# paragraphs contains a list of all the p tags in the Web Page
print("\n", paragraphs)

# Get all anchor tags from the page
anchor = soup.find_all('a')
# anchor contains a list of all the a tags in the Web Page
print("\n", anchor)

print("\n", soup.find('p'))
# This returns the 'first' paragraph  of the page that soup object finds

print("\n", soup.find('p')['class'])
# This returns the class of 'first' paragraph  of the page that soup object finds

# print("\n", soup.find('p')['id']) this line returns an error as the given tag has no id
# This returns the id of 'first' paragraph  of the page that soup object finds

# Find all the elements which have the class name "lead"
print("\n", soup.find_all('p', class_="lead"))

# Get the Text form the tags/soup
print("\n", soup.find('p').get_text())
# print("\n", soup.get_text())

# Get all the links on the page
a = soup.find_all('a')
all_links = set()
for link in a:
    if link.get('href') != '#':
        all_links.add("https://codewithharry.com" + link.get('href'))

print("\n", all_links)

# Getting Element with a specified id
navbarSupportedContent = soup.find(id='navbarSupportedContent')
print("\n", navbarSupportedContent)
# print("\n", navbarSupportedContent.contents) this prints the list of elements found

print("\nContent")
for elem in navbarSupportedContent.contents:
    print(elem)

print("\nChildren")
for elem in navbarSupportedContent.children:
    print(elem)

# As we can see from the output, .children and .cintent print the same thing.Then what is the difference between both?
# .children - A tag's children are available as a list 
# .content - A tag's children are available a generator

print("\nStrings")
for item in navbarSupportedContent.strings:
    print(item)

print("\nStrippedStrings")
for item in navbarSupportedContent.stripped_strings:
    print(item)