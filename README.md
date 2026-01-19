# OSOP - Çoklu Veritabanı Yönetim Aracı

Bu proje, Açık Kaynak İşletim Sistemi Projesi (OSOP) dersi kapsamında hazırlanmıştır.

## 🚀 Proje Hakkında
Bu araç; MySQL, PostgreSQL ve SQLite veritabanlarını Docker konteynerleri kullanarak hızlıca kurmayı ve yönetmeyi sağlar.

## 📂 Klasör Yapısı
- **docs/**: Kullanım kılavuzları.
- **researchs/**: Veritabanı teknolojileri üzerine araştırmalar.
- **specs/**: Sistem analizi ve gereksinim dökümanları.
- **src/**: Uygulamanın Python kaynak kodları.

## 🚀 Özellikler ve Teknik Gereksinimler (Specs)

Hocanın Adım 8/9 yönergesine uygun olarak projeye dahil edilen özellikler:

* **Otomatik Kontrol Yeteneği (Self-Check):** Uygulama başlatıldığında sistemde Docker Engine'in yüklü ve çalışır durumda olup olmadığını otomatik olarak denetler.
* **Otomatik Test Yeteneği:** Seçilen veritabanı konteynerının başarıyla oluşturulup oluşturulmadığını ve servislerin yanıt verip vermediğini test eder.
* **Modern Tasarım Standartları:** Terminal üzerinde kullanıcı dostu, renkli ve kategorize edilmiş bir menü yapısı sunar.
* **JSON Meta Veri Desteği:** Proje bilgileri `specs/proje_bilgisi.json` dosyası üzerinden standartlaştırılmış bir formatta sunulmaktadır.

## 🛠️ Kurulum
1. Bilgisayarınızda Python ve Docker Desktop kurulu olmalıdır.
2. Terminale `python src/main.py` yazarak başlatabilirsiniz.

"Bu araştırmalar Gemini kullanılarak doğrulanmıştır"

**Hazırlayan:** [Mikayil Hakkı Çakır]