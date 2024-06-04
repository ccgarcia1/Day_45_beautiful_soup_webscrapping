from bs4 import BeautifulSoup
#import lxml

with open("website.html", encoding='utf-8') as file:
    website_content = file.read()
    print(website_content)

soup = BeautifulSoup(website_content , "html.parser")

print(soup.contents)

