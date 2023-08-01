from selenium import webdriver
from time import sleep


chrome_driver_path = "F:\software\chrome drive\chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://spribe.co/games/aviator")
sleep(3)

email_section = driver.find_element_by_xpath("/html/body/app-root/app-layout/app-game-details/div/section[1]/div/div/div/a/button").click()
sleep(1)
driver.find_element_by_xpath("/html/body/ngb-modal-window/div/div/app-age-permission-modal/div[3]/button[1]").click()

another_window = list(set(driver.window_handles) - {driver.current_window_handle})[0]
print(driver.window_handles)
driver.switch_to.window(another_window);
sleep(12)
driver.find_element_by_xpath("/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/div[1]/div[2]/button").click()





