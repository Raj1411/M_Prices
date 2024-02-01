import streamlit as st
from bs4 import BeautifulSoup
import json
import requests as rq
from datetime import datetime
from time import sleep

headerss = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def myntra_price(style_id):
    try:
        res_4 = rq.Session().get(f'https://www.myntra.com/foundation-and-primer/swiss-beauty/swiss-beauty-long-lasting-makeup-fixer-natural-spray---aloe-vera-with-vitamin-e-50-ml/{style_id}/buy', headers=headerss)
        soup_4 = BeautifulSoup(res_4.text, 'lxml')
        script = None
        for s in soup_4.find_all("script"):
            if 'pdpData' in s.text:
                script = s.get_text(strip=True)
                break
        aa = json.loads(script[script.index('{'):])
        price_look_4 = aa['pdpData']['selectedSeller']['discountedPrice']
        sleep(1)
        return price_look_4
    except:
        return 'OOS'

def main():
    st.title("Myntra Price Tracker")

    style_ids = ['15580238']  # Add more Style IDs as needed
    
    for style_id in style_ids:
        price = myntra_price(style_id)
        st.success(f"Myntra Price for Style ID {style_id}: {price}")

if __name__ == "__main__":
    main()
