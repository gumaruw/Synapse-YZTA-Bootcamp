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
Prototip geliştirme için kullanılan Kaggle notebook: [Synapse Prototype](https://www.kaggle.com/code/synapseproject/synapse-medical-analogy-generator)

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
