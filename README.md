# YZTA Bootcamp Grup 134 - Synapse 

## Takım Bilgileri
- **Takım Adı:** YZTA Bootcamp Grup 134
- **Proje Adı:** Synapse - Yapay Zeka Destekli Medikal Analoji Üreteci

### Takım Üyeleri
| İsim | Rol |
|------|-----|
| Hasan BUDAK | Product Owner, Scrum Master, Developer |
| Cemre DAĞ | Developer,Product Owner |
| Yusuf Sait SAKOĞLU | Developer |
| Aydan KAYA | Developer |

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
### 🎯 Ana Modüller
- **Analoji Modülü:** Karmaşık tıbbi konuları basit analojilerle açıklama
- **Görsel Hikaye Modülü:** Çizim ve hikaye önerileri
- **Kişiselleştirme:** Hasta yaşı, ilgi alanları ve durumuna göre özelleştirme
- **Kaçınılması Gereken Kelimeler:** Hassas kelimeler için alternatif öneriler

### 🔧 Teknik Özellikler
- **AI Entegrasyonu:** Google Gemini 1.5 Flash
- **Web Arayüzü:** Streamlit
- **Dil:** Python
- **Responsive Tasarım:** Mobil ve desktop uyumlu

synapse/
├── streamlit_app.py       # Ana uygulama
├── requirements.txt       # Python paketleri
├── .env                  # API anahtarları 
├── config.py             # Yapılandırma dosyası

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
git clone https://github.com/gumaruw/YZTA-Bootcamp-Grup-134.git
cd YZTA-Bootcamp-Grup-134
```

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
```

```bash
pip install -r requirements.txt
```

- API key from https://aistudio.google.com/
- add it to the .env
 
```bash
python -m streamlit run streamlit_app.py
```

## Proje Yönetimi
- **Sprint Planning:** Trello Board
- **Daily Scrum:** Günlük ilerleme takibi
- **Sprint Review:** Sprint sonunda demo ve değerlendirme
- **Sprint Retrospective:** Süreç iyileştirmeleri

## Demo ve Çıktılar
- **Web Uygulaması:** Streamlit tabanlı interaktif arayüz
- **API Entegrasyonu:** Gemini AI ile başarılı entegrasyon
- **Analoji Örnekleri:** Diyabet, kırık kemik, kemoterapi gibi konular için üretilen analojiler

 ---------------------------------------------------------------------------------------------------------------------------------------------------------

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

---------------------------------------------------
SYNAPSE PROJESİ - DAILY SCRUM TOPLANTI KAYDI
---------------------------------------------------
Tarih: 24.06.2025
Sprint: 1. Sprint, 5. Gün
Katılımcılar: Hasan BUDAK (Scrum Master), Cemre Dağ, Yusuf Sait Sakoğlu
---------------------------------------------------

### GÜNCELLEMELER ###

1. Hasan BUDAK (Scrum Master):
   - Dün ne yaptım?: Projenin GitHub reposunu ve Jira panosunu oluşturdum. Sprint 1'in ana hedeflerini panoya görev olarak ekledim.
   - Bugün ne yapacağım?: Ekibin Kaggle ve Google AI Studio erişimlerinde bir sorun olup olmadığını kontrol edeceğim. Gemini API anahtarının nasıl güvenli saklanacağı üzerine bir araştırma yapacağım.
   - Herhangi bir engelleyici var mı?: Şimdilik yok, planlama aşamasındayız.

2. Cemre DAĞ (Developer):
   - Dün ne yaptım?: Sprint 1 hedeflerini ve Kaggle'da nasıl bir notebook yapısı kuracağımızı planladım.
   - Bugün ne yapacağım?: Boş bir Kaggle Notebook oluşturup, temel Python kütüphanelerini import ederek ve dosya yapısını planlayarak projeye teknik olarak başlayacağım.
   - Herhangi bir engelleyici var mı?: Yok.

3. Yusuf Sait SAKOĞLU (Developer):
   - Dün ne yaptım?: "Analoji üretimi" için Gemini'nin yeteneklerini araştırdım. Prompt'un hangi girdileri (yaş, ilgi alanı vb.) alması gerektiği üzerine beyin fırtınası yaptım.
   - Bugün ne yapacağım?: İlk ve en basit analoji senaryosu ("kırık kemik") için bir prompt taslağı (v0.1) yazmaya başlayacağım.
   - Herhangi bir engelleyici var mı?: Yok.

