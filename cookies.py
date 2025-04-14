from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")





start_time=time.time()

while(1):
    try:
        cookie=driver.find_element(By.ID,value="cookie")
        cookie.click()
        money=int(driver.find_element(By.CSS_SELECTOR,value="#money").text.replace(",",""))
        
        upgrades_value=[]
        items=driver.find_elements(By.CSS_SELECTOR, value="#store b")
        for item in items:
            upgrades_value.append(item.text.split("-")[-1].strip().replace(",",""))
        upgrades_value[:]=upgrades_value[:-1]
        for i,val in enumerate(upgrades_value):
            upgrades_value[i]=int(upgrades_value[i])
        

    
        

        current_time=time.time()
        if current_time - start_time >= 5:
            cursor=driver.find_element(By.ID,value="buyCursor")
            grandma=driver.find_element(By.ID,value="buyGrandma")
            factory=driver.find_element(By.ID,value="buyFactory")
            mine=driver.find_element(By.ID,value="buyMine")
            shipment=driver.find_element(By.ID,value="buyShipment")
            alchemy_lab=driver.find_elements(By.CSS_SELECTOR,value="#store div")[-4]
            portal=driver.find_element(By.ID,value="buyPortal")
            time_machine=driver.find_elements(By.CSS_SELECTOR,value="#store div")[-2]

            data=[cursor,grandma,factory,mine,shipment,alchemy_lab,portal,time_machine]
            index=0
            max=0
            for i, v in enumerate(upgrades_value):
                if v>max and v<=money:
                    max=v
                    index=i
            if max<=money:
                data[index].click()
            start_time = current_time
    except StaleElementReferenceException:
        continue

        
  
