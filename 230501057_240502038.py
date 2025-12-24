class Kitap:
    def __init__(self, ad, yazar, yil):
        self.ad = ad
        self.yazar = yazar
        self.yil = yil

    def bilgi_ver(self):
        return f"{self.ad} | {self.yazar} | {self.yil}"


class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, ad, yazar, yil):
        self.kitaplar.append(Kitap(ad, yazar, yil))
        return "Kitap sisteme eklendi."

    def kitap_sil(self, ad):
        for i in range(len(self.kitaplar)):
            if self.kitaplar[i].ad.lower() == ad.lower():
                del self.kitaplar[i]
                return "Kitap silme işlemi başarılı."
        return "Silinecek kitap bulunamadı."

    def ada_gore_ara(self, anahtar):
        sonuc = []
        for kitap in self.kitaplar:
            if anahtar.lower() in kitap.ad.lower():
                sonuc.append(kitap)
        return sonuc

    def yazara_gore_ara(self, anahtar):
        sonuc = []
        for kitap in self.kitaplar:
            if anahtar.lower() in kitap.yazar.lower():
                sonuc.append(kitap)
        return sonuc

    def tumunu_getir(self):
        return self.kitaplar


def menu_goster():
    print("\n--- KÜTÜPHANE OTOMASYONU ---")
    print("1) Kitap Ekle")
    print("2) Kitap Sil")
    print("3) Ada Göre Ara")
    print("4) Yazara Göre Ara")
    print("5) Kitapları Listele")
    print("0) Çıkış")


def uygulama():
    sistem = Kutuphane()

    while True:
        menu_goster()
        secim = input("Seçiminiz: ")

        if secim == "1":
            ad = input("Kitap adı: ")
            yazar = input("Yazar adı: ")
            yil = input("Yayın yılı: ")
            print(sistem.kitap_ekle(ad, yazar, yil))

        elif secim == "2":
            ad = input("Silinecek kitabın adı: ")
            print(sistem.kitap_sil(ad))

        elif secim == "3":
            kelime = input("Aranacak kitap adı: ")
            bulunanlar = sistem.ada_gore_ara(kelime)
            if bulunanlar:
                for k in bulunanlar:
                    print(k.bilgi_ver())
            else:
                print("Eşleşen kitap yok.")

        elif secim == "4":
            kelime = input("Aranacak yazar adı: ")
            bulunanlar = sistem.yazara_gore_ara(kelime)
            if bulunanlar:
                for k in bulunanlar:
                    print(k.bilgi_ver())
            else:
                print("Bu yazara ait kitap yok.")

        elif secim == "5":
            liste = sistem.tumunu_getir()
            if liste:
                for k in liste:
                    print(k.bilgi_ver())
            else:
                print("Kütüphane boş.")

        elif secim == "0":
            print("Program kapatılıyor...")
            break

        else:
            print("Hatalı seçim yaptınız.")


uygulama()
