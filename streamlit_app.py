import streamlit as st
import google.generativeai as genai
import os
from datetime import datetime
import time
import json
from typing import Dict, List, Optional
import random
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Dil desteği için çeviri sözlükleri
TRANSLATIONS = {
    "tr": {
        "page_title": "Synapse - Medikal Analoji Üreteci",
        "main_title": "🧠 Synapse",
        "subtitle": "Yapay Zeka Destekli Medikal Analoji Üreteci",
        "description": "Karmaşık tıbbi konuları basit analojilerle açıklayın",
        "settings": "⚙️ Ayarlar",
        "api_key_label": "Gemini API Key",
        "api_key_help": "Google AI Studio'dan aldığınız API anahtarını girin",
        "project_info": "📋 Proje Bilgileri",
        "team": "Takım",
        "sprint": "Sprint",
        "version": "Versiyon",
        "developers": "Geliştirici",
        "usage_stats": "📊 Kullanım İstatistikleri",
        "total_queries": "Toplam Sorgu",
        "active_session": "Aktif Oturum",
        "clear_history": "🗑️ Geçmişi Temizle",
        "analogy_generation": "🎯 Analoji Üretimi",
        "medical_topic": "📝 Tıbbi Konu",
        "medical_topic_placeholder": "Örn: Diyabet Tip 1 - Pankreasın insülin üretememesi",
        "medical_topic_help": "Hastaya açıklamak istediğiniz tıbbi konuyu detaylı olarak yazın",
        "patient_age": "👤 Hasta Yaşı",
        "patient_age_help": "Hastanın yaş grubunu seçin",
        "patient_interest": "🎨 İlgi Alanı",
        "patient_interest_help": "Hastanın ilgi alanını seçin",
        "analogy_settings": "🎨 Analoji Ayarları",
        "length": "Uzunluk",
        "length_help": "Analojinin uzunluğunu seçin",
        "detail_level": "Detay Seviyesi",
        "detail_help": "Ne kadar detaylı olacağını seçin",
        "tone": "Ton",
        "tone_help": "Analojinin tonunu seçin",
        "output_modules": "📚 Çıktı Modülleri",
        "generate_analogy": "🔄 Analoji Üret",
        "generate_story": "📖 Görsel Hikaye",
        "generate_warnings": "⚠️ Kelime Uyarıları",
        "submit_button": "🚀 Analoji Üret",
        "history_queries": "📚 Geçmiş Sorgular",
        "help_section": "❓ Yardım",
        "how_to_use": "Nasıl kullanılır?",
        "tips": "İpuçları:",
        "error_no_api": "❌ Lütfen önce API anahtarınızı girin!",
        "error_no_topic": "❌ Lütfen bir tıbbi konu girin!",
        "generating_analogy": "🔄 Analoji üretiliyor...",
        "generating_story": "📖 Görsel hikaye üretiliyor...",
        "generating_warnings": "⚠️ Kelime uyarıları üretiliyor...",
        "completed": "✅ Tamamlandı!",
        "error_occurred": "❌ Hata",
        "error_message": "Bir hata oluştu:",
        "no_history": "Henüz sorgu geçmişi yok.",
        "reuse_query": "Tekrar Kullan",
        "generated_analogy": "🎯 Üretilen Analoji",
        "visual_story_suggestion": "📖 Görsel Hikaye Önerisi",
        "word_usage_guide": "⚠️ Kelime Kullanım Rehberi",
        "copy_button": "Kopyala",
        "email_share": "E-posta ile Paylaş",
        "whatsapp_share": "WhatsApp"
    },
    "en": {
        "page_title": "Synapse - Medical Analogy Generator",
        "main_title": "🧠 Synapse",
        "subtitle": "AI-Powered Medical Analogy Generator",
        "description": "Explain complex medical topics with simple analogies",
        "settings": "⚙️ Settings",
        "api_key_label": "Gemini API Key",
        "api_key_help": "Enter your API key from Google AI Studio",
        "project_info": "📋 Project Info",
        "team": "Team",
        "sprint": "Sprint",
        "version": "Version",
        "developers": "Developers",
        "usage_stats": "📊 Usage Statistics",
        "total_queries": "Total Queries",
        "active_session": "Active Session",
        "clear_history": "🗑️ Clear History",
        "analogy_generation": "🎯 Analogy Generation",
        "medical_topic": "📝 Medical Topic",
        "medical_topic_placeholder": "Ex: Type 1 Diabetes - Pancreas not producing insulin",
        "medical_topic_help": "Write the medical topic you want to explain to the patient in detail",
        "patient_age": "👤 Patient Age",
        "patient_age_help": "Select the patient's age group",
        "patient_interest": "🎨 Interest Area",
        "patient_interest_help": "Select the patient's area of interest",
        "analogy_settings": "🎨 Analogy Settings",
        "length": "Length",
        "length_help": "Select the length of the analogy",
        "detail_level": "Detail Level",
        "detail_help": "Select how detailed it should be",
        "tone": "Tone",
        "tone_help": "Select the tone of the analogy",
        "output_modules": "📚 Output Modules",
        "generate_analogy": "🔄 Generate Analogy",
        "generate_story": "📖 Visual Story",
        "generate_warnings": "⚠️ Word Warnings",
        "submit_button": "🚀 Generate Analogy",
        "history_queries": "📚 Query History",
        "help_section": "❓ Help",
        "how_to_use": "How to use?",
        "tips": "Tips:",
        "error_no_api": "❌ Please enter your API key first!",
        "error_no_topic": "❌ Please enter a medical topic!",
        "generating_analogy": "🔄 Generating analogy...",
        "generating_story": "📖 Generating visual story...",
        "generating_warnings": "⚠️ Generating word warnings...",
        "completed": "✅ Completed!",
        "error_occurred": "❌ Error",
        "error_message": "An error occurred:",
        "no_history": "No query history yet.",
        "reuse_query": "Reuse",
        "generated_analogy": "🎯 Generated Analogy",
        "visual_story_suggestion": "📖 Visual Story Suggestion",
        "word_usage_guide": "⚠️ Word Usage Guide",
        "copy_button": "Copy",
        "email_share": "Share via Email",
        "whatsapp_share": "WhatsApp"
    }
}

