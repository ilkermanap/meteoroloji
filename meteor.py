import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

    
def getir(iladi):
    opts = Options()
    opts.set_headless()   
    browser = Firefox(options=opts)
    browser.get(f"https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il={iladi}")
    #time.sleep(2)
    bilgi = browser.find_element_by_class_name("anlik-sicaklik").text.splitlines()
    print(bilgi)
    isi, durum, y, yagis = bilgi

    print(isi)
    browser.close()
    


if __name__ == "__main__":
    getir("Nevsehir")
    getir("Ankara")
