# YZTA-Bootcamp-Grup-134 - Synapse Projesi

## Takım Bilgileri
- **Takım Adı:** YZTA-Bootcamp-Grup-134
- **Proje Adı:** Synapse - Yapay Zeka Destekli Medikal Analoji Üreteci

### Takım Üyeleri
| İsim | Rol |
|------|-----|
| Hasan BUDAK | Product Owner, Scrum Master, Developer |
| Cemre Dağ | Developer, Product Owner, Scrum Master |
| Yusuf Sait Sakoğlu | Developer |

## Proje Açıklaması
Synapse, doktorların karmaşık tıbbi konuları hastalara (özellikle çocuklara, yaşlılara veya sağlık okuryazarlığı düşük bireylere) anlatmalarına yardımcı olmak için Google Gemini AI kullanarak kişiselleştirilmiş analojiler, metaforlar ve görsel hikaye fikirleri üreten bir web uygulamasıdır.

## Hedef Kitle
- Doktorlar
- Tıp Fakültesi Öğrencileri
- Sağlık Çalışanları

## Teknoloji Stack
- **Backend:** Python, FastAPI
- **Frontend:** Streamlit
- **AI/ML:** Google Gemini API
- **Development:** Kaggle Notebooks
- **Proje Yönetimi:** Trello

## Proje Özellikleri
- **Analoji Modülü:** Karmaşık tıbbi konuları basit analojilerle açıklama
- **Görsel Hikaye Modülü:** Çizim ve hikaye önerileri
- **Kişiselleştirme:** Hasta yaşı, ilgi alanları ve durumuna göre özelleştirme
- **Kaçınılması Gereken Kelimeler:** Hassas kelimeler için alternatif öneriler

## Sprint Yapısı
### Sprint 1 (20.06.2025 - 06.07.2025) ✅
- Kaggle ortamında temel prototype geliştirme
- Gemini API entegrasyonu
- Temel analoji üretimi fonksiyonalitesi

### Sprint 2 (07.07.2025 - 20.07.2025) ✅
- Streamlit web arayüzü geliştirme
- Kullanıcı deneyimi iyileştirmeleri
- Çoklu modül entegrasyonu

### Sprint 3 (21.07.2025 - 03.08.2025) ✅
- UI/UX geliştirmeleri
- Test ve optimizasyon
- Final demo hazırlığı

## Kurulum ve Çalıştırma

### Gereksinimler
```bash
pip install streamlit google-generativeai python-dotenv
```

### Çalıştırma
```bash
streamlit run app.py
```

### Kaggle Notebook
Prototip geliştirme için kullanılan Kaggle notebook: 

## Proje Yönetimi
- **Sprint Planning:** Trello Board
- **Daily Scrum:** Günlük ilerleme takibi
- **Sprint Review:** Sprint sonunda demo ve değerlendirme
- **Sprint Retrospective:** Süreç iyileştirmeleri

## Demo ve Çıktılar
- **Web Uygulaması:** Streamlit tabanlı interaktif arayüz
- **API Entegrasyonu:** Gemini AI ile başarılı entegrasyon
- **Analoji Örnekleri:** Diyabet, kırık kemik, kemoterapi gibi konular için üretilen analojiler

## Lisans
MIT License





# Proje Synapse - Sprint 1 Değerlendirme Raporu

Rapor Tarihi: 06.07.2025
Sprint Dönemi: 20.06.2025 - 06.07.2025

## 1. Yönetici Özeti

Bu rapor, "Synapse" projesinin ilk sprint dönemindeki hedefleri, ulaşılan başarıları ve stratejik kararları özetlemektedir. Bu dönemin ana hedefi, projenin temel hipotezi olan "yapay zekanın, karmaşık tıbbi konular için kişiselleştirilmiş analojiler üretebilmesi" fikrinin teknik fizibilitesini kanıtlamaktı. Sprint sonunda bu hedefe başarıyla ulaşılmış, projenin bir sonraki faza geçmesi için gerekli olan temel teknoloji ve altyapı doğrulanmıştır.

## 2. Sprint Notları ve Stratejik Kararlar

Platform Seçimi: Geliştirme ortamı olarak, donanımdan bağımsız çalışma esnekliği ve güçlü işlem kaynaklarına erişim imkanı sunması sebebiyle Kaggle platformu stratejik bir tercih olarak belirlenmiştir. Tüm prototip geliştirme ve test süreçleri Kaggle Notebook üzerinde yürütülmüştür.

