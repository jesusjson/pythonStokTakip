import mysql.connector
import time
import os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
js = db.cursor()

print("[DATABASE] Kurulum işlemi başlıyor!")

try:
    js.execute("CREATE DATABASE jesuotomasyon")
    print("[DATABASE] Database kuruldu!")
  
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jesuotomasyon"
    )
    jc = mydb.cursor()
    time.sleep(4)
    
    jc.execute("CREATE TABLE urunler (urunBarkod VARCHAR(15), urunAd VARCHAR(20), urunAdet INT(11))")
    print("[DATABASE] Tablolar oluşturuldu!")
    
    time.sleep(2)
    print("[DATABASE] Sistem kullanıma hazır!")
    os.remove("kurulum.bat")
    os.remove("kurulum.py")
except ValueError as err:
    print("[DATABASE] Bir hata ile karşılaştım " + err)