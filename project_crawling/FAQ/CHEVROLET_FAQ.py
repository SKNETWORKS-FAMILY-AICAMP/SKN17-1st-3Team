from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


# ---------------- Chevrolet FAQ 크롤링 ----------------
def making_faq():
    faq_data= {
        '브랜드':[],   # kia 0 번, 쉐보레 1번, bmw 2번 polestar 3번 
        '질문내용':[],
        '답변내용':[]
    }

    # 새 드라이버 인스턴스 생성
    path = 'chromedriver.exe'
    service = Service(path)
    driver = webdriver.Chrome(service=service)

    # 1. 쉐보레 FAQ 페이지 접속
    driver.get('https://www.chevrolet.co.kr/faq')
    time.sleep(1)

    # 2. 반복 크롤링 (질문 → + 버튼 클릭 → 답변)  ─ 스크롤 없음
    # (1) 첫 번째 FAQ 질문 요소 선택
    question_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[1]/div/div[1]/h6')
    question_text = question_elem.text.strip()

    # (2) 질문 요소 클릭하여 답변 영역 펼치기
    question_elem.click()
    time.sleep(0.3)

    # (3) 답변 추출 : 질문 요소 부모의 다음 형제 div에서 찾기
    answer_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[1]/div/div[2]/gb-content-well/adv-grid/adv-col')
    answer_text = answer_elem.text.strip()

    faq_data['브랜드'].append(1)
    faq_data['질문내용'].append(question_text)
    faq_data['답변내용'].append(answer_text)



    # (1) 첫 번째 FAQ 질문 요소 선택
    question_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[2]/div/div[1]/h6')
    question_text = question_elem.text.strip()

    # (2) 질문 요소 클릭하여 답변 영역 펼치기
    question_elem.click()
    time.sleep(0.3)

# (3) 답변 추출 : 질문 요소 부모의 다음 형제 div에서 찾기
    answer_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[2]/div/div[2]/gb-content-well/adv-grid/adv-col/div/div/div/p')
    answer_text = answer_elem.text.strip()
    faq_data['브랜드'].append(1)
    faq_data['질문내용'].append(question_text)
    faq_data['답변내용'].append(answer_text)


    # (1) 첫 번째 FAQ 질문 요소 선택
    question_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[3]/div/div[1]/h6')
    question_text = question_elem.text.strip()

    # (2) 질문 요소 클릭하여 답변 영역 펼치기
    question_elem.click()
    time.sleep(0.3)

    # (3) 답변 추출 : 질문 요소 부모의 다음 형제 div에서 찾기
    answer_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[3]/div/div[2]/gb-content-well/adv-grid/adv-col/div/div/div/p')
    answer_text = answer_elem.text.strip()

    faq_data['브랜드'].append(1)
    faq_data['질문내용'].append(question_text)
    faq_data['답변내용'].append(answer_text)



    #   (1) 첫 번째 FAQ 질문 요소 선택
    question_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[4]/div/div[1]/h6')
    question_text = question_elem.text.strip()

    # (2) 질문 요소 클릭하여 답변 영역 펼치기
    question_elem.click()
    time.sleep(0.3)

    # (3) 답변 추출 : 질문 요소 부모의 다음 형제 div에서 찾기
    answer_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[4]/div/div[2]/gb-content-well/adv-grid/adv-col/div/div/div/p')
    answer_text = answer_elem.text.strip()
    faq_data['브랜드'].append(1)
    faq_data['질문내용'].append(question_text)
    faq_data['답변내용'].append(answer_text)



    # (1) 첫 번째 FAQ 질문 요소 선택
    question_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[5]/div/div[1]/h6')
    question_text = question_elem.text.strip()

    # (2) 질문 요소 클릭하여 답변 영역 펼치기
    question_elem.click()
    time.sleep(0.3)

    # (3) 답변 추출 : 질문 요소 부모의 다음 형제 div에서 찾기
    answer_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[5]/div/div[2]/gb-content-well/adv-grid/adv-col/div/div/div/p[1]')
    answer_text = answer_elem.text.strip()
    faq_data['브랜드'].append(1)
    faq_data['질문내용'].append(question_text)
    faq_data['답변내용'].append(answer_text)


    # (1) 첫 번째 FAQ 질문 요소 선택
    question_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[6]/div/div[1]/h6')
    question_text = question_elem.text.strip()


    # (2) 질문 요소 클릭하여 답변 영역 펼치기
    question_elem.click()
    time.sleep(0.3)

    # (3) 답변 추출 : 질문 요소 부모의 다음 형제 div에서 찾기
    answer_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[6]/div/div[2]/gb-content-well/adv-grid/adv-col')
    answer_text = answer_elem.text.strip()
    faq_data['브랜드'].append(1)
    faq_data['질문내용'].append(question_text)
    faq_data['답변내용'].append(answer_text)


    # (1) 첫 번째 FAQ 질문 요소 선택
    question_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[7]/div/div[1]/h6')
    question_text = question_elem.text.strip()

    # (2) 질문 요소 클릭하여 답변 영역 펼치기
    question_elem.click()
    time.sleep(0.3)

    # (3) 답변 추출 : 질문 요소 부모의 다음 형제 div에서 찾기
    answer_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[7]/div/div[2]/gb-content-well/adv-grid/adv-col/div/div/div/p')
    answer_text = answer_elem.text.strip()
    faq_data['브랜드'].append(1)
    faq_data['질문내용'].append(question_text)
    faq_data['답변내용'].append(answer_text)


    # (1) 첫 번째 FAQ 질문 요소 선택
    question_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[8]/div/div[1]/h6')
    question_text = question_elem.text.strip()
    

    # (2) 질문 요소 클릭하여 답변 영역 펼치기
    question_elem.click()
    time.sleep(0.3)

    # (3) 답변 추출 : 질문 요소 부모의 다음 형제 div에서 찾기
    answer_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[8]/div/div[2]/gb-content-well/adv-grid/adv-col/div/div/div/p')
    answer_text = answer_elem.text.strip()
    faq_data['브랜드'].append(1)
    faq_data['질문내용'].append(question_text)
    faq_data['답변내용'].append(answer_text)



    # (1) 첫 번째 FAQ 질문 요소 선택
    question_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[9]/div/div[1]/h6')
    question_text = question_elem.text.strip()

    # (2) 질문 요소 클릭하여 답변 영역 펼치기
    question_elem.click()
    time.sleep(0.3)

    # (3) 답변 추출 : 질문 요소 부모의 다음 형제 div에서 찾기
    answer_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[9]/div/div[2]/gb-content-well/adv-grid/adv-col/div/div/div/p')
    answer_text = answer_elem.text.strip()
    faq_data['브랜드'].append(1)
    faq_data['질문내용'].append(question_text)
    faq_data['답변내용'].append(answer_text)



    # (1) 첫 번째 FAQ 질문 요소 선택
    question_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[10]/div/div[1]/h6')
    question_text = question_elem.text.strip()

    # (2) 질문 요소 클릭하여 답변 영역 펼치기
    question_elem.click()
    time.sleep(0.3)

    # (3) 답변 추출 : 질문 요소 부모의 다음 형제 div에서 찾기
    answer_elem = driver.find_element(By.XPATH, '//*[@id="gb-main-content"]/adv-grid[5]/adv-col/div/div[10]/div/div[2]/gb-content-well/adv-grid/adv-col/div/div/div/p')
    answer_text = answer_elem.text.strip()

    faq_data['브랜드'].append(1)
    faq_data['질문내용'].append(question_text)
    faq_data['답변내용'].append(answer_text)

    driver.quit()

    return faq_data
