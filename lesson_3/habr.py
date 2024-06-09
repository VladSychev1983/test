import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

def get_headers():
    return Headers(browser="chrome",os="win").generate()

main_response = requests.get(url="https://habr.com/ru/articles/", headers=get_headers())

parsed_data = []
main_html = main_response.text

main_soup = BeautifulSoup(main_html, features="lxml")

tag_articles = main_soup.find(name="div",class_="tm-articles-list")

articles = tag_articles.find_all('article')

for article in articles:
    tag_time = article.find("time")
    pub_time = tag_time["datetime"]

    h2_tag = article.find("h2")
    a_tag = h2_tag.find("a")
    
    link = a_tag["href"]
    link = f'https://habr.com{link}'
    title = a_tag.text

    article_response = requests.get(link, headers=get_headers())
    article_soup = BeautifulSoup(article_response.text, features='lxml')
    article_body_tag = article_soup.find(name='div', id="post-content-body")

    article_text = article_body_tag.text[:100]

    parsed_data.append({
        "pub_time":  pub_time,
        "link": link,
        "title": title,
        "text" : article_text         
    })

print(parsed_data)
print(len(parsed_data))