# Dil seçenekleri
LANGUAGES = {
    "🇹🇷 Türkçe": "tr",
    "🇺🇸 English": "en"
}

# Yaş grupları ve ilgi alanları (çok dilli)
AGE_GROUPS = {
    "tr": ["0-5 yaş", "6-12 yaş", "13-18 yaş", "19-65 yaş", "65+ yaş"],
    "en": ["0-5 years", "6-12 years", "13-18 years", "19-65 years", "65+ years"]
}

INTEREST_AREAS = {
    "tr": ["Arabalar", "Hayvanlar", "Spor", "Müzik", "Bahçıvanlık", "Teknoloji", "Yemek", "Kitaplar"],
    "en": ["Cars", "Animals", "Sports", "Music", "Gardening", "Technology", "Food", "Books"]
}

# Analoji parametreleri (çok dilli)
ANALOGY_PARAMS = {
    "tr": {
        "length": ["kısa", "orta", "uzun"],
        "detail": ["genel", "detaylı"],
        "tone": ["resmi", "samimi", "çocuksu"]
    },
    "en": {
        "length": ["short", "medium", "long"],
        "detail": ["general", "detailed"],
        "tone": ["formal", "friendly", "childish"]
    }
}

# Sayfa yapılandırması
st.set_page_config(
    page_title="Synapse - Medikal Analoji Üreteci",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS stilleri (daha dinamik ve modern)
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2.5rem 1rem 2rem 1rem;
        border-radius: 16px;
        text-align: center;
        color: white;
        margin-bottom: 2.5rem;
        box-shadow: 0 6px 24px rgba(0,0,0,0.12);
        font-family: 'Segoe UI', 'Arial', sans-serif;
        letter-spacing: 1px;
    }
    .module-card, .result-card, .warning-card, .error-card, .story-card {
        background: #fff;
        padding: 1.7rem 1.2rem;
        border-radius: 14px;
        border-left: 5px solid #667eea;
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 18px rgba(102,126,234,0.07);
        transition: box-shadow 0.2s, transform 0.2s;
        position: relative;
    }
    .module-card:hover, .result-card:hover, .warning-card:hover, .error-card:hover, .story-card:hover {
        box-shadow: 0 8px 32px rgba(102,126,234,0.18);
        transform: translateY(-2px) scale(1.01);
    }
    .result-card h4, .story-card h4, .warning-card h4 {
        margin-top: 0;
        font-size: 1.3rem;
        color: #667eea;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .result-card h4:before { content: "🎯 "; }
    .story-card h4:before { content: "📖 "; }
    .warning-card h4:before { content: "⚠️ "; }
    .error-card h4:before { content: "❌ "; }
    .result-card p, .story-card p, .warning-card p {
        font-size: 1.1rem;
        color: #222;
        margin-bottom: 0.5rem;
    }
    .copy-share-bar {
        display: flex;
        gap: 0.7rem;
        margin-bottom: 0.7rem;
        margin-top: 0.2rem;
    }
    .copy-btn, .share-btn {
        padding: 0.45rem 1.1rem;
        border-radius: 6px;
        border: none;
        font-size: 1rem;
        font-weight: 500;
        cursor: pointer;
        transition: background 0.2s, color 0.2s, box-shadow 0.2s;
        box-shadow: 0 2px 8px rgba(102,126,234,0.07);
        outline: none;
    }
    .copy-btn { background: #667eea; color: #fff; }
    .copy-btn:hover { background: #4f5bd5; }
    .share-btn.mail { background: #28a745; color: #fff; }
    .share-btn.mail:hover { background: #218838; }
    .share-btn.wa { background: #25D366; color: #fff; }
    .share-btn.wa:hover { background: #128C7E; }
    .stTextInput, .stSelectbox, .stRadio, .stButton {
        margin-bottom: 0.7rem !important;
    }
    .stForm { margin-bottom: 2rem; }
    .stDivider { margin: 1.5rem 0; border-top: 2px dashed #667eea; }
</style>
""", unsafe_allow_html=True)

# Session state başlatma
if 'history' not in st.session_state:
    st.session_state.history = []
if 'api_key' not in st.session_state:
    st.session_state.api_key = None
if 'model' not in st.session_state:
    st.session_state.model = None
if 'language' not in st.session_state:
    st.session_state.language = "tr"

def get_text(key: str) -> str:
    """Dil çevirisi için yardımcı fonksiyon"""
    return TRANSLATIONS[st.session_state.language].get(key, key)

def create_animated_header():
    """Animasyonlu başlık oluştur"""
    colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c', '#4facfe', '#00f2fe']
    
    # Rastgele renk seç
    color1, color2 = random.sample(colors, 2)
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(90deg, {color1} 0%, {color2} 100%);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        animation: gradient 3s ease infinite;
    ">
        <h1 style="font-size: 3rem; margin-bottom: 0.5rem;">{get_text('main_title')}</h1>
        <p style="font-size: 1.2rem; margin-bottom: 0.5rem;">{get_text('subtitle')}</p>
        <p style="font-style: italic; opacity: 0.9;">{get_text('description')}</p>
    </div>
    
    <style>
    @keyframes gradient {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    </style>
    """, unsafe_allow_html=True)

def create_usage_chart():
    """Kullanım istatistikleri için dinamik grafik oluştur"""
    if not st.session_state.history:
        return
    
    # Son 10 sorgunun zaman dağılımını analiz et
    recent_queries = st.session_state.history[-10:]
    
    # Modül kullanım istatistikleri
    module_usage = {
        'analogy': sum(1 for q in recent_queries if 'analogy' in q.get('results', {})),
        'story': sum(1 for q in recent_queries if 'story' in q.get('results', {})),
        'warnings': sum(1 for q in recent_queries if 'warnings' in q.get('results', {}))
    }
    
    # Pasta grafik oluştur
    fig = go.Figure(data=[go.Pie(
        labels=[get_text('generate_analogy'), get_text('generate_story'), get_text('generate_warnings')],
        values=[module_usage['analogy'], module_usage['story'], module_usage['warnings']],
        hole=0.3,
        marker_colors=['#28a745', '#2196f3', '#ffc107']
    )])
    
    fig.update_layout(
        title=get_text('usage_stats'),
        showlegend=True,
        height=300
    )
    
    st.plotly_chart(fig, use_container_width=True)

def create_activity_timeline():
    """Aktivite zaman çizelgesi oluştur"""
    if len(st.session_state.history) < 2:
        return
    
    # Son 5 sorguyu al
    recent_queries = st.session_state.history[-5:]
    
    # Zaman damgalarını parse et
    times = []
    topics = []
    
    for query in recent_queries:
        try:
            time_obj = datetime.strptime(query['timestamp'], '%Y-%m-%d %H:%M:%S')
            times.append(time_obj)
            topics.append(query['medical_topic'][:30] + "...")
        except:
            continue
    
    if not times:
        return
    
    # Zaman çizelgesi grafiği
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=times,
        y=topics,
        mode='markers+lines',
        marker=dict(size=10, color='#667eea'),
        line=dict(color='#667eea', width=2),
        name=get_text('history_queries')
    ))
    
    fig.update_layout(
        title="Son Aktiviteler",
        xaxis_title="Zaman",
        yaxis_title="Konular",
        height=300,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)

def create_loading_animation():
    """Dinamik loading animasyonu"""
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <div class="loading-spinner"></div>
        <p style="margin-top: 1rem; color: #667eea;">AI çalışıyor...</p>
    </div>
    
    <style>
    .loading-spinner {
        width: 50px;
        height: 50px;
        border: 5px solid #f3f3f3;
        border-top: 5px solid #667eea;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin: 0 auto;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    </style>
    """, unsafe_allow_html=True)

class SynapseAI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.configure_model()
    
    def configure_model(self):
        """Gemini modelini yapılandır"""
        try:
            genai.configure(api_key=self.api_key)
            
            generation_config = {
                "temperature": 0.7,
                "top_p": 0.9,
                "top_k": 40,
                "max_output_tokens": 1000,
            }
            
            self.model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                generation_config=generation_config,
            )
            return True
        except Exception as e:
            st.error(f"Model yapılandırma hatası: {str(e)}")
            return False
    
    def generate_analogy(self, medical_topic: str, patient_profile: Dict, length: str = "orta", detail: str = "genel", tone: str = "samimi") -> str:
        """Tıbbi analoji üret (dinamik parametrelerle)"""
        age_group = patient_profile.get('age', '')
        interest = patient_profile.get('interest', '')
        gender = patient_profile.get('gender', '')
        education = patient_profile.get('education', '')
        job = patient_profile.get('job', '')

        # Uzunluk, detay ve ton için açıklama haritaları
        length_map = {
            "kısa": "Kısa ve öz tut.",
            "orta": "Orta uzunlukta, yeterli açıklama ile.",
            "uzun": "Detaylı ve uzun bir analoji yaz.",
            "short": "Keep it short and concise.",
            "medium": "Medium length with sufficient explanation.",
            "long": "Write a detailed and long analogy."
        }
        detail_map = {
            "genel": "Genel hatlarıyla açıkla.",
            "detaylı": "Detaylara gir, örneklerle zenginleştir.",
            "general": "Explain in general terms.",
            "detailed": "Go into details, enrich with examples."
        }
        tone_map = {
            "resmi": "Resmi ve ciddi bir dil kullan.",
            "samimi": "Samimi, sıcak ve motive edici bir dil kullan.",
            "çocuksu": "Çocuklara uygun, eğlenceli ve basit bir dil kullan.",
            "formal": "Use a formal and serious tone.",
            "friendly": "Use a friendly, warm and motivating tone.",
            "childish": "Use a child-friendly, fun and simple tone."
        }

        prompt = f"""
        Sen deneyimli bir doktor ve yaratıcı bir iletişim uzmanısın.\n\
        Görevin karmaşık tıbbi konuları hastalar için anlaşılır analojiler haline getirmek.\n\
        TIBBİ KONU: {medical_topic}\n\
        HASTA YAŞI: {age_group}\n\
        CİNSİYET: {gender}\n\
        EĞİTİM SEVİYESİ: {education}\n\
        MESLEK: {job}\n\
        İLGİ ALANI: {interest}\n\
        Analoji Uzunluğu: {length_map.get(length, length)}\n\
        Detay Seviyesi: {detail_map.get(detail, detail)}\n\
        Ton: {tone_map.get(tone, tone)}\n\
        Lütfen bu tıbbi konuyu, hasta profiline uygun, seçilen uzunluk, detay ve ton ile bir analojiyle açıkla.\n\
        Analojin:\n\
        - Günlük yaşamdan örnekler içermeli\n        - Hasta profiline uygun olmalı\n        - Korku yaratmamalı, umut vermeli\n        - Basit ve akılda kalıcı olmalı\n        - Türkçe olmalı\n\
        Analoji:\n        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Analoji üretimi sırasında hata: {str(e)}"
    
    def generate_visual_story(self, medical_topic: str, patient_profile: Dict) -> str:
        """Görsel hikaye önerisi üret"""
        age_group = patient_profile.get('age', '')
        interest = patient_profile.get('interest', '')
        
        prompt = f"""
        Sen bir çocuk kitabı yazarı ve illüstratörüsün. 
        Tıbbi konuları görsel hikayelerle anlatmak için yaratıcı öneriler üretiyorsun.
        
        TIBBİ KONU: {medical_topic}
        HASTA YAŞI: {age_group}
        İLGİ ALANI: {interest}
        
        Bu tıbbi konu için 4 adımdan oluşan görsel hikaye önerisi hazırla:
        1. Normal durum (sağlıklı hal)
        2. Problemin başlangıcı
        3. Tedavi süreci
        4. İyileşme ve umut
        
        Her adım için:
        - Çizilecek sahne açıklaması
        - Kullanılacak renkler
        - Karakterler ve nesneler
        - Hasta profiline uygun öğeler
        
        Hikaye önerisi:
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Hikaye üretimi sırasında hata: {str(e)}"
    
    def generate_word_warnings(self, medical_topic: str, patient_profile: Dict) -> str:
        """Kaçınılması gereken kelimeler için uyarı üret"""
        age_group = patient_profile.get('age', '')
        
        prompt = f"""
        Sen bir tıbbi iletişim uzmanısın. 
        Hastalara tıbbi durumları anlatırken kaçınılması gereken kelimeler ve daha iyi alternatifler hakkında rehberlik yapıyorsun.
        
        TIBBİ KONU: {medical_topic}
        HASTA YAŞI: {age_group}
        
        Bu tıbbi konu için:
        1. Kaçınılması gereken kelimeler ve ifadeler
        2. Her biri için alternatif, daha olumlu kelimeler
        3. Neden kaçınılması gerektiğinin açıklaması
        
        Yaş grubuna özel öneriler ver.
        
        Kelime rehberi:
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Kelime uyarısı üretimi sırasında hata: {str(e)}"

def main():
    # Ana başlık
    create_animated_header()

    # Sidebar - API Key ve Ayarlar
    with st.sidebar:
        st.header(get_text("settings"))
        
        # Dil seçimi
        selected_language = st.selectbox(
            "🌍 Dil / Language",
            list(LANGUAGES.keys()),
            index=0 if st.session_state.language == "tr" else 1
        )
        st.session_state.language = LANGUAGES[selected_language]
        
        # Tema seçici ve tema CSS kodları kaldırıldı.
        
        # API Key girişi
        api_key = st.text_input(
            get_text("api_key_label"), 
            type="password", 
            value=st.session_state.api_key or "",
            help=get_text("api_key_help")
        )
        
        if api_key:
            st.session_state.api_key = api_key
            if st.session_state.model is None:
                try:
                    st.session_state.model = SynapseAI(api_key)
                    st.success("✅ API bağlantısı başarılı!")
                except Exception as e:
                    st.error(f"❌ API bağlantısı başarısız: {str(e)}")
        
        st.markdown("---")
        
        # Proje bilgileri
        st.header(get_text("project_info"))
        st.markdown(f"""
        **{get_text('team')}:** YZTA-Bootcamp-Grup-134  
        **{get_text('sprint')}:** 2/3  
        **{get_text('version')}:** 2.0  
        **{get_text('developers')}:** Hasan BUDAK, Cemre Dağ, Yusuf Sait Sakoğlu
        """)
        
        st.markdown("---")
        
        # Kullanım istatistikleri
        st.header(get_text("usage_stats"))
        create_usage_chart()
        create_activity_timeline()
        
        # Geçmiş temizleme
        if st.button(get_text("clear_history")):
            st.session_state.history = []
            st.success("Geçmiş temizlendi!")

    # Ana içerik alanı
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header(get_text("analogy_generation"))
        
        # --- Form ---
        with st.form("analogy_form"):
            st.markdown('<div class="module-card">', unsafe_allow_html=True)
            # Tıbbi konu
            medical_topic = st.text_area(
                get_text("medical_topic"),
                placeholder=get_text("medical_topic_placeholder"),
                height=100,
                help=get_text("medical_topic_help")
            )
            is_topic_filled = bool(medical_topic.strip())
            # Hasta profili
            col_age, col_interest = st.columns(2)
            with col_age:
                patient_age = st.selectbox(
                    get_text("patient_age"),
                    AGE_GROUPS[st.session_state.language],
                    help=get_text("patient_age_help")
                )
            with col_interest:
                patient_interest = st.selectbox(
                    get_text("patient_interest"),
                    INTEREST_AREAS[st.session_state.language],
                    help=get_text("patient_interest_help")
                )
            # Ek hasta profili alanları
            col_gender, col_edu, col_job = st.columns(3)
            with col_gender:
                patient_gender = st.selectbox(
                    "Cinsiyet" if st.session_state.language == "tr" else "Gender",
                    ["Kadın", "Erkek", "Diğer"] if st.session_state.language == "tr" else ["Female", "Male", "Other"]
                )
            with col_edu:
                patient_education = st.selectbox(
                    "Eğitim Seviyesi" if st.session_state.language == "tr" else "Education Level",
                    ["İlkokul", "Ortaokul", "Lise", "Üniversite", "Yüksek Lisans", "Doktora"] if st.session_state.language == "tr" else ["Primary", "Secondary", "High School", "University", "Master's", "PhD"]
                )
            with col_job:
                patient_job = st.text_input(
                    "Meslek" if st.session_state.language == "tr" else "Occupation",
                    ""
                )
            # Analoji parametreleri
            st.subheader(get_text("analogy_settings"))
            col_len, col_det, col_tone = st.columns(3)
            with col_len:
                analogy_length = st.radio(
                    get_text("length"),
                    ANALOGY_PARAMS[st.session_state.language]["length"],
                    index=1,
                    help=get_text("length_help")
                )
            with col_det:
                analogy_detail = st.radio(
                    get_text("detail_level"),
                    ANALOGY_PARAMS[st.session_state.language]["detail"],
                    index=0,
                    help=get_text("detail_help")
                )
            with col_tone:
                analogy_tone = st.radio(
                    get_text("tone"),
                    ANALOGY_PARAMS[st.session_state.language]["tone"],
                    index=1,
                    help=get_text("tone_help")
                )
            # Modül seçimi
            st.subheader(get_text("output_modules"))
            col_mod1, col_mod2, col_mod3 = st.columns(3)
            with col_mod1:
                gen_analogy = st.checkbox(get_text("generate_analogy"), value=True)
            with col_mod2:
                gen_story = st.checkbox(get_text("generate_story"))
            with col_mod3:
                gen_warnings = st.checkbox(get_text("generate_warnings"))
            st.markdown('</div>', unsafe_allow_html=True)
            submitted = st.form_submit_button(get_text("submit_button"), type="primary")
            if submitted and not is_topic_filled:
                st.warning("Lütfen tıbbi konu alanını doldurun.")

    # --- FORM BLOĞU BİTTİ ---
    # Formdan çıktıktan sonra, butona basıldıysa ve tıbbi konu doluysa analoji üretimini burada yap
    if submitted and is_topic_filled:
        patient_profile = {
            'age': patient_age,
            'interest': patient_interest,
            'gender': patient_gender,
            'education': patient_education,
            'job': patient_job
        }
        with st.spinner("AI çalışıyor..."):
            analogy_result = st.session_state.model.generate_analogy(
                medical_topic, patient_profile, analogy_length, analogy_detail, analogy_tone
            )
            st.session_state['analogy_result'] = analogy_result

    # Sonuç ve butonlar
    analogy_result = st.session_state.get('analogy_result', None)
    if analogy_result:
        st.markdown(f"<div class='result-card'><h4>{get_text('generated_analogy')}</h4></div>", unsafe_allow_html=True)
        st.text_area("", value=analogy_result, height=180, key="analogy_output", label_visibility="collapsed")
        # Sadece WhatsApp paylaşım butonu gösteriliyor
        import urllib.parse
        wa_body = urllib.parse.quote(analogy_result)
        wa_link = f"https://wa.me/?text={wa_body}"
        st.markdown(f'<a href="{wa_link}" target="_blank" style="text-decoration:none;font-weight:600;">🟢 {get_text("whatsapp_share")}</a>', unsafe_allow_html=True)

    with col2:
        st.header(get_text("history_queries"))
        
        if st.session_state.history:
            for i, entry in enumerate(reversed(st.session_state.history[-10:])):
                with st.expander(f"Sorgu {len(st.session_state.history) - i}: {entry['timestamp']}"):
                    st.write(f"**Konu:** {entry['medical_topic'][:50]}...")
                    st.write(f"**Hasta:** {entry['patient_profile']['age']}, {entry['patient_profile']['interest']}")
                    
                    if st.button(f"{get_text('reuse_query')} {len(st.session_state.history) - i}", key=f"reuse_{i}"):
                        # Tekrar kullanma özelliği için state'i güncelleyelim
                        st.session_state.reuse_data = {
                            'topic': entry['medical_topic'],
                            'age': entry['patient_profile']['age'],
                            'interest': entry['patient_profile']['interest']
                        }
                        st.rerun()
        else:
            st.info(get_text("no_history"))
            
        st.markdown("---")
        
        # Yardım ve bilgi
        st.header(get_text("help_section"))
        st.markdown(f"""
        **{get_text('how_to_use')}**
        1. API anahtarınızı girin
        2. Tıbbi konuyu yazın
        3. Hasta profilini seçin
        4. İstediğiniz modülleri işaretleyin
        5. '{get_text('submit_button')}' butonuna tıklayın
        
        **{get_text('tips')}**
        - Tıbbi konuyu detaylı yazın
        - Hasta profilini doğru seçin
        - Birden fazla modül deneyebilirsiniz
        """)

if __name__ == "__main__":
    main()
