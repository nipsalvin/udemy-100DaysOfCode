from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

# # Getting a the first article
# article_titles = soup.find(class_='titleline')
# article = article_titles.select_one('span a')
# article_text = article.get_text()
# article_link = article.get('href')
# article_upvote = soup.find(name='span', class_='score').text

# Getting all articles
articles = soup.find_all(name='span', class_='titleline')
article_text = []
article_link = []

for article in articles:
    text = article.get_text()
    article_text.append(text)
    link = article.select_one('span a').get('href')
    article_link.append(link)

article_upvote = [int(upvote.get_text().split()[0]) for upvote in soup.find_all(name='span', class_='score')]
# split item in a list at the space then select first item in the list


## Getting the index of the largest integer in the `article_upvote` list and getting the coresponding text and link
### method 1
# largest_number = max(article_upvote)
# largest_index = article_upvote.index(largest_number)

### method 2
largest_index = article_upvote.index(max(article_upvote))
print(article_text[largest_index])
print(article_link[largest_index])
print(article_upvote[largest_index])


# # print(article)
# print(article_text)
# print(article_link)
# print(article_upvote)
