# Synapse

Synapse, doktorların karmaşık tıbbi konuları hastalara (özellikle çocuklar, yaşlılar veya sağlık okuryazarlığı düşük bireylere) anlatmalarına yardımcı olmak için Google Gemini AI kullanarak kişiselleştirilmiş analojiler, metaforlar ve görsel hikaye fikirleri üreten bir web uygulamasıdır.  

---

## İçindekiler
1. [Takım Bilgileri](#takım-bilgileri)
2. [Hedef Kitle](#hedef-kitle)
3. [Teknolojiler](#teknolojiler)
4. [Proje Özellikleri](#proje-özellikleri)
5. [Dosya Yapısı](#dosya-yapısı)
6. [Kurulum ve Çalıştırma](#kurulum-ve-çalıştırma)
7. [Sprint Yapısı](#sprint-yapısı)
8. [Demo ve Çıktılar](#demo-ve-çıktılar)
9. [Belgeler](#belgeler)

---

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

## Hedef Kitle
- Doktorlar
- Tıp Fakültesi Öğrencileri
- Sağlık Çalışanları

## Teknolojiler
- **Backend:** Python, FastAPI
- **Frontend:** Streamlit
- **AI/ML:** Google Gemini API
- **Development:** Kaggle Notebooks
- **Proje Yönetimi:** Trello

## Proje Özellikleri
### Ana Modüller
- **Analoji Modülü:** Karmaşık tıbbi konuları basit analojilerle açıklama
- **Görsel Hikaye Modülü:** Çizim ve hikaye önerileri
- **Kişiselleştirme:** Hasta yaşı, ilgi alanları ve durumuna göre özelleştirme
- **Kaçınılması Gereken Kelimeler:** Hassas kelimeler için alternatif öneriler

### Teknik Özellikler
- **AI Entegrasyonu:** Google Gemini 1.5 Flash
- **Web Arayüzü:** Streamlit
- **Dil:** Python
- **Responsive Tasarım:** Mobil ve desktop uyumlu

## Dosya Yapısı 
synapse/  
├── streamlit_app.py       # Ana uygulama  
├── requirements.txt       # Python paketleri  
├── .env                  # API anahtarları   
├── config.py             # Yapılandırma dosyası  

## Sprint Yapısı
### Sprint 1 (20.06.2025 - 06.07.2025)
- Kaggle ortamında temel prototype geliştirme
- Gemini API entegrasyonu
- Temel analoji üretimi fonksiyonalitesi

### Sprint 2 (07.07.2025 - 20.07.2025)
- Streamlit web arayüzü geliştirme
- Kullanıcı deneyimi iyileştirmeleri
- Çoklu modül entegrasyonu

### Sprint 3 (21.07.2025 - 03.08.2025)
- UI/UX geliştirmeleri
- Test ve optimizasyon
- Final demo hazırlığı

## Kurulum ve Çalıştırma

```bash
pip install streamlit google-generativeai python-dotenv
```

```bash
git clone https://github.com/gumaruw/YZTA-Bootcamp-Synapse.git
cd YZTA-Bootcamp-Synapse
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

## Belgeler
[Sprint_Details.md](Sprint_Details.md)
[Product Backlog](Product_Backlog.md)
