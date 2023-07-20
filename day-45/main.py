from bs4 import BeautifulSoup
# import lxml

with open("day-45\website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# You can also use `lxml` instead of `html.parser`
# soup = BeautifulSoup(contents, 'lxml')

# # prints the title
# print(soup.title)
# print(soup.title.string) #You can also use `print(soup.title.name)`
# #prints the tag
# print(soup.title.name)
# #Prints the whole html page
# print(soup.prettify())

all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.text)
#     print(tag.getText())
#     print(tag.get('href'))

# getting by 'id'
heading = soup.find(name='h1', id='name')
# print(f'Heading is {heading}\nHeading Text is {heading.get_text()}')

# getting by 'class'
section_heading = soup.find(name='h3', class_='heading')
'''Since the word `class` is reserved in python, we use `class_`'''
print(f'Heading is {section_heading}\nHeading Text is {section_heading.get_text()}')
print(section_heading.get('class'))

# getting exact tag
company_url = soup.select_one('p a')
url = company_url.get('href')
url_text = company_url.text
print(company_url, url_text, url)


