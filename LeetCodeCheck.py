import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime


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
user6 = "janother1"
userList = [user1, user2, user3, user4, user5, user6]

#Validate hoursLimit

hoursLimit = input("How many hours to limit: ")
if hoursLimit == "":
    hoursLimit = "24"


print("Limiting problems done to:", hoursLimit)
now = datetime.datetime.now()
print ("Current date and time: ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

for i in range(len(userList)):
    nameStore = ""
    URL = "https://leetcode.com/" + userList[i]
    driver.get(URL)
    # driver.implicitly_wait(5)

    counter = 1
    output = ""
    problemNameList = []
    while True:
        try:
            problemTime = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/a['+ str(counter) + ']/div/span[2]')
            problemTime = problemTime.text.strip().split(" ")[:2]
            problemName =  driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/a[' + str(counter) + ']/div/span[1]').text
            # print(problemName)
            # print(problemTime)
            if problemTime[1] == "days" or problemTime[1] == "months" or problemTime[1] == "day":
                break
            elif problemTime[1] == "hours":
            
                if problemTime[0] == "a":
                    problemTime[0] = 1
                if int(problemTime[0]) > int(hoursLimit):
                    pass
                else:
                    problemNameList.append(problemName)
            else: #seconds, minutes, minute
                problemNameList.append(problemName)
            counter += 1
        except:
            break

    output += "```ini\n" + userList[i] + " has done " + str(len(problemNameList)) + " problem(s) in the past " + str(hoursLimit) + " hours: ["
    for i in range(len(problemNameList)):
        if i < len(problemNameList) - 1:
            output += str(i + 1) + ". " + problemNameList[i] + ", "
        else:
            output += str(i + 1) + ". " + problemNameList[i] + "."
    output += "]\n```"
    print(output)
        
driver.quit()
"""
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
"""
