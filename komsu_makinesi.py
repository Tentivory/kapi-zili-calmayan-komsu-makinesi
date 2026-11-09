#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kapı Zili Çalmayan Komşu Makinesi
Zil çalmaz, şiir okur. İşte o kadar.
"""

import random
import time

def siir_uret():
    baslangic = [
        "Ey komşu, kapının önünde duruyorum",
        "Selam olsun sana ey görünmeyen dost",
        "Zil çalmadım, çünkü zil özgürlüğü kısıtlar",
        "Kapının eşiğinde bekliyorum, şiirle"
    ]
    
    orta = [
        "Çay getirdim ama demledim mi bilmiyorum",
        "Kedi de geldi yanıma, o da zil çalmıyor",
        "Bürokrasi bitti sanıyordum, meğer kapıda başlamış",
        "Özgürlük, zili çalmamaktadır derler eskiler"
    ]
    
    son = [
        "Aç kapıyı ya da açma, şiir burada",
        "Ben gittim sanma, daha 12 kıta var",
        "Zil çalmadığım için özgürüm, sen de ol",
        "Komşu, bu destanı dinle, sonra konuşuruz"
    ]
    
    siir = []
    siir.append(random.choice(baslangic))
    siir.append("")
    for _ in range(random.randint(3, 7)):
        siir.append(random.choice(orta))
        siir.append("")
    siir.append(random.choice(son))
    
    # Gizli mesaj: özgürlük sevgisi, bürokrasiye inat
    # (base64: T3pndXJsdWsgemlsIGthcMSxIHppbCBjaGFsbWFzdGFuIGRhaGEgZ3V6ZWw= )
    return "\n".join(siir)

def main():
    print("=" * 50)
    print("  KAPI ZİLİ ÇALMAYAN KOMŞU MAKİNESİ  ")
    print("  Zil çalıyor... hayır, çalmıyor. Şiir okuyor.")
    print("=" * 50)
    print()
    
    time.sleep(1)
    print("Makine ısınıyor... (zil çalmasın diye yavaş)")
    time.sleep(2)
    
    siir = siir_uret()
    print("\n" + siir)
    print("\n" + "=" * 50)
    print("Şiir bitti. Komşu hâlâ açmadıysa sorun yok.")
    print("Zil çalmadı. Özgür kaldık.")
    print("=" * 50)

if __name__ == "__main__":
    main()
