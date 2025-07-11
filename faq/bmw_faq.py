from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def making_faq():

    # FAQ 정보를 딕셔너리 형태로 저장
    faq_data= {
        '브랜드':[],   # kia 0 번, 쉐보레 1번, bmw 2번 polestar 3번 
        '질문내용':[],
        '답변내용':[]
    }

# 1. Chrome browser 실행

    path = 'chromedriver.exe'
    service = webdriver.chrome.service.Service(path)
    driver=webdriver.Chrome(service=service)

# 2. BMW 전기차 FAQ에 접근
    driver.get('https://www.bmw.co.kr/ko/electric-cars.html#faq')
    time.sleep(2)

    id_index = ["accordion-3d01d7b3d2-item-9a95537360","accordion-3d01d7b3d2-item-590b3c6a9f","accordion-3d01d7b3d2-item-2a6a7f043a","accordion-3d01d7b3d2-item-2771f8490d","accordion-3d01d7b3d2-item-614a9a627e","accordion-3d01d7b3d2-item-fb57d26481","accordion-3d01d7b3d2-item-a9f132c4f6"]
    time.sleep(1)

    # id   
    # //*[@id="accordion-3d01d7b3d2-item-9a95537360"] 
    # //*[@id="accordion-3d01d7b3d2-item-590b3c6a9f"]
    # //*[@id="accordion-3d01d7b3d2-item-2a6a7f043a"]
    # //*[@id="accordion-3d01d7b3d2-item-2771f8490d"]
    # //*[@id="accordion-3d01d7b3d2-item-614a9a627e"]
    # //*[@id="accordion-3d01d7b3d2-item-fb57d26481"]
    # //*[@id="accordion-3d01d7b3d2-item-a9f132c4f6"]



    for id in id_index:

        bmw_contents_element = driver.find_element(By.ID,id)
        button = bmw_contents_element.find_element(By.CSS_SELECTOR,'.cmp-accordion__title')
        button.click()
        time.sleep(1)

        title_tag = bmw_contents_element.find_element(By.CSS_SELECTOR,'.cmp-accordion__title')
        answer_path = bmw_contents_element.find_element(By.CSS_SELECTOR,'.cmp-text__paragraph')

        current_scroll_position = driver.execute_script("return window.pageYOffset;")
        new_scroll_position = current_scroll_position + 290   # 290은 답변 상자 높이 평균
        driver.execute_script(f"window.scrollTo(0, {new_scroll_position});")
        time.sleep(1)
        
        faq_data['브랜드'].append(2)
        faq_data['질문내용'].append(title_tag.text)
        faq_data['답변내용'].append(answer_path.text)


    driver.quit()


    return faq_data
