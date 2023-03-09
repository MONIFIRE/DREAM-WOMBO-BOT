import requests,os
from getuseragent import UserAgent
import json,time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import chromedriver_autoinstaller
import time
from selenium.webdriver import ActionChains
import urllib


useragent = UserAgent()
theuseragent = useragent.Random()

url = "https://paint.api.wombo.ai/api/v2/tasks"
# TOKEN DREAM WOMBO
token = ""
HEADERS = {
    "authorization": f"bearer {token}",
    "user-agent": theuseragent
}

def send_message_draw(url):
    dream = open('wombo.txt', 'r', encoding='utf-8')
    prompt = dream.read()
    response = requests.post(url, headers=HEADERS, json={"is_premium":False,"input_spec":{"prompt":prompt,"style":84,"display_freq":10}})
    if response.status_code == requests.codes.ok:
        response_json = json.loads(response.text)
        task_id = response_json['id']
        load = [f'processing image {task_id}']
        for mess_load in load:
            for i in range(6):
                time.sleep(10)
                random_int = random.randint(1, 5)
                print(f"\n{load} [{random_int}]\n") 
        resimage = requests.post('https://dream.ai/api/gallery', json={"task_id":task_id,"name":"","is_public":True,"is_prompt_visible":True,"tags":[]},headers=HEADERS)
        if resimage.status_code == 200:
             chromedriver_autoinstaller.install()
             chrome_options = webdriver.ChromeOptions()
             chrome_options.add_argument("--mute-audio")
             chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
             driver = webdriver.Chrome(options=chrome_options)
             driver.get('https://dream.ai/listing/'+task_id)
             
             with open('dream.png', 'wb') as file:

                l = driver.find_element(By.XPATH, '//*[@alt="trading_card"]')

                file.write(l.screenshot_as_png)

                driver.quit()
                
                print ("\n[ / ] The picture is already in your file dream.png")
            
        else:
             print(f"\n[ x ] Error sending message: {resimage.status_code} - {resimage.text}")            
    else:
         print(f"\n[ x ] Error sending message: {response.status_code} - {response.text}")

if __name__ == '__main__':
    send_message_draw(url)
