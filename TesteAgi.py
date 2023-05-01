from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL= "https://blogdoagi.com.br/"

nav = webdriver.Chrome()
nav.get(BASE_URL)
nav.maximize_window()

wait = WebDriverWait(nav, 25)
searchbtn = wait.until(EC.visibility_of_element_located((By.ID, 'search-open')))
searchbtn.click()
#campos abaixo não possui ID e NAME, por essa razão estou usando o xpath pois o css selector também não é boa pratica por causa do DOM.
nav.find_element(By.XPATH, '//*[@id="masthead"]/div[1]/div[2]/form/label/input').send_keys('Sua Carreira')
submetebtn = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="masthead"]/div[1]/div[2]/form/input')))
submetebtn.click()
nav.quit()
