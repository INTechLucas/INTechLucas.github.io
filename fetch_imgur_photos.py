from lxml import html
import requests
from bs4 import BeautifulSoup
import dryscrape

sess = dryscrape.Session()
sess.visit('https://imgur.com/user/Lucamionette/posts')

base_page = sess.body()

base_html_soup = BeautifulSoup(base_page, 'html.parser')

posts = base_html_soup.find_all('a', class_ = 'Post-item')

for a in posts :
    print(a.get('href'))


#scrape the post
response = requests.get('https://imgur.com/a/1G6n0QV')
html_soup = BeautifulSoup(response.text, 'html.parser')

#find the title of post
post_title = html_soup.find_all('h1', class_ = 'post-title')[0].get_text()
print(post_title)

#print all the image links
post_containers = html_soup.find_all('div', class_ = 'post-image-container')
for div in post_containers :
    print("- https://i.imgur.com/" + div.get('id') + ".jpg")