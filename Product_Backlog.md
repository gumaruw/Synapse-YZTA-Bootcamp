# Synapse - Product Backlog

## Proje Genel Bilgileri
- **Proje Adı:** Synapse - Yapay Zeka Destekli Medikal Analoji Üreteci
- **Takım:** YZTA-Bootcamp-Grup-134
- **Toplam Sprint:** 3
- **Proje Süresi:** 6 hafta

## Product Backlog Items

### Epic 1: Core AI Integration
**Priorite:** High | **Puan:** 100

| User Story | Kabul Kriterleri | Sprint | Puan | Durum |
|------------|------------------|--------|------|-------|
| Doktor olarak, tıbbi bir konuyu girdiğimde AI'dan analoji almak istiyorum | - Gemini API entegrasyonu<br>- Başarılı API çağrısı<br>- Anlamlı analoji üretimi | 1 | 30 | ✅ |
| Doktor olarak, hasta profilini belirleyerek kişiselleştirilmiş analoji almak istiyorum | - Yaş, cinsiyet, ilgi alanı girdisi<br>- Profil bazlı analoji özelleştirme | 1 | 20 | ✅ |

### Epic 2: User Interface Development
**Priorite:** High | **Puan:** 80

| User Story | Kabul Kriterleri | Sprint | Puan | Durum |
|------------|------------------|--------|------|-------|
| Doktor olarak, kolay kullanılabilir bir web arayüzü istiyorum | - Streamlit arayüzü<br>- Form giriş alanları<br>- Sonuç görüntüleme | 2 | 25 | ✅ |
| Doktor olarak, farklı modülleri (analoji, hikaye, kelime) seçebilmek istiyorum | - Modül seçim arayüzü<br>- Çoklu çıktı görüntüleme | 2 | 20 | ✅ |
| Doktor olarak, üretilen içeriği kolayca kopyalayabilmek istiyorum | - Kopyalama butonu<br>- Metin formatı | 2 | 15 | ✅ |

### Epic 3: Content Modules
**Priorite:** Medium | **Puan:** 70

| User Story | Kabul Kriterleri | Sprint | Puan | Durum |
|------------|------------------|--------|------|-------|
| Doktor olarak, görsel hikaye önerileri almak istiyorum | - Hikaye taslağı üretimi<br>- Adım adım çizim önerileri | 2 | 20 | ✅ |
| Doktor olarak, kaçınılması gereken kelimeler hakkında uyarı almak istiyorum | - Hassas kelime tespiti<br>- Alternatif kelime önerileri | 3 | 15 | ✅ |
| Doktor olarak, farklı yaş grupları için uygun dil kullanmak istiyorum | - Yaş grubuna göre dil adaptasyonu<br>- Kelime karmaşıklığı ayarı | 3 | 20 | ✅ |

### Epic 4: Quality & Testing
**Priorite:** Medium | **Puan:** 50

| User Story | Kabul Kriterleri | Sprint | Puan | Durum |
|------------|------------------|--------|------|-------|
| Sistem yöneticisi olarak, hata durumlarında kullanıcıya bilgi verilmesini istiyorum | - API hata yakalama<br>- Kullanıcı dostu hata mesajları | 3 | 15 | ✅ |
| Doktor olarak, hızlı yanıt alabilmek istiyorum | - 5 saniye altı yanıt süresi<br>- Loading göstergeleri | 3 | 10 | ✅ |
| Doktor olarak, önceki sorguları görebilmek istiyorum | - Session içi geçmiş<br>- Tekrar kullanım özelliği | 3 | 10 | ✅ |

### Epic 5: Documentation & Demo
**Priorite:** High | **Puan:** 40

| User Story | Kabul Kriterleri | Sprint | Puan | Durum |
|------------|------------------|--------|------|-------|
| Takım olarak, proje dokümantasyonu hazırlamak istiyoruz | - README.md<br>- Teknik dokümantasyon | 1,2,3 | 20 | ✅ |
| Takım olarak, demo sunumu hazırlamak istiyoruz | - Demo video<br>- Sunum materyali | 3 | 20 | ✅ |

## Sprint Dağılımı

### Sprint 1 (20.06.2025 - 06.07.2025)
**Hedef:** Teknik fizibilite kanıtlama
**Toplam Puan:** 70
- Gemini API entegrasyonu (30 puan)
- Temel analoji üretimi (20 puan)
- Kaggle prototype (20 puan)

### Sprint 2 (07.07.2025 - 20.07.2025)
**Hedef:** Web arayüzü geliştirme
**Toplam Puan:** 80
- Streamlit arayüzü (25 puan)
- Modül seçimi (20 puan)
- Görsel hikaye modülü (20 puan)
- Kopyalama özelliği (15 puan)

### Sprint 3 (21.07.2025 - 03.08.2025)
**Hedef:** Kalite ve demo hazırlığı
**Toplam Puan:** 90
- UI/UX iyileştirmeleri (20 puan)
- Hata yönetimi (15 puan)
- Kelime uyarı sistemi (15 puan)
- Yaş grubuna göre dil (20 puan)
- Session geçmişi (10 puan)
- Demo hazırlığı (20 puan)

## Toplam Proje Puanı: 240 Puan

## Definition of Done
- [x] Kod GitHub'da commit edildi
- [x] Fonksiyonellik test edildi
- [x] Dokümantasyon güncellendi
- [ ] Sprint review'da demo yapıldı
- [x] Sprint retrospective'de değerlendirildi
