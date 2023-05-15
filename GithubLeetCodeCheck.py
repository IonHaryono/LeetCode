import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
driver = webdriver.Chrome(options=options)

user1 = "IonH"
user2 = "eric-yem"
user3 = "ZeloSama"
user4 = "MintMuffinz"
user5 = "imashapereraa"
userList = [user1, user2, user3, user4, user5]

for i in range(len(userList)):
    nameStore = ""
    URL = "https://leetcode.com/" + userList[i]
    driver.get(URL)
    # driver.implicitly_wait(5)

    secondProblem = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/a[2]/div/span[2]')
    secondTime = secondProblem.text.strip().split(" ")[1]
    # print(secondTime)
    if secondTime == "days" or secondTime == "months":
        # print(userList[i] + " has NOT done 2 problems.")
        firstProblem = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/a[1]/div/span[2]')
        firstTime = firstProblem.text.strip().split(" ")[1]

        if firstTime == "days" or firstTime == "months":
            print(userList[i] + " has not done any problems today.")
        else: 
            firstName = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/a[1]/div/span[1]').text
            print(userList[i] + " has done only 1 problem today: " + firstName + ".")

           
    else:
        firstName = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/a[1]/div/span[1]').text
        secondName = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/a[2]/div/span[1]').text
        print(userList[i] + " has done 2 problems today: " + firstName + ", " + secondName + ".")


driver.quit()