Teknolojik Kilometre Taşı: Projenin çekirdeğini oluşturan Google Gemini (GenAI) API'si ile başarılı bir entegrasyon sağlanmış, yapay zeka modelinden anlamlı ve bağlama uygun çıktılar alınarak projenin en kritik teknik riski ortadan kaldırılmıştır.

Proje Yönetimi: Görev takibi ve sprint planlaması için Trello panosu aktif olarak kullanılarak projenin şeffaf ve düzenli bir şekilde ilerlemesi temin edilmiştir.

## 3. Performans Değerlendirmesi: Puanlama ve Gerçekleşme

Sprint İçinde Tamamlanması Öngörülen Puan: 50 Puan

Sprint Sonunda Tamamlanan Puan: 50 Puan

Tahmin Mantığı: Puanlama, projenin başlangıç aşamasındaki belirsizlikleri ve riskleri azaltmaya yönelik yapılmıştır. En yüksek puanlar, projenin devamlılığı için hayati önem taşıyan "API Entegrasyonu" ve "Temel Hipotezin Doğrulanması" gibi görevlere atanmış ve bu hedeflere tam olarak ulaşılmıştır.

## 4. Proje Yönetimi ve Süreç

Öz-yönetim ve Disiplinli Takip: Tek kişilik bir proje olması sebebiyle, günlük ilerleme takibi ve hedef odağını korumak amacıyla Trello panosu ve günlük görev listeleri etkin bir şekilde kullanılmıştır.

Sprint Süreci: Sprint, belirlenen iş akışına sadık kalınarak yürütülmüştür:

Geliştirme platformu olarak Kaggle'ın seçilmesi ve yapılandırılması.

Gemini API anahtarlarının temin edilip güvenli bir şekilde entegre edilmesi.

Belirlenmiş bir test senaryosu için ilk başarılı prompt (v1.0) mühendisliğinin tamamlanması.

Tüm sürecin ve sonuçların şeffaf bir şekilde Kaggle Notebook üzerinde belgelenmesi.

## 5. Proje Yönetim Panosu (Sprint Board)

Sprint boyunca görev takibi için kullanılan Trello panosu kullanılmıştır.

## 6. Ürün Durumu ve Somut Çıktılar

Sprint 1 sonunda ortaya çıkan ürün, tüm adımları ve çıktıları şeffaf bir şekilde belgelenmiş, çalıştırılabilir bir Kaggle Notebook'udur.

İşlevsellik: Notebook, önceden tanımlanmış bir tıbbi kavramı (örn: "kırık kemik") ve hasta profilini (örn: "8 yaşında çocuk") girdi olarak alır. Bu girdileri kullanarak Gemini API'sine bir istek gönderir ve yapay zeka tarafından üretilen özgün analojiyi bir çıktı hücresinde net bir şekilde yazdırır.

Doğrulanabilirlik: Notebook, heyetiniz veya herhangi bir teknik değerlendirici tarafından baştan sona çalıştırılarak sonuçların tekrarlanabilirliği teyit edilebilir. 

![WhatsApp Image 2025-07-07 at 20 52 49_ab9d90c9](https://github.com/user-attachments/assets/265c049f-83cf-4975-a5cf-bf9626873441)


## 7. Sprint Değerlendirmesi (Sprint Review)

Sprint sonunda yapılan değerlendirme sonucunda, projenin temel hipotezi olan "AI tabanlı yaratıcı analoji üretimi"nin teknik olarak mümkün olduğu ve başarılı sonuçlar verdiği teyit edilmiştir. Sprint 1 prototipi, projenin potansiyelini ve yenilikçi değerini somut bir şekilde ortaya koymuştur. Bu doğrultuda, Sprint 2 için stratejik karar, Kaggle üzerinde doğrulanan bu çekirdek mantığın, interaktif bir kullanıcı deneyimi sunacak web tabanlı bir arayüze (Streamlit vb.) taşınması olarak belirlenmiştir.

## 8. Geriye Dönük Değerlendirme (Sprint Retrospective)

Güçlü Yönler: Kaggle kullanımı, geliştirme sürecini ciddi anlamda hızlandırmış ve esneklik sağlamıştır. Prompt mühendisliğine odaklanmak, projenin en kritik parçasının sağlam bir temel üzerine oturmasını sağlamıştır.

Gelişim Alanları: API'den dönen yanıtların yapılandırılması (JSON formatı gibi) ve hata yönetimi, bir sonraki sprint'te odaklanılması gereken teknik konulardır.

## 9.Proje Prototip Çıktısı
<img width="902" alt="Ekran Resmi 2025-07-06 20 36 08" src="https://github.com/user-attachments/assets/1dce2f11-e98e-4f9b-a5db-71ab75ad8c2c" />





