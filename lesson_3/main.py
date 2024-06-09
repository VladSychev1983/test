import requests
import re
from bs4 import BeautifulSoup
from fake_headers import Headers

keywords = ['дизайн', 'фото', 'web', 'python','фобию','разработчики']

def get_headers():
    return Headers(browser="chrome",os="win").generate()

def check_news(news_list):
    result = {}
    counter = 0
    found_counter =0
    for idx,dicts in enumerate(news_list):
        for word in dicts["title"].split(" "):
            word = str(word).replace(",","")
            word = str(word).replace(".","")
            word = str(word).strip()
            counter += 1
            print(f'Проверяю {word} в title')
            if word in keywords:
                found_counter += 1
                result[dicts["title"]] = {"pub_time": dicts["pub_time"], 
                                          "link" : dicts["link"], "word": word}            
        for word in dicts["text"].split(" "):
            word = str(word).replace(",","")
            word = str(word).replace(".","")
            word = str(word).strip()
            print(f'Проверяю {word} в text')
            counter += 1
            if word in keywords:
                result[dicts["title"]] = {"pub_time": dicts["pub_time"],
                                          "link" : dicts["link"], "word": word}
                found_counter += 1

    print(f'Checked words: {counter}')
    print(f'Found words: {found_counter}')             
    
    for key,value in result.items():
        pattern = r"^(\d+-\d+-\d{2})(T.*$)"
        mytime = re.sub(pattern, r'\1', str(value["pub_time"]))
        print(f"{mytime} - {key} - {value["link"]}")


main_response = requests.get(url="https://habr.com/ru/all/", headers=get_headers())
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

    div_tag = article.find(name="div", class_="tm-article-body")
    div_tag2 = div_tag.find(name="div", class_="article-formatted-body")
    p_tag = div_tag2.find_all("p")
    article_text = ""
    
    for idx, item in enumerate(p_tag):
        item = str(item).replace("<p>","")
        item = str(item).replace("</p>","")
        article_text += "".join(item)
    
    parsed_data.append({
        "pub_time" : pub_time,
        "link" : link,
        "title" : title,
        "text" : article_text
    })
if __name__ == '__main__':
    check_news(parsed_data)