### ALINAN KARARLAR / SONRAKİ ADIMLAR ###
- Ekip, ilk olarak sadece tek bir senaryo üzerinde çalışarak API bağlantısını kurmaya odaklanma kararı aldı.


---------------------------------------------------
SYNAPSE PROJESİ - DAILY SCRUM TOPLANTI KAYDI 2
---------------------------------------------------
Tarih: 28.06.2025
Sprint: 1. Sprint, 9. Gün
Katılımcılar: Hasan BUDAK (Scrum Master), Cemre Dağ, Yusuf Sait Sakoğlu
---------------------------------------------------

### GÜNCELLEMELER ###

1. Hasan BUDAK (Scrum Master):
   - Dün ne yaptım?: Ekibin karşılaştığı API yetkilendirme sorununu çözmek için Cemre ve Yusuf'a destek oldum. Sorunun Kaggle Secrets'ın senkronizasyonundan kaynaklandığını tespit ettik ve çözdük.
   - Bugün ne yapacağım?: Ekibin sorunsuz çalıştığından emin olduktan sonra, projenin `README.md` dosyasını son haline getirmek için Cemre'ye destek olacağım.
   - Herhangi bir engelleyici var mı?: Engelleyici sorun çözüldü.

2. Cemre DAĞ (Developer):
   - Dün ne yaptım?: Hasan'ın desteğiyle API yetkilendirme sorununu aştık ve Gemini'ye ilk başarılı isteği gönderdik. "200 OK" yanıtını aldık.
   - Bugün ne yapacağım?: Yusuf'un hazırladığı v1 prompt'unu kullanarak ilk anlamlı analoji çıktısını üreten kodu Kaggle Notebook'a ekleyeceğim.
   - Herhangi bir engelleyici var mı?: Artık yok.

3. Yusuf Sait SAKOĞLU (Developer):
   - Dün ne yaptım?: API bağlantısı beklenirken, farklı senaryolar için prompt taslakları üzerinde çalıştım.
   - Bugün ne yapacağım?: Cemre'nin alacağı ilk analoji çıktısını inceleyeceğim. Çıktının tonuna ve yaratıcılığına göre prompt'u iyileştirmek için (v1.1) düzenlemeler yapacağım.
   - Herhangi bir engelleyici var mı?: Yok, heyecanla çıktıyı bekliyorum.

### ALINAN KARARLAR / SONRAKİ ADIMLAR ###
- İlk başarılı analoji çıktısının ekran görüntüsü alınacak ve sprint raporu için saklanacak.
- Cemre, `README.md` dosyasını tamamlayacak.

---------------------------------------------------
SYNAPSE PROJESİ - DAILY SCRUM TOPLANTI KAYDI 3
---------------------------------------------------
Tarih: 05.07.2025
Sprint: 1. Sprint, 16. Gün
Katılımcılar: Hasan BUDAK (Scrum Master), Cemre Dağ, Yusuf Sait Sakoğlu
---------------------------------------------------

### GÜNCELLEMELER ###

1. Hasan BUDAK (Scrum Master):
   - Dün ne yaptım?: Sprint 1 Raporu için gerekli olan tüm başlıkları ve içerikleri bir araya getirdim. Ekibin hazırladığı ekran görüntülerini ve çıktıları rapora ekledim.
   - Bugün ne yapacağım?: Sprint 1 Raporu'nun son okumasını yapacağım ve ekibin onayıyla GitHub'a yükleyeceğim. Sprint 2'nin Jira panosunu hazırlamaya başlayacağım.
   - Herhangi bir engelleyici var mı?: Yok, sprint hedeflerine ulaştık.

2. Cemre DAĞ (Developer):
   - Dün ne yaptım?: Kaggle Notebook'unu temizledim, kodlara yorum satırları ekleyerek daha anlaşılır hale getirdim. Jira panosundaki tüm görevlerin "Tamamlandı" olarak işaretlenmesini sağladım.
   - Bugün ne yapacağım?: Sprint raporu için Jira panosunun ve Kaggle Notebook'un final ekran görüntülerini alıp Hasan'a ileteceğim. Sprint 2 için Streamlit kurulumunu araştırmaya başlayacağım.
   - Herhangi bir engelleyici var mı?: Yok.

3. Yusuf Sait SAKOĞLU (Developer):
   - Dün ne yaptım?: Sprint 1'de geliştirdiğimiz prompt'un son halini (v1.2) ve nasıl çalıştığını anlatan kısa bir teknik doküman hazırladım.
   - Bugün ne yapacağım?: Hazırladığım bu teknik özeti, `README.md` dosyasına veya sprint raporuna eklenmesi için Hasan'a göndereceğim. Sprint 2'deki çoklu modül (hikaye, kelimeler) için prompt yapısını düşünmeye başlayacağım.
   - Herhangi bir engelleyici var mı?: Yok.

### ALINAN KARARLAR / SONRAKİ ADIMLAR ###
- Sprint 1 Raporu bugün (05.07) gün sonuna kadar tamamlanıp GitHub'a yüklenecek.
- Sprint 1 resmi olarak başarılı kabul edildi.



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# Synapse Projesi - Sprint 2 Değerlendirme Raporu

**Rapor Tarihi:** 20.07.2025  
**Sprint Dönemi:** 07.07.2025 - 20.07.2025  
**Takım:** YZTA Bootcamp Grup 134

---

## 1. Yönetici Özeti
Bu rapor, "Synapse" projesinin ikinci sprint dönemindeki hedeflerini, ulaşılan başarıları ve stratejik kararları özetlemektedir. Sprint 1'de teknik fizibilitesi kanıtlanan çekirdek yapay zeka fonksiyonelliği, bu sprint'in ana hedefi doğrultusunda, kullanıcıların doğrudan etkileşime geçebileceği, modern ve interaktif bir web uygulamasına başarıyla dönüştürülmüştür. Sprint sonunda, projenin temel modüllerini içeren ve çalışan bir web uygulaması (Minimum Viable Product - MVP) ortaya konmuştur.

## 2. Sprint Notları ve Stratejik Kararlar
### Ekip Genişlemesi
Sprint 2'nin başında ekibimize Aydan Kaya'nın da "Developer" rolüyle katılmasıyla proje geliştirme kapasitemiz artırılmıştır. Yeni görev dağılımı, web arayüzü ve arka plan süreçlerinin paralel olarak ilerletilmesine olanak tanımıştır.

### Teknoloji Seçimi
Kaggle üzerinde doğrulanan temel mantığın kullanıcıya sunulması için, hızlı prototipleme ve kolay entegrasyon imkanları sunan **Streamlit** framework'ü web arayüzü için stratejik olarak tercih edilmiştir.

### Fonksiyonel Geliştirme
Proje, tek bir analoji üretiminden çıkarılarak; **Analoji Modülü**, **Görsel Hikaye Modülü** ve **Kelime Uyarı Modülü**'nü içeren çoklu modül yapısına kavuşturulmuştur. Bu karar, ürünün değer önerisini zenginleştirmiştir.

### Proje Yönetimi
Görev takibi ve sprint planlaması için Trello panosu, teknik problemlerin takibi için ise GitHub Issues aktif olarak kullanılmaya devam edilmiştir.

## 3. Performans Değerlendirmesi: Puanlama ve Gerçekleşme
- **Sprint İçinde Tamamlanması Öngörülen Puan:** 80 Puan
- **Sprint Sonunda Tamamlanan Puan:** 80 Puan (%100 Tamamlanma)
- **Tahmin Mantığı:** Puanlama, bu sprint'in odak noktası olan web arayüzünün geliştirilmesi, temel modüllerin entegrasyonu ve kullanıcı deneyiminin başlangıç seviyesinde optimize edilmesi gibi kritik görevlere ağırlık verilerek yapılmıştır. Tüm hedeflere tam olarak ulaşılmıştır.

## 4. Proje Yönetimi ve Süreç
### Takım Koordinasyonu
Ekibe yeni katılan üyemizle birlikte görev dağılımı yeniden planlanmış, günlük scrum toplantıları ile ekip içi senkronizasyon ve bilgi akışı en üst düzeyde tutulmuştur.

### Sprint Süreci
1. Sprint 2 hedeflerinin ve görevlerinin Trello panosuna aktarılması.
2. Streamlit ile temel arayüz tasarımının ve layout'unun oluşturulması.
3. Sprint 1'deki Gemini API mantığının Streamlit backend'ine entegre edilmesi.
4. Çoklu modüllerin (Analoji, Hikaye, Kelimeler) arayüze eklenmesi ve API ile ilişkilendirilmesi.
5. Kullanıcı girdilerine (yaş, ilgi alanı) göre kişiselleştirme özelliklerinin geliştirilmesi.
6. Session state (oturum yönetimi) kullanılarak temel kullanıcı geçmişi takibinin sağlanması.

## 5. Proje Yönetim Panosu (Sprint Board)
Sprint boyunca görev takibi için Trello panosu aktif olarak kullanılmıştır. Haftalık demolar ve günlük ilerleme takibi bu pano üzerinden yönetilmiştir.

## 6. Ürün Durumu ve Somut Çıktılar
Sprint 2 sonunda ortaya çıkan ürün, canlı olarak test edilebilen, interaktif bir Streamlit web uygulamasıdır.

- **İşlevsellik:** Uygulama, kullanıcının kenar çubuğundan tıbbi konu, anahtar kavram, hasta yaşı ve ilgi alanı gibi bilgileri girmesine olanak tanır. "Üret" butonuna basıldığında, uygulama Gemini API'sine istek gönderir ve üretilen Analoji, Görsel Hikaye ve Kelime Önerilerini arayüzde eş zamanlı olarak gösterir.
- **Kullanıcı Deneyimi:** Arayüz, kullanıcıya anlık geri bildirimler (progress bar) sunar ve modern bir tasarıma sahiptir. Ayrıca, responsive yapısı sayesinde mobil cihazlarda da kullanılabilir.
<img width="1109" height="790" alt="Ekran Resmi 2025-07-20 14 11 52" src="https://github.com/user-attachments/assets/de459e71-df0f-4d1e-8d3b-f434a61b3921" />



## 7. Sprint Değerlendirmesi (Sprint Review)
Sprint sonunda yapılan değerlendirmede, projenin çalışan bir MVP (Minimum Viable Product) seviyesine ulaştığı teyit edilmiştir. Kullanıcı dostu arayüz, çoklu modüllerin sorunsuz çalışması ve hızlı yanıt süresi gibi özellikler başarılı bulunmuştur. Sprint 3 için öncelik, mevcut ürünün kalitesini artırmak, kapsamlı hata yönetimi eklemek ve final demoya hazırlık yapmak olarak belirlenmiştir.

## 8. Geriye Dönük Değerlendirme (Sprint Retrospective)
### Güçlü Yönler
- Streamlit seçimi, geliştirme sürecini ciddi anlamda hızlandıran doğru bir teknoloji kararıydı.
- Modüler yapı, gelecekteki geliştirmeleri ve bakımı kolaylaştıracak sağlam bir temel oluşturdu.
- Ekip içi iletişim ve koordinasyon, yeni üyenin katılımına rağmen mükemmel seviyedeydi.

### Gelişim Alanları
- API'den gelebilecek olası hataların yönetimi (Error Handling) daha kapsamlı hale getirilmeli.
- Kullanıcıların daha fazla hasta profili (örn: yaşlı, farklı kültürel arkaplan) seçebilmesi için seçenekler artırılmalı.
- Kullanıcıların doğrudan geri bildirimde bulunabileceği basit bir mekanizma eklenebilir.

## 9.Proje Çıktısı
<img width="633" height="749" alt="Ekran Resmi 2025-07-20 14 35 58" src="https://github.com/user-attachments/assets/a26daef5-d63d-4a1c-a20d-042d344a96b7" />






### SYNAPSE PROJESİ - DAILY SCRUM TOPLANTI KAYDI 1

**Tarih:** 09.07.2025  
**Sprint:** 2. Sprint, 3. Gün  
**Katılımcılar:** Hasan BUDAK (Scrum Master), Cemre Dağ, Yusuf Sait Sakoğlu, Aydan Kaya

---

#### GÜNCELLEMELER

1.  **Hasan BUDAK (Scrum Master):**
    * **Dün ne yaptım?:** Sprint 2'nin tüm görevlerini Jira panosuna aktardım. Ekibe yeni katılan Aydan Kaya'nın proje reposuna ve Jira panosuna erişimini sağladım. Ekip ile bir tanışma ve görev dağılımı toplantısı organize ettim.
    * **Bugün ne yapacağım?:** Streamlit arayüzü için temel bir wireframe (taslak çizim) hazırlayacağım. Cemre ve Aydan'ın görevlerini senkronize etmelerine yardımcı olacağım.
    * **Herhangi bir engelleyici var mı?:** Şimdilik yok.

2.  **Cemre DAĞ (Developer):**
    * **Dün ne yaptım?:** Sprint 1'deki temel analoji üretme fonksiyonunu, Streamlit'te çalışacak şekilde yeniden düzenledim. `requirements.txt` dosyasını güncelledim.
    * **Bugün ne yapacağım?:** Streamlit üzerinde ana uygulama iskeletini (`streamlit_app.py`) oluşturacağım. Başlık, kenar çubuğu (sidebar) gibi temel layout bileşenlerini ekleyeceğim.
    * **Herhangi bir engelleyici var mı?:** Yok.

3.  **Yusuf Sait SAKOĞLU (Developer):**
    * **Dün ne yaptım?:** Sprint 1'de geliştirdiğimiz prompt'u, yeni eklenecek "Görsel Hikaye" ve "Kelime Uyarıları" modüllerini de kapsayacak şekilde nasıl genişletebileceğimizi araştırdım.
    * **Bugün ne yapacağım?:** Gemini'ye tek bir istekte üç farklı modül için çıktı ürettirecek yeni bir prompt (v2.0) taslağı hazırlayacağım.
    * **Herhangi bir engelleyici var mı?:** Prompt'un karmaşıklığı arttıkça, çıktının tutarlılığını sağlamak zorlayıcı olabilir ama şu an bir engel yok.

4.  **Aydan KAYA (Developer):**
    * **Dün ne yaptım?:** Proje dokümantasyonunu ve Sprint 1 çıktılarını inceleyerek projeyi anladım. Gerekli kurulumları kendi ortamımda tamamladım.
    * **Bugün ne yapacağım?:** Cemre ile koordineli olarak, kullanıcıdan girdileri (Tıbbi Konu, Yaş, İlgi Alanı) alacağımız Streamlit form bileşenlerini kenar çubuğuna eklemek üzerine çalışacağım.
    * **Herhangi bir engelleyici var mı?:** Yok, ekibe adapte oluyorum.

#### ALINAN KARARLAR / SONRAKİ ADIMLAR
* Cemre ve Aydan, arayüzün temel yapısı üzerinde birlikte çalışacaklar.
* Yusuf, yeni prompt yapısını tamamladığında test için ekiple paylaşacak.

---

### SYNAPSE PROJESİ - DAILY SCRUM TOPLANTI KAYDI 2

**Tarih:** 15.07.2025  
**Sprint:** 2. Sprint, 9. Gün  
**Katılımcılar:** Hasan BUDAK (Scrum Master), Cemre Dağ, Yusuf Sait Sakoğlu, Aydan Kaya

---

#### GÜNCELLEMELER

1.  **Hasan BUDAK (Scrum Master):**
    * **Dün ne yaptım?:** Ekibin karşılaştığı Streamlit "session state" sorununu araştırdım ve birkaç çözüm önerisi sundum. Jira panosundaki tamamlanan görevleri güncelledim.
    * **Bugün ne yapacağım?:** Sprint 2 raporu için taslak oluşturmaya başlayacağım. Ekibin herhangi bir ek ihtiyacı olup olmadığını kontrol edeceğim.
    * **Herhangi bir engelleyici var mı?:** Session state sorunu çözüldüğü için şu an bir engelleyici yok.

2.  **Cemre DAĞ (Developer):**
    * **Dün ne yaptım?:** Yusuf'un hazırladığı v2.0 prompt'u kullanarak Gemini'den gelen çoklu modül çıktısını başarıyla aldım ve Streamlit arayüzünde ham olarak yazdırdım.
    * **Bugün ne yapacağım?:** Gelen bu çıktıyı (Analoji, Hikaye, Kelimeler) parse edip arayüzdeki ilgili kartlara veya bölümlere düzgün bir şekilde yerleştireceğim.
    * **Herhangi bir engelleyici var mı?:** Yok.

3.  **Yusuf Sait SAKOĞLU (Developer):**
    * **Dün ne yaptım?:** Gelen ilk test çıktılarına göre v2.0 prompt'unda iyileştirmeler yaptım. Özellikle "Görsel Hikaye" modülünün adımlarını daha net vermesi için prompt'u düzenledim (v2.1).
    * **Bugün ne yapacağım?:** Farklı hasta profilleri ve tıbbi konular için prompt'un tutarlılığını test etmeye devam edeceğim. Kenar durumları (edge cases) arıyorum.
    * **Herhangi bir engelleyici var mı?:** Yok.

4.  **Aydan KAYA (Developer):**
    * **Dün ne yaptım?:** Kullanıcı "Analoji Üret" butonuna bastığında bir yüklenme göstergesi (progress bar) ekledim. Ayrıca, Hasan'ın desteğiyle kullanıcı girdilerinin bir sonraki istek için hafızada tutulmasını sağlayan session state sorununu çözdük.
    * **Bugün ne yapacağım?:** Arayüzün görsel tasarımını iyileştirmek için basit CSS düzenlemeleri yapacağım. Buton ve girdi alanlarının stillerini güncelleyeceğim.
    * **Herhangi bir engelleyici var mı?:** Yok.

#### ALINAN KARARLAR / SONRAKİ ADIMLAR
* Çıktıların arayüze yerleştirilmesi tamamlandığında tüm ekip birlikte bir kullanıcı deneyimi testi yapacak.

---

### SYNAPSE PROJESİ - DAILY SCRUM TOPLANTI KAYDI 3

**Tarih:** 19.07.2025  
**Sprint:** 2. Sprint, 13. Gün  
**Katılımcılar:** Hasan BUDAK (Scrum Master), Cemre Dağ, Yusuf Sait Sakoğlu, Aydan Kaya

---

#### GÜNCELLEMELER

1.  **Hasan BUDAK (Scrum Master):**
    * **Dün ne yaptım?:** Sprint 2 raporunun taslağını tamamladım ve ekibin incelemesi için paylaştım. Trello'daki tüm görevlerin durumunu son kez kontrol ettim.
    * **Bugün ne yapacağım?:** Ekip üyelerinden gelen geri bildirimlerle Sprint 2 raporuna son halini vereceğim. Sprint 3'ün Jira panosunu hazırlamaya başlayacağım.
    * **Herhangi bir engelleyici var mı?:** Yok, sprint hedeflerine ulaştık.

2.  **Cemre DAĞ (Developer):**
    * **Dün ne yaptım?:** Uygulamanın temel hata yönetimini (örn: API anahtarı yoksa uyarı ver) ekledim. Kodları temizledim ve yorum satırları ekleyerek daha anlaşılır hale getirdim. Jira panosundaki tüm görevlerin "Tamamlandı" olarak işaretlenmesini sağladım.
    * **Bugün ne yapacağım?:** Projenin son halinin ekran görüntülerini ve kısa bir ekran kaydını alıp Hasan'a ileteceğim. Sprint 3'te yapılacak UI/UX iyileştirmeleri için fikirleri not alacağım.
    * **Herhangi bir engelleyici var mı?:** Yok.

3.  **Yusuf Sait SAKOĞLU (Developer):**
    * **Dün ne yaptım?:** Geliştirdiğimiz prompt'un son halini (v2.2) ve nasıl çalıştığını anlatan kısa bir teknik dokümanı `README.md` dosyasına eklenmesi için hazırladım.
    * **Bugün ne yapacağım?:** Sprint 3'te eklenebilecek daha fazla kişiselleştirme seçeneği (örn: yaşlılar için farklı ilgi alanları) üzerine araştırma yapacağım.
    * **Herhangi bir engelleyici var mı?:** Yok.

4.  **Aydan KAYA (Developer):**
    * **Dün ne yaptım?:** Uygulamanın farklı ekran boyutlarında (mobil, tablet) düzgün görünmesi için responsive tasarım testleri yaptım ve gerekli CSS düzeltmelerini tamamladım.
    * **Bugün ne yapacağım?:** Uygulamadaki metinleri ve yardım bölümünü son kez gözden geçireceğim. Yazım hatası veya anlaşılmayan bir yer olup olmadığını kontrol edeceğim.
    * **Herhangi bir engelleyici var mı?:** Yok.

#### ALINAN KARARLAR / SONRAKİ ADIMLAR
* Sprint 2'nin tüm hedefleri başarıyla tamamlandı.
* Sprint raporu bugün gün sonuna kadar tamamlanacak.
* Ekip, Sprint 3'ün planlama toplantısı için hazırlıklara başlayacak.
