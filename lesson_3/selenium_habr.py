from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from webdriver_manager.chrome import ChromeDriverManager

import os;path = os.getenv('PATH'); print(path);

browser = webdriver.Chrome()


browser.get("https://habr.com/ru/articles/")


def wait_element(browser, delay_seconds=1, by=By.CLASS_NAME, value=None):
    return WebDriverWait(browser,delay_seconds).until(expected_conditions.presence_of_all_elements_located(by, value))


article_list_tag = browser.find_element(By.CLASS_NAME,  value="tm-articles-list")
article_tags = article_list_tag.find_elements(By.TAG_NAME, value="article")

parsed_data =[]
for article in article_tags:
    h2_tag = wait_element(article, by=By.TAG_NAME, value="h2")
    time_tag = wait_element(article, by=By.TAG_NAME, value="time")
    a_tag = wait_element(h2_tag, by=By.TAG_NAME, value="a")
    title = a_tag.text
    pub_time = time_tag.get_attribute("datetime")
    link = a_tag.get_attribute("href")

    parsed_data.append({
        "title" : title,
        "pub_time": pub_time,
        "link" : link,
        "text" : ""
    })

for parsed_article in parsed_data:
    browser.get(parsed_article["link"])
    article_tag = wait_element(browser, by=By.ID, value="post-content-body")
    article_text = article_tag.text
    parsed_data["text"] = article_text[:100]

browser.quit()