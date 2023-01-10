#pip install webdriver-manager
#Теперь вместо кода типа webdriver.Chrome('/home/user/drivers/chromedriver'),
#вы можете использовать менеджер, который всегда будет использовать поточную
#актуальную версию браузера и драйвера. Это имеет следующий вид для браузера Chrome:

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#-----------------------------------------------
import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(5)

driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

textarea.send_keys("get()")
time.sleep(5)

submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

submit_button.click()
time.sleep(5)

driver.quit()
