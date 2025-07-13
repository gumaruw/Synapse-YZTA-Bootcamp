import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

class Config:
    """Uygulama yapılandırma ayarları"""
    
    # API Ayarları
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    
    # Streamlit Ayarları
    STREAMLIT_SERVER_PORT = int(os.getenv('STREAMLIT_SERVER_PORT', 8501))
    STREAMLIT_SERVER_HEADLESS = os.getenv('STREAMLIT_SERVER_HEADLESS', 'true').lower() == 'true'
    
    # Gemini Model Ayarları
    GEMINI_MODEL = "gemini-1.5-flash"
    GENERATION_CONFIG = {
        "temperature": 0.7,
        "top_p": 0.9,
        "top_k": 40,
        "max_output_tokens": 1000,
    }
    
    # Uygulama Ayarları
    APP_NAME = "Synapse"
    APP_VERSION = "2.0"
    TEAM_NAME = "YZTA-Bootcamp-Grup-134"
    
    # Hasta Profili Seçenekleri
    AGE_GROUPS = [
        "0-5 yaş",
        "6-12 yaş", 
        "13-18 yaş",
        "19-65 yaş",
        "65+ yaş"
    ]
    
    INTEREST_AREAS = [
        "Arabalar",
        "Hayvanlar",
        "Spor",
        "Müzik",
        "Bahçıvanlık",
        "Teknoloji",
        "Yemek",
        "Kitaplar"
    ]
    
    # Örnek Tıbbi Konular
    SAMPLE_MEDICAL_TOPICS = [
        "Diyabet Tip 1 - Pankreasın insülin üretememesi",
        "Kırık kemik iyileşme süreci",
        "Kemoterapi tedavisi",
        "Astım nöbeti ve tedavisi",
        "Kalp krizi ve stent takma",
        "Böbrek taşı ve tedavisi",
        "Migren ağrısı ve tetikleyiciler",
        "Yüksek tansiyon ve diyet"
    ]
