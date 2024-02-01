from bs4 import BeautifulSoup
import json
import requests as rq
import pandas as pd
from datetime import datetime





headerss = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

OOS_remarks=[]

def myntra_price():
    style_id = ['15580238']

    for i in style_id:
        res_4 = rq.Session().get(f'https://www.myntra.com/foundation-and-primer/swiss-beauty/swiss-beauty-long-lasting-makeup-fixer-natural-spray---aloe-vera-with-vitamin-e-50-ml/{i}/buy', headers=headerss)
        soup_4 = BeautifulSoup(res_4.text, 'lxml')
        script = None
        try:
            for s in soup_4.find_all("script"):
                if 'pdpData' in s.text:
                    script = s.get_text(strip=True)
                    break
            aa=json.loads(script[script.index('{'):])
            # print(aa)
            # get seller name
            price_look_4 = aa['pdpData']['selectedSeller']['discountedPrice']
            print(price_look_4)
        except:
            price_look_4 = 'OOS'
            # print(price_look_4)
        OOS_remarks.append([i,price_look_4,'Myntra'])
    df = pd.DataFrame(OOS_remarks, columns=['Myntra_Code', 'Myntra_Price', 'Myntra_Seller'])
    df.to_excel(f'D:\\Office\\Myntra\\Swiss Beauty\\OOS Tracker_{datetime.now().strftime("%d-%m-%Y %H-%M-%S")}.xlsx', index=False)


if __name__ == "__main__":
    myntra_price()