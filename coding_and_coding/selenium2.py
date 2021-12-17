from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

import time
import string
import random

def sendEmail():
    xx=list(string.ascii_lowercase)

    pas=''
    for x in range(random.randint(8,12)):
        
        pas+=xx[random.randint(0,25)]

    return pas+random.choice(['@yahoo.com','@gmail.com','@outlook.com'])
    

listOFMail=[]


for x in range(15):
    
    browserpath=r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
    driverPath=r'D:\webDrive\chromedriver.exe'

    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    
    options.binary_location = browserpath

    driver = webdriver.Chrome(chrome_options=options, 
    executable_path=driverPath )

    driver.get('https://quizlet.com/sign-up')
    # select="div[class='single-ayah']"
    time.sleep(.2)

    bMnt=driver.find_element_by_name('birth_month')
    day=driver.find_element_by_name('birth_day')
    yar=driver.find_element_by_name('birth_year')

    email=driver.find_element_by_id('email')
    pss=driver.find_element_by_id('password1')


    mn=Select(bMnt)
    dy=Select(day)
    yr=Select(yar)

    # time.sleep(.1)

    mn.select_by_value(str(random.randint(1,12)))
    dy.select_by_value(str(random.randint(1,30)))
    yr.select_by_visible_text( random.choice(['1997','1998','1999','2000','2001','2002']) )



    # time.sleep(.2)

    mail=sendEmail()
    listOFMail.append(mail)
    email.send_keys(mail)
    pss.send_keys('mannerMan@1')



# ''' this thing advanced//// if cant work with some element...'''
# '''it first target some near element then add offset for clicking the desired button...'''

    el=driver.find_element_by_class_name('TosCheckbox')

    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(el, 0, 8)
    action.click()
    action.perform()
    #### done.........>>>>>>>> /////////>>>>>>

    try:
        driver.find_element_by_name('is_parent').click()
    except:
        print('invvvv>>>')
    
    time.sleep(.8)

    driver.find_element_by_class_name('UILoadingButton').click()
    time.sleep(7)

    print(listOFMail)



    driver.close()

print(listOFMail)
with open('readme.txt', 'w') as f:
    for x in listOFMail:
        f.write(x+'\n')


driver.close()
