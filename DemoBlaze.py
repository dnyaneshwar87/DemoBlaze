import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(".\\chromedriver.exe")
driver.get("https://demoblaze.com/index.html")
driver.maximize_window()
driver.implicitly_wait(7)
driver.find_element(By.ID, "login2").click()
driver.find_element(By.ID, "loginusername").send_keys("sctqaautomation@grr.la")
driver.find_element(By.ID, "loginpassword").send_keys("Spring@123")
driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
time.sleep(5)
add_card= driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']")
add_card.click()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)

driver.get("https://demoblaze.com/index.html")
# driver.back()
time.sleep(5)

driver.find_element(By.XPATH, "//a[3]").click()
time.sleep(10)
driver.find_element(By.LINK_TEXT, "Dell i7 8gb").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
time.sleep(5)
driver.switch_to.alert.accept()

driver.get("https://demoblaze.com/index.html")
# driver.back()
time.sleep(5)

driver.find_element(By.XPATH, "//a[4]").click()
time.sleep(10)
driver.find_element(By.LINK_TEXT, "ASUS Full HD").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)
driver.find_element(By.ID, "cartur").click()
time.sleep(5)
ele=[]
# for i in range(1,4):
elements = driver.find_elements(By.XPATH, "//tbody/tr/td[3]")
# m=1
for k in elements:
    # print(k.text)
    l = int(k.text)
    ele.append(l)
    # m=m+1
    # if(m>4):
    #     break
ele.sort()
print(ele)
from functools import reduce
val = reduce(lambda x,y: x+y, ele)
print (val)

total = (driver.find_element(By.ID, "totalp").text)
print(total)
if val == int(total):
    print("total Amount verification Done")
else:
    print("total Amount verification Fail")

driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()
time.sleep(5)
driver.find_element(By.ID, "name").send_keys("Mauli")
driver.find_element(By.ID, "country").send_keys("India")
driver.find_element(By.ID, "city").send_keys("Pune")
driver.find_element(By.ID, "card").send_keys("544667889993")
driver.find_element(By.ID, "month").send_keys("November")
driver.find_element(By.ID, "year").send_keys("2022")
driver.find_element(By.XPATH, "//button[normalize-space()='Purchase']")
variable = driver.switch_to.alert
# All_order = (driver.find_element(By.XPATH, "//p[@class='lead text-muted ']").get_attribute("InnerText"))
print(variable.text)












# driver.close()

