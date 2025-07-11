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

    path = 'chromedriver.exe'
    service = webdriver.chrome.service.Service(path)
    driver = webdriver.Chrome(service=service)

    driver.get('https://polestar.com/kr/support/')
    time.sleep(3)

    # 팝업창 
    button_path = driver.find_element(By.ID,'onetrust-accept-btn-handler')
    button_path.click()
    time.sleep(1)

    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    pol_chg_btn = driver.find_element(By.XPATH, '//*[@id="faq"]/div/div[2]/div[9]/a' )
    pol_chg_btn.click()
    time.sleep(1)

    pol_ChgPlus_btn = driver.find_element(By.XPATH,'//*[@id="where-can-i-find-information-about-charging-a-polestar-car"]/button')
    pol_ChgPlus_btn.click()
    time.sleep(1)

    pol_chg_title = driver.find_element(By.CSS_SELECTOR, '.css-159k6z1 span')
    pol_chg_ans = driver.find_element(By.CSS_SELECTOR, '.css-chjg7v')

    faq_data['브랜드'].append(3)
    faq_data['질문내용'].append(pol_chg_title.text)
    faq_data['답변내용'].append(pol_chg_ans.text)

    pol_back_btn = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/nav/a')
    pol_back_btn.click()
    time.sleep(1)

    # 2번째 창
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    pol_huschg_btn = driver.find_element(By.XPATH, '//*[@id="faq"]/div/div[2]/div[10]/a')
    pol_huschg_btn.click()
    time.sleep(1)

    pol_husPlus_btn = driver.find_element(By.XPATH, '//*[@id="what-is-the-point-of-charging-timers-and-how-do-they-work"]/button')
    pol_husPlus_btn.click()
    time.sleep(1)

    pol_hus_title = driver.find_element(By.CSS_SELECTOR, '.css-159k6z1')
    pol_hus_ans = driver.find_element(By.CSS_SELECTOR, '.x_elementToProof')
    
    faq_data['브랜드'].append(3)
    faq_data['질문내용'].append(pol_hus_title.text)
    faq_data['답변내용'].append(pol_hus_ans.text)

    pol_back_btn = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/nav/a')
    pol_back_btn.click()
    time.sleep(1)

    # 3번째 창 보증 창
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    link_move_path = driver.find_element(By.XPATH,'//*[@id="faq"]/div/div[2]/div[12]/a')    # //*[@id="faq"]/div/div[2]/div[12]/a
    link_move_path.click()
    time.sleep(1)

    # 보증 페이지로 넘어와 faq 저장
    button = driver.find_element(By.ID ,'what-warranty-is-included-title')
    button.click()
    time.sleep(1)

    title_tag = driver.find_element(By.CSS_SELECTOR,'.css-159k6z1 span')

    contents = driver.find_elements(By.CSS_SELECTOR,'p.css-chjg7v')
    content=[]
    for i,x in enumerate(contents):
        content.append(x.text)
        if i==3:
            break

    answer=" ".join(x for x in content)

    faq_data['브랜드'].append(3)
    faq_data['질문내용'].append(title_tag.text)
    faq_data['답변내용'].append(answer)

    
    driver.quit()

    return faq_data





