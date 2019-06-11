import selenium
import json
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
import sys
from random import randint
from selenium.webdriver.common.by import By

    

def SearchStudents(ident,firstname,lastname,middleinitial,obligation,driver):
    element=driver.find_element_by_name("studentID")
    element.send_keys(ident)
   # button=driver.find_element_by_css_selector('input.btn btn-lg btn-success')
    button=driver.find_element_by_id('form-submit')
   # button=driver.find_element_by_tag_name('input class="btn btn-lg btn-success" type="submit" value="Submit"')
    button.click()
    ticketEntry(ident,firstname,lastname,middleinitial,obligation,driver)
    

def SearchStudentsLast(ident,firstname,lastname,middleinitial,obligation,driver):
    element=driver.find_element_by_name("studentID")
    element.send_keys(ident)
   # button=driver.find_element_by_css_selector('input.btn btn-lg btn-success')
    button=driver.find_element_by_xpath('//input[@class="btn btn-lg btn-success" and @type="submit" and @value="Submit"]')
   # button=driver.find_element_by_tag_name('input class="btn btn-lg btn-success" type="submit" value="Submit"')
    button.click()
    ticketEntry(ident,firstname,lastname,middleinitial,obligation,driver)        

def ticketEntry(ident,firstname,lastname,middleinitial,obligation,driver):
    

    a=randint(0,2)
    if (a==0):
        element=driver.find_element_by_id("payCash")
        element.click()
    elif (a==1):
        element=driver.find_element_by_id("payCheck")
        element.click()
        b=randint(1000000,9999999)
        element=driver.find_element_by_id("checkNum")
        element.send_keys(b)
    else:
        element=driver.find_element_by_id("payWaiver")
        element.click()


##    oblig=driver.find_element_by_id("oblig")
##    oblig.click()
    tick=randint(10000000,99999999)
    ticket=driver.find_element_by_id("ticketNum")
    ticket.send_keys(tick)
    enterGuest()
    saving=driver.find_element_by_id("saveButton")
    saving.click()
    
    alert=driver.switch_to.alert
    alert.accept()

    time.sleep(1)

def ticketRawEntry(ident,firstname,lastname,middleinitial,obligation,driver):
    element=driver.find_element_by_id("studentID")
        element.send_keys(ident)
        element=driver.find_element_by_id("firstName")
        element.send_keys(firstname)
        element=driver.find_element_by_id("lastName")
        element.send_keys(lastname)
        element=driver.find_element_by_id("midInit")
        element.send_keys(middleinitial)
        element=driver.find_element_by_id("grade")
        element.send_keys(obligation)
    
    
    a=randint(0,2)
    if (a==0):
        element=driver.find_element_by_id("payCash")
        element.click()
    elif (a==1):
        element=driver.find_element_by_id("payCheck")
        element.click()
        b=randint(1000000,9999999)
        element=driver.find_element_by_id("checkNum")
        element.send_keys(b)
    else:
        element=driver.find_element_by_id("payWaiver")
        element.click()
    
    
    ##    oblig=driver.find_element_by_id("oblig")
    ##    oblig.click()
    tick=randint(10000000,99999999)
    ticket=driver.find_element_by_id("ticketNum")
    ticket.send_keys(tick)
    enterGuest()
    saving=driver.find_element_by_id("saveButton")
    saving.click()
    
    alert=driver.switch_to.alert
    alert.accept()

time.sleep(1)


def enterGuest():
    with open('/Users/ryanli/Documents/Good virtual data 10000 right form.json') as json2:
        data=json.load(json2)
        
        for p in data['objects']:
            ID=p['']
            FN=p['FIRST']
            LN=p['LAST']
            MI=p['MI']
            GD=p['GR']
            element=driver
            
            

def getExistData():
    options=webdriver.ChromeOptions()
    options.add_argument("--test-type")
    
    driver_path=r'/Users/ryanli/Documents/chromedriver'##Need to download the chromedriver

    driver=webdriver.Chrome(driver_path)
   
    driver.get("http://localhost:3000/search-student")##Need to re-enter the web address
    with open('/Users/ryanli/Documents/StudentIDListThing.json') as json2:
        data=json.load(json2)
        i=0
        
        for p in data['objects']:
            
            ID=p['ID']
            FN=p['FIRST']
            LN=p['LAST']
            MI=p['MI']
            GD=p['GR']
            a=time.time()
            SearchStudents(ID,FN,LN,MI,GD,driver)
            b=time.time()
            print(b-a)
            driver.get("http://localhost:3000/search-student")
          #  print(ID)
            i+=1

getExistData()
            
def getUnexistData():
    options=webdriver.ChromeOptions()
    options.add_argument("--test-type")
    
    driver_path=r'/Users/ryanli/Documents/chromedriver'##Need to download the chromedriver

    driver=webdriver.Chrome(driver_path)
   
    driver.get("http://localhost:3000/ticket-entry?studentID=&lastname=")##Need to re-enter the web address
    with open('/Users/ryanli/Documents/Good virtual data 10000 right form.json') as json2:
        data=json.load(json2)
       
        i=1
        for p in data['objects']:
            if(i==2100):
                break
            
            ID=p['ID']
            FN=p['FirstName']
            LN=p['LastName']
            MI=p['MiddleInitial']
            GD=p['Grade']
            #SearchStudents(ID,FN,LN,MI,GD,driver)
            a=time.time()
            ticketEntry(ID,FN,LN,MI,GD,driver)
            b=time.time()
            print(b-a)
            driver.get("http://localhost:3000/ticket-entry?studentID=&lastname=")
          #  print(ID)
            i+=1
            
def main():
    a=int(input("Would you like to test out (1) existen data or (2) unexisten data?:"))
    if (a==1):
        getExistenData()
    elif(a==2):
        getUnexistData()

main()
