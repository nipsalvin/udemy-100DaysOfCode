from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

article_titles = soup.find(class_='titleline')
# print(article_titles)
a_tag = article_titles.select_one('a', class_='titleline')
# print(a_tag)

article = article_titles.select_one('span a')
article_text = article.get_text()
article_link = article_titles.get('href')
article_upvote = soup.find(name='span', class_='score').text
# print(atricle_text)

# print(f'Article Text:{article_text}\nArticle Link:{article_link}\nArticle Upvote:{article_upvote}')
print(article)
print(article_text)
print(article_link)
print(article_upvote)
