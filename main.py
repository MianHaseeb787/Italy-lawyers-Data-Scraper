import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("/Users/mian/ScrapedData/CNF_sel/chromedriver")
driver = webdriver.Chrome(service=service)

def iterate_cards():

        try:
            
            elements = driver.find_elements(By.CLASS_NAME, 'card-avvocato--clickable')

            print("Number of elements found:", len(elements))

            for i in range(len(elements)):
                elements = driver.find_elements(By.CLASS_NAME, 'card-avvocato--clickable')
                element = elements[i]

                print("element", i)
                

                element.click()
                try:
                    # time.sleep(1)

                    
                    # name = driver.find_element(By.CLASS_NAME, "card-avvocato__name")
                    # name = name.text

                    
                    waitcards = WebDriverWait(driver, 10) 
                    infos = waitcards.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card-avvocato__info")))

                
                    avvocato_data = {}

                    avvocato_data["City"] = city

                    

                    
                    for info in infos:
                        
                        info_text = info.text.strip()

                        
                        if "E-mail" in info_text:
                        
                            email = info_text.split("E-mail")[-1].strip()
                            print(email)
                            
                            avvocato_data["Email"] = email
                        elif "PEC" in info_text:
                            
                            pec = info_text.split("PEC")[-1].strip()
                        
                            print(pec)
                            avvocato_data["PEC"] = pec

                    
                    data.append(avvocato_data)

                    waitname = WebDriverWait(driver, 10) 
                    name = waitname.until(EC.presence_of_element_located((By.CLASS_NAME, "card-avvocato__name")))
                    print(name.text)
                    avvocato_data["Name"] = name.text

                
                    back_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Torna a tutti i risultati di ricerca')]"))
                    )
                    driver.execute_script("arguments[0].click();", back_btn)

                except Exception as e:
                    #  time.sleep(1)
                    print(f"Exception : {e}")

                    
                    name = driver.find_element(By.CLASS_NAME, "card-avvocato__name")
                    name = name.text

                    infos = driver.find_elements(By.CLASS_NAME, "card-avvocato__info")

                
                    avvocato_data = {}

                    avvocato_data["City"] = city

                    avvocato_data["Name"] = name

                    
                    for info in infos:
                        
                        info_text = info.text.strip()

                        
                        if "E-mail" in info_text:
                        
                            email = info_text.split("E-mail")[-1].strip()
                            print(email)
                            
                            avvocato_data["Email"] = email
                        elif "PEC" in info_text:
                            
                            pec = info_text.split("PEC")[-1].strip()
                        
                            print(pec)
                            avvocato_data["PEC"] = pec

                    
                    data.append(avvocato_data)

                
                    back_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Torna a tutti i risultati di ricerca')]"))
                    )
                    driver.execute_script("arguments[0].click();", back_btn)
                     
                

        except Exception as e:
            print(e)
            


data = []

driver.get("https://www.consiglionazionaleforense.it/ricerca-avvocati")
time.sleep(25)


desired_page = 1




city = "VITERBO"

for i in range(1,desired_page):
        time.sleep(2.5)
        
        successiva_button = driver.find_element(By.XPATH, "//button[contains(text(), 'successiva')]")
        successiva_button.click()

        print(f"next button clicked  {i}")

time.sleep(2)

iterate_cards()

# writemode = ""
# if desired_page == 1:
#      writemode = "w"
# else:
#      writemode = "a"

with open("CNF-LawyersData-M3L.csv", "w", newline="") as csvfile:
    
    fieldnames = ["Name", "Email", "PEC", "City"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # if desired_page == 1:
    writer.writeheader()
    
    for row in data:
        writer.writerow(row)
        

driver.quit()
