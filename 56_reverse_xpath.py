from selenium import webdriver
import time
list = []
list2 = []
driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(3)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
##//div[@class='product-action']/button/parent::div/parent::div/h4   ## reverse of x path
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list)

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

vegitable = driver.find_elements_by_xpath("//tr/td[2]/p")
for veg in vegitable:
    list2.append(veg.text)
print(list2)
print(len(list2))
assert list == list2




