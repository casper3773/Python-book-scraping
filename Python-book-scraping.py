import requests
from bs4 import BeautifulSoup
import csv
import time



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
tum_veriler = []

for sayfa_no in range(1, 6):
    print(f"\n--- {sayfa_no} cekiliyor... ---")

    URL = f"https://www.kitapyurdu.com/cok-satan-kitaplar/haftalik/{sayfa_no}.html"
    cevap = requests.get(URL, headers=headers)

    if cevap.status_code == 200:
        soup = BeautifulSoup(cevap.content, "html.parser")
        kitaplar = soup.find_all("div", {"class": "ky-product"})
   
    
        for kitaplar in kitaplar:
            ad_etiketi = kitaplar.find("span",{"class":"ky-product-title"})
            fiyat_etiketi = kitaplar.find("span", {"class":"ky-product-price ky-product-sell-price"})
        
            if ad_etiketi and fiyat_etiketi:
                kitap_adi = ad_etiketi.text.strip()
                kitap_fiyati = " ".join(fiyat_etiketi.text.split())

                print(f"Kitap: {kitap_adi} - Fiyat: {kitap_fiyati}")
                tum_veriler.append([kitap_adi, kitap_fiyati])

        time.sleep(1)
                    
    else:
            print(f"Hata Meydana Geldi! Hata Kodu: {cevap.status_code}")
           
if tum_veriler:
    with open("kitaplarListesi.csv", "w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Kitap Adı", "Fiyat"]) #Baslıklar
        writer.writerows(tum_veriler) # Veriler

    print("\n" + "="*30)
    print("Veriler CSV dosyasına kaydedildi.")
    print("="*30)
    print(f"BİTTİ! Toplam {len(tum_veriler)} kitap bilgisi Excel dosyasına kaydedildi.")