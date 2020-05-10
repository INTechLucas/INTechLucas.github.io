from lxml import html
import requests
from bs4 import BeautifulSoup
import dryscrape
from unidecode import unidecode

sess = dryscrape.Session()
sess.visit('https://imgur.com/user/Lucamionette/posts')

base_page = sess.body()

base_html_soup = BeautifulSoup(base_page, 'html.parser')

galleries_index = ""

#find posts
posts = base_html_soup.find_all('a', class_ = 'Post-item')

#for each post found
for a in posts :
    link = a.get('href')

    #scrape the post
    response = requests.get('https://imgur.com/' + link)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    #find the title of post
    post_title = html_soup.find_all('h1', class_ = 'post-title')[0].get_text()
    print(post_title)

    #print all the image links
    post_containers = html_soup.find_all('div', class_ = 'post-image-container')
    print("[" + str(len(post_containers)) + "]")
    for div in post_containers :
        print("- https://i.imgur.com/" + div.get('id') + ".jpg")

    galleries_index += "\n- title: " + post_title + "\n" + \
                        "  cover: https://i.imgur.com/" + post_containers[0].get('id') + ".jpg\n" + \
                        "  url: photos/" + unidecode(post_title).lower().replace(' ', '_').replace('-', '_')

print(galleries_index)