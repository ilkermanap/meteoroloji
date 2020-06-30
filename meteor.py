import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


class Meteor:
    def __init__(self, il_adi):
        self.iladi = il_adi
        
    def anlik(self):
        out = {}
        temp = getir(self.iladi, ["anlik-sicaklik", "anlik-diger"])
        out["sicaklik"] = float(temp[0].replace(",","."))
        out["durum"] = temp[1]
        out["yagis"] = float(temp[3].replace(",","."))
        out["nem"] = float(temp[6].replace(",","."))                           
        out["ruzgar"] = float(temp[8].replace(",","."))
        out["alcakbasinc"] = float(temp[10].replace(",","."))
        out["yuksekbasinc"] = float(temp[12].replace(",","."))    
        return out
        


    
def getir(iladi, classnames):
    opts = Options()
    opts.set_headless()   
    browser = Firefox(options=opts)
    browser.get(f"https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il={iladi}")
    #time.sleep(2)
    out = []
    for classname in classnames:
        bilgi = browser.find_element_by_class_name(classname).text.splitlines()
        for satir in bilgi:
            out.append(satir)
    browser.close()
    return out

    


if __name__ == "__main__":
    m = Meteor("Nevsehir")
    d = m.anlik()
    print(d)
