from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding='utf-8') as file:
    website_content = file.read()
    #print(website_content)

soup = BeautifulSoup(website_content, "html.parser")

#print(soup.contents)


#print(soup.findAll(name = "p"))

all_p_tags = soup.findAll(name="p")
# getting the string content inside the tag
for tag in all_p_tags:
    print(tag.getText())


all_anchor_tags = soup.findAll(name="a")
# getting all links of the anchor tag
for tag in all_anchor_tags:
    print(tag.get("href"))

# finding a specific name and id
heading = soup.find(name="h1", id="name")
print(heading)

# finding by name and class
section_heading = soup.find(name="h3", class_="heading").getText()
print(section_heading)

# getting the first item matching, can be used as the same CSS selector
company_url = soup.select_one(selector="p a")
print(company_url)