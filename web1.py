from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver .maximize_window()
driver.find_element_by_name("wd").send_keys("哈哈")
driver.find_element_by_id("su").click()
sleep(5)
driver.quit()



#from selenium webdriver.Common.keys import Keys
#调用键盘
#driver.sleep_element_name("wd").send._keys(Keys.CONTROL,"a")(Keys,ENTEL)

# ctrl + D 复制一行
# Alt +左键 同时操作多个元素

