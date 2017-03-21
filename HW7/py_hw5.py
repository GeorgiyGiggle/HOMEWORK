from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import os
from datetime import datetime

chromedriver = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver")
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("https://toster.ru")

def get_info():
    questions = driver.find_elements_by_class_name("question_short")
    for ques in questions:
        title_element = ques.find_element_by_class_name("question__title-link")
        title = title_element.text

        url = title_element.get_attribute("href")

        subscribers = ques.find_element_by_class_name("question__views-count").text.split()[0]

        published_string = ques.find_element_by_class_name("question__date_publish").get_attribute("datetime")
        published_datetime = datetime.strptime(published_string, "%Y-%m-%d %H:%M:%S")
        published = published_datetime.strftime("%d-%m-%Y")

        answers = ques.find_element_by_class_name("mini-counter__count_grey").text

        try:
            ques.find_element_by_class_name("icon_check")
            has_correct_answer = True
        except NoSuchElementException:
            has_correct_answer = False

        data = {
            "title": title,
            "url": url,
            "subscribers": subscribers,
            "published": published,
            "answers": answers,
            "has_correct_answer": has_correct_answer
        }
        print(data)

driver.set_window_size(414, 736)

# driver.quit()