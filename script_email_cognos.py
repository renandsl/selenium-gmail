from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {"download.default_directory": r"D:\Meus Documentos\Projetos Python\bd\diario_cognos"})

with open(r"D:\Meus Documentos\Projetos Python\bd\credentials.json", 'r') as file:
    credenciais = json.load(file)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
email_url = "https://mail.google.com/mail/u/0/#inbox"
driver.get(email_url)

sleep(5)

email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_input.send_keys(credenciais["email"])
email_input.send_keys(Keys.RETURN)

sleep(3)

password_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password_input.send_keys(credenciais["password"])
password_input.send_keys(Keys.RETURN)

sleep(3)

notificacao = 'notificacao-cognos'
wait = WebDriverWait(driver, 10)

emails = driver.find_elements(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[2]/div/table/tbody/tr')

for email in emails:
    
    try:
        
        assunto = wait.until(EC.visibility_of_element_located((By.XPATH, './/td[4]/div[2]/span/span')))
        subject_text = assunto.text.lower()

        if notificacao.lower() in subject_text:
            print(f'Assunto: {subject_text}')
            email.click()
            sleep(2)
            download_button = driver.find_element(By.CLASS_NAME, 'T-I.J-J5-Ji.aQv.T-I-ax7.L3')
            download_button.click()
            sleep(2)
            driver.execute_script("window.history.go(-1)")

    except Exception as e:
        print(f'Erro ao processar e-mail: {e}')

sleep(3)

check_box = driver.find_element(By.XPATH, '//*[@id=":1y"]/div[1]/span')
check_box.click()

delete_button = driver.find_element(By.XPATH, '//div[@class="T-I J-J5-Ji nX T-I-ax7 T-I-Js-Gs mA"]')
# delete_button.click()
sleep(5)
print('Coleta finalizada')
