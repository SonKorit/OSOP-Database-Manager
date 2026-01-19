print("--- OSOP VERİTABANI SİSTEMİ BAŞLATILIYOR ---")
import os

def menu():
    print("1- MySQL Kur")
    print("2- PostgreSQL Kur")
    print("3- Durumu Kontrol Et")
    secim = input("Seçiminiz: ")
    print(f"{secim} seçildi.")

if __name__ == "__main__":
    menu()