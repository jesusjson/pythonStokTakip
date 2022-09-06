import mysql.connector
import time

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "jesuotomasyon"
)
cursor = db.cursor()




#sec = input("a1")
def urunAdetKontrol(No):
    toplamUrun = "SELECT * FROM urunler WHERE urunBarkod = %s"
    adr = (No, )
    cursor.execute(toplamUrun, adr)
    result = cursor.fetchall()
    for x in result:
        Jadet = x[2]
    return Jadet


def urunEkle():
    while True:
        print("Çıkamak için lütfen [0] tuşlayın!")
        barkod = input("Lütfen ürün barkodunu giriniz: ")
        if barkod == "0":
            break
        urunAdSorgu = "SELECT * FROM urunler WHERE urunBarkod = %s"
        depoUrun = urunAdetKontrol(barkod)
        adr = (barkod, )
        cursor.execute(urunAdSorgu, adr)
        result = cursor.fetchall()
        for x in result:
            urunAd = x[1]
        print(f""" 
              ---- Ürün bilgileri ----
              1 - Ürün barkod: {barkod}
              2 - Ürün Ad: {urunAd}
              3 - Ürün adet: {depoUrun}
              
              [!] İşleme bu ürünlemi devam etmek istiyorsunuz [y/n] :
              """)
        sec = input("[?] ")
        if(sec == "y"):
            try:
                newAdet = int(input("Lütfen ürün adetini giriniz: "))
                toplamAdet = newAdet + depoUrun

                urunUpdate = "UPDATE urunler SET urunAdet = %s WHERE urunAdet = %s"
                val = (toplamAdet, depoUrun, )
                cursor.execute(urunUpdate, val)
                db.commit()
                print(f"{urunAd}'a {newAdet} adet eklendi toplam {toplamAdet} adetiniz oldu!")
            except ValueError as err:
                print(err)
        elif sec == "n":
            break
        
def urunAdetSil():
    while True:
        print("Çıkamak için lütfen [0] tuşlayın!")
        barkod = input("Lütfen ürün barkodunu giriniz: ")
        if barkod == "0":
            break
        urunAdSorgu = "SELECT * FROM urunler WHERE urunBarkod = %s"
        depoUrun = urunAdetKontrol(barkod)
        adr = (barkod, )
        cursor.execute(urunAdSorgu, adr)
        result = cursor.fetchall()
        for x in result:
            urunAd = x[1]
        print(f""" 
              ---- Ürün bilgileri ----
              1 - Ürün barkod: {barkod}
              2 - Ürün Ad: {urunAd}
              3 - Ürün adet: {depoUrun}
              
              [!] İşleme bu ürünlemi devam etmek istiyorsunuz [y/n] :
              """)
        sec = input("[?] ")
        if(sec == "y"):
            try:
                newAdet = int(input("Lütfen ürün adetini giriniz: "))
                toplamAdet = depoUrun - newAdet

                urunUpdate = "UPDATE urunler SET urunAdet = %s WHERE urunAdet = %s"
                val = (toplamAdet, depoUrun, )
                cursor.execute(urunUpdate, val)
                db.commit()
                print(f"{urunAd}'dan {newAdet} adet silindi mevcut {toplamAdet} adet ürününüz oldu!")
            except ValueError as err:
                print(err)
        elif sec == "n":
            break


        
######################### MAİN FUNCTİONS ##################################################
def urunKayit():
    
    while True:
        print("""
              ---- Kayıt seçenekler ----
              1 - Yeni ürün
              2 - Adet ekleme
              0 - Çıkış
              """)
        sec = int(input("Lütfen bir işlem numarası giriniz: "))

        if sec == 1:
            while True:
                print("Çıkamak için lütfen [0] tuşlayın!")
                barkod = input("Lütfen ürün barkodunu giriniz: ")
                if(barkod == "0"):
                    break
                else:
                    urunAd = input("Lütfen ürün adını giriniz: ")
                    if urunAd == "0":
                        break
                    else:
                        urunAdet = input("Lütfen ürün adeti giriniz: ")
                        if urunAdet == "0":
                            break
                        else:
                            ### KAYIT İŞLEM
                            kayit = "INSERT INTO urunler (urunBarkod, urunAd, urunAdet) VALUES (%s, %s, %s)"
                            val = (barkod,urunAd,urunAdet)
                            cursor.execute(kayit,val)
                            ### KAYIT İŞLEM SON
                            print("Kayıt işlem başarılı!")
                            print(f""" 
                                ---- Kayıt verileri ----
                                Ürün barkod: {barkod}
                                Ürün Adı: {urunAd}
                                Ürün Adet Eklenen: {urunAdet}
                                """)
                            db.commit()
                
        if sec == 2:
            urunEkle()  
        elif sec == 0:
            break
        
def urunSil():

    while True:
        print(""" 
              ---- Sil seçenekler ----
              1 - Ürün sil
              2 - Adet sil
              0 - Çıkış
              """)

        sec = input("Lütfen bir işlem numarası giriniz: ")
        
        if(sec == "1"):
            while True:
                print("Çıkış yapmak için [0] tuşlayınız! ")
                barkod = input("Silmek istediğiniz barkod numarasını giriniz: ")
                
                if barkod == "0":
                    break
                urunAdSorgu = "SELECT * FROM urunler WHERE urunBarkod = %s"
                adr = (barkod, )
                cursor.execute(urunAdSorgu, adr)
                result = cursor.fetchall()

                for x in result:
                    print(f""" 
                            ---- Kayıt verileri ----
                            Ürün barkod: {barkod}
                            Ürün Adı: {x[1]}
                            Ürün Adet Eklenen: {x[2]}
                            """)
                secim = input("Veriyi silmek istediğinize eminmisiniz [y/n]: ")

                if secim == "y":
                    silUrun = "DELETE FROM urunler WHERE urunBarkod = %s"
                    vl = (barkod, )
                    cursor.execute(silUrun, vl)
                    db.commit()
                    print("Ürün başarıyla silindi!")
                else:
                    break
        elif sec == "2":
            urunAdetSil()  
        elif sec == "0":
            break   
        
def urunListele():

    listeSQL = "SELECT * FROM urunler"
    cursor.execute(listeSQL, )
    liste = cursor.fetchall()
    for x in liste:
        print(f"""
              ---- Ürünler ----
              1 - Barkod Numarası: {x[0]}
              2 - Ürün Adı: {x[1]}
              3 - Ürün Adeti: {x[2]}
              """)
    time.sleep(5)
        

        
######################### MAİN FUNCTİONS ##################################################
  
while True:
    print(""" 
          ---- Lütfen bir işlem numarası seçiniz ----
          1 - Ürün Kayıt / Ekle
          2 - Ürün Sil / Adet Sil
          3 - Ürün listele
          0 - Çıkış
          """)
    sec = int(input("Numara: "))
    if sec == 1:
        urunKayit()
    elif sec == 2:
        urunSil()
    elif sec == 3:
        urunListele()
    elif sec == 0:
        break
    
