from selenium import webdriver
import threading

chrome_driver_path = "F:\software\chrome drive\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")
big_cookie = driver.find_element_by_id("bigCookie")
click = 1
a = 1
base = 0

def check_unlock():
    threading.Timer(6.0, check_unlock).start()  # called every minute
    print("running check unlock")
    store_section = driver.find_elements_by_css_selector("#products .enabled")
    print(store_section)
    for i in store_section[::-1]:
        # print("owned", i.find_element_by_class_name("owned"))
        # print("owned", i.find_element_by_class_name("owned").text)
        if i.find_element_by_class_name("owned").text != "":
            if int(i.find_element_by_class_name("owned").text) > 40:
                continue
        i.click()
    upgrade_section = driver.find_elements_by_css_selector("#upgrades .enabled")
    for i in upgrade_section[::-1]:
        i.click()


check_unlock()
while True:
    big_cookie.click()
    click += 1
    print("click", click)

# driver.quit()
