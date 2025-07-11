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

# 2. Kia 전기차 FAQ에 접근
    driver.get('https://kia.com/kr/vehicles/kia-ev/guide/faq#localnav')
    time.sleep(1)
    

# 3. FAQ에 담을 elements 선택해서 담기

    for num in range(7):
        button = driver.find_element(By.ID,f'accordion-item-{num}-button')
        button.click()

        question_tag = driver.find_element(By.ID, f'accordion-item-{num}-button')
        answer_elements = driver.find_element(By.ID, f'accordion-item-{num}-panel')
        question_element = question_tag.find_element(By.CSS_SELECTOR,'.cmp-accordion__title')
        
        answer_path = answer_elements.find_elements(By.CSS_SELECTOR,'.faqinner__wrap div p')
        answer=[]
        for x in answer_path:
            answer.append(x.text)
        answer_content="".join(x for x in answer)
    
        faq_data['브랜드'].append(0)
        faq_data['질문내용'].append(question_element.text)
        faq_data['답변내용'].append(answer_content)        

    driver.quit()


    return faq_data