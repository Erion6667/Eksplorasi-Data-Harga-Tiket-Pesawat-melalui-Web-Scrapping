import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "https://www.tiket.com/pesawat/search?d=SUBC&a=JKTC&dType=CITY&aType=CITY&date=2023-05-31&adult=1&child=0&infant=0&class=economy&flexiFare=true"
driver = webdriver.Chrome()
driver.get(url)

data = []

for j in range(45):
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 250)")
        time.sleep(1)

soup = BeautifulSoup(driver.page_source, "html.parser")

#Discount Ticket
for item in soup.findAll("div", class_ = "harga_coret_regular"):
    maskapai = item.find("span", class_ = "text-marketing-airline").text
    print(maskapai)
    print("=")
    jam_takeoff = item.find("div", class_ = "text-time").text
    print(jam_takeoff)
    print("==")
    bandara_takeoff = item.find("div", class_ = "text-code").text
    print(bandara_takeoff)
    print("===")
    
    for item_2 in item.findAll("div", class_ = "list-horizontal__middle"):
        for i,item__1 in enumerate(item_2.findAll("div", class_ = "row")):
            if i == 0:
                jam_penerbangan = item__1.find("div", class_ = "text-total-time").text
                print(jam_penerbangan)
                print("====")
                break
        for j,item__2 in enumerate(item_2.findAll("div", class_ = "row")):
            if j == 2:    
                metode_penerbangan = item__2.find("div", class_ = "text-total-time").text
                print(metode_penerbangan)
                print("=====")
                break
    
    for k, item_3 in enumerate(item.findAll("div", class_ = "list-horizontal__middle")[4]): 
        if k == 0:
            jam_landing = item_3.text
            print(jam_landing)
            print("======")
        if k == 1:
            bandara_landing = item_3.text
            print(bandara_landing)
            print("=======")
            break
    
    for item_4 in item.findAll("div", class_ =  "priceV2"):
        for l,item__3 in enumerate(item_4.findAll("div", class_ = "text-price")):
            if l == 0:
                harga_diskon = item__3.find("div", class_ = "text-price-main").text
                print(harga_diskon)
                print("========")
            if l == 1:
                harga_asli = item__3.find("div", class_ = "text-price-main").text
                print(harga_asli)
                print("=========")
                break
    data.append(
                (maskapai, jam_takeoff, bandara_takeoff, metode_penerbangan, jam_landing, bandara_landing, harga_diskon, harga_asli)
            )

#Not Discount Ticket
for item2 in soup.findAll("div", class_ = "wrapper-flight-list"):
    maskapai = item2.find("span", class_ = "text-marketing-airline").text
    print(maskapai)
    print("-")
    jam_takeoff = item2.find("div", class_ = "text-time").text
    print(jam_takeoff)
    print("--")
    bandara_takeoff = item2.find("div", class_ = "text-code").text
    print(bandara_takeoff)
    print("---")
    
    for item_5 in item2.findAll("div", class_ = "list-horizontal__middle"):
        for i,item__4 in enumerate(item_5.findAll("div", class_ = "row")):
            if i == 0:
                jam_penerbangan = item__4.find("div", class_ = "text-total-time").text
                print(jam_penerbangan)
                print("----")
                break
        for j,item__5 in enumerate(item_5.findAll("div", class_ = "row")):
            if j == 2:    
                metode_penerbangan = item__5.find("div", class_ = "text-total-time").text
                print(metode_penerbangan)
                print("-----")
                break
    
    for k, item_6 in enumerate(item2.findAll("div", class_ = "list-horizontal__middle")[4]): 
        if k == 0:
            jam_landing = item_6.text
            print(jam_landing)
            print("------")
        if k == 1:
            bandara_landing = item_6.text
            print(bandara_landing)
            print("-------")
            break
    
    for item_7 in item2.findAll("div", class_ =  "priceV2"):
        for item__6 in item_7.findAll("div", class_ = "text-price-default"):    
            harga_diskon = " "
            print(harga_diskon)
            print("--------")
            harga_asli = item__6.find("div", class_ = "text-price-main-default").text
            print(harga_asli)
            print("---------")
    
    data.append(
                (maskapai, jam_takeoff, bandara_takeoff, metode_penerbangan, jam_landing, bandara_landing, harga_diskon, harga_asli)
            )

df = pd.DataFrame(data, columns = ["Maskapai", "Jam Takeoff", "Bandara Takeoff", "Metode Penerbangan", "Jam Landing",
"Bandara Landing", "Harga Diskon", "Harga Asli"])
print(df)

df.to_csv("tiketcom.csv", index = False)
print("Data Telah Tersimpan")
driver.close()