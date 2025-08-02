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
        "developers": "Geliştiriciler",
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
        "whatsapp_share": "WhatsApp",
        "community": "👥 Topluluk",
        "announcements": "📢 Duyurular",
        "community_comments": "💬 Topluluk Yorumları",
        "add_comment": "Yorum Ekle",
        "your_name": "Adınız",
        "your_comment": "Yorumunuz",
        "submit_comment": "Yorum Gönder",
        "no_comments": "Henüz yorum yok. İlk yorumu siz yapın!",
        "comment_success": "Yorumunuz başarıyla eklendi!",
        "recent_announcements": "Son Duyurular",
        "no_announcements": "Henüz duyuru yok.",
        "community_stats": "Topluluk İstatistikleri",
        "total_comments": "Toplam Yorum",
        "active_users": "Aktif Kullanıcı",
        "page_home": "🏠 Ana Sayfa",
        "page_community": "👥 Topluluk",
        "like_comment": "👍 Beğen",
        "reply_comment": "💬 Yanıtla",
        "share_experience": "Deneyim Paylaş",
        "helpful_tips": "Faydalı İpuçları",
        "medical_stories": "Tıbbi Hikayeler",
        "upcoming_events": "🎉 Yaklaşan Etkinlikler"
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
        "whatsapp_share": "WhatsApp",
        "community": "👥 Community",
        "announcements": "📢 Announcements",
        "community_comments": "💬 Community Comments",
        "add_comment": "Add Comment",
        "your_name": "Your Name",
        "your_comment": "Your Comment",
        "submit_comment": "Submit Comment",
        "no_comments": "No comments yet. Be the first to comment!",
        "comment_success": "Your comment has been added successfully!",
        "recent_announcements": "Recent Announcements",
        "no_announcements": "No announcements yet.",
        "community_stats": "Community Statistics",
        "total_comments": "Total Comments",
        "active_users": "Active Users",
        "page_home": "🏠 Home",
        "page_community": "👥 Community",
        "like_comment": "👍 Like",
        "reply_comment": "💬 Reply",
        "share_experience": "Share Experience",
        "helpful_tips": "Helpful Tips",
        "medical_stories": "Medical Stories",
        "upcoming_events": "🎉 Upcoming Events"
    }
}

LANGUAGES = {
    "🇹🇷 Türkçe": "tr",
    "🇺🇸 English": "en"
}

AGE_GROUPS = {
    "tr": ["0-5 yaş", "6-12 yaş", "13-18 yaş", "19-65 yaş", "65+ yaş"],
    "en": ["0-5 years", "6-12 years", "13-18 years", "19-65 years", "65+ years"]
}

INTEREST_AREAS = {
    "tr": ["Arabalar", "Hayvanlar", "Spor", "Müzik", "Bahçıvanlık", "Teknoloji", "Yemek", "Kitaplar"],
    "en": ["Cars", "Animals", "Sports", "Music", "Gardening", "Technology", "Food", "Books"]
}

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

# GÜNCELLENEN DUYURULAR (2025 tarihleri - Ağustos-Eylül)
SAMPLE_ANNOUNCEMENTS = {
    "tr": [
        {
            "title": "🎉 Synapse v2.2 Güncelleme Duyurusu",
            "content": "Yeni özellik: Görsel hikaye modülü tam entegre edildi! Artık tıbbi konuları hem analoji hem de hikaye formatında açıklayabilirsiniz. Hasta-hasta yakını yorumları da eklendi.",
            "date": "2025-08-05",
            "type": "update"
        },
        {
            "title": "🔧 Planlı Sistem Bakımı",  
            "content": "15 Ağustos Cuma günü saat 02:00-04:00 arasında rutin sistem güncellemesi yapılacaktır. Bu sürede geçici kesintiler yaşanabilir.",
            "date": "2025-08-10",
            "type": "maintenance"
        },
        {
            "title": "🎯 Hasta Deneyimi Paylaşım Kampanyası",
            "content": "Eylül ayında 'Hastalık Yolculuğum' temalı deneyim paylaşım kampanyası başlıyor. En etkileyici hikayeler ödüllendirilecek.",
            "date": "2025-08-20", 
            "type": "feature"
        }
    ],
    "en": [
        {
            "title": "🎉 Synapse v2.2 Update Announcement",
            "content": "New feature: Visual story module fully integrated! Now you can explain medical topics in both analogy and story formats. Patient and family comments also added.",
            "date": "2025-08-05",
            "type": "update"
        },
        {
            "title": "🔧 Scheduled System Maintenance",
            "content": "Routine system update will be performed on Friday, August 15th between 02:00-04:00. Temporary interruptions may occur.",
            "date": "2025-08-10", 
            "type": "maintenance"
        },
        {
            "title": "🎯 Patient Experience Sharing Campaign",
            "content": "Starting in September: 'My Disease Journey' themed experience sharing campaign. Most impactful stories will be rewarded.",
            "date": "2025-08-20",
            "type": "feature"
        }
    ]
}

st.set_page_config(
    page_title="Synapse - Medikal Analoji Üreteci",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
    .module-card, .result-card, .warning-card, .error-card, .story-card, .community-card, .announcement-card, .comment-card {
        background: #fff;
        padding: 1.7rem 1.2rem;
        border-radius: 14px;
        border-left: 5px solid #667eea;
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 18px rgba(102,126,234,0.07);
        transition: box-shadow 0.2s, transform 0.2s;
        position: relative;
    }
    .module-card:hover, .result-card:hover, .warning-card:hover, .error-card:hover, .story-card:hover, .community-card:hover, .announcement-card:hover, .comment-card:hover {
        box-shadow: 0 8px 32px rgba(102,126,234,0.18);
        transform: translateY(-2px) scale(1.01);
    }
    
    .community-card {
        border-left-color: #28a745;
    }
    .announcement-card {
        border-left-color: #ffc107;
        background: linear-gradient(135deg, #fff9e6 0%, #ffffff 100%);
    }
    .comment-card {
        border-left-color: #17a2b8;
        margin-left: 1rem;
        position: relative;
    }
    .announcement-card.update { border-left-color: #28a745; }
    .announcement-card.maintenance { border-left-color: #dc3545; }
    .announcement-card.feature { border-left-color: #007bff; }
    
    .announcement-mini {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.8rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        font-size: 0.9rem;
        box-shadow: 0 2px 8px rgba(102,126,234,0.2);
    }
    .announcement-mini h6 {
        margin: 0 0 0.3rem 0;
        font-size: 0.95rem;
        font-weight: 600;
    }
    .announcement-mini p {
        margin: 0;
        font-size: 0.85rem;
        opacity: 0.9;
    }
    
    .page-nav {
        display: flex;
        gap: 1rem;
        margin-bottom: 2rem;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .result-card h4, .story-card h4, .warning-card h4, .community-card h4, .announcement-card h4, .comment-card h4 {
        margin-top: 0;
        font-size: 1.3rem;
        color: #667eea;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .result-card p, .story-card p, .warning-card p, .community-card p, .announcement-card p, .comment-card p {
        font-size: 1.1rem;
        color: #222;
        margin-bottom: 0.5rem;
    }
    
    .like-btn, .reply-btn {
        background: none;
        border: none;
        color: #667eea;
        cursor: pointer;
        font-size: 0.9rem;
        padding: 0.3rem 0.5rem;
        border-radius: 4px;
        transition: background 0.2s;
    }
    
    .like-btn:hover, .reply-btn:hover {
        background: #f0f2ff;
    }
    
    .like-btn.liked {
        color: #28a745;
        font-weight: bold;
    }
    
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
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"
if 'community_comments' not in st.session_state:
    st.session_state.community_comments = [
        {
            'name': 'Ayşe Yılmaz - Diyabet Hastası',
            'comment': ' İlk defa bu kadar net anladım. Artık ilaçlarımı neden düzenli almam gerektiğini biliyorum. Teşekkürler!',
            'timestamp': '2025-07-28 14:30:00',
            'likes': 23,
            'category': 'deneyim',
            'liked_by': []
        },
        {
            'name': 'Mehmet Demir - Kanser Hasta Yakını',
            'comment': ' Kötü hücrelerin temizlendiğini artık daha iyi anlıyoruz.',
            'timestamp': '2025-07-25 09:45:00',
            'likes': 19,
            'category': 'deneyim',
            'liked_by': []
        },
        {
            'name': 'Fatma Öz - Astım Hastası',
            'comment': 'Astım nöbetlerimi anlattılar. Artık çocuğum da durumu anlıyor ve inhalerimle ilgili daha dikkatli.',
            'timestamp': '2025-07-20 16:20:00',
            'likes': 15,
            'category': 'ipucu',
            'liked_by': []
        },
        {
            'name': 'Ali Kaya - Hipertansiyon Hastası',
            'comment': 'tuz tüketimimi azaltmaya daha çok motive oldum.',
            'timestamp': '2025-07-18 11:15:00',
            'likes': 27,
            'category': 'deneyim',
            'liked_by': []
        },
        {
            'name': 'Zeynep Aksoy - Hasta Yakını',
            'comment': 'Oğlumun DEHB durumunu  açıkladılar. Artık tedavi sürecine daha sabırla yaklaşıyorum.',
            'timestamp': '2025-07-15 13:40:00',
            'likes': 21,
            'category': 'ipucu',
            'liked_by': []
        },
        {
            'name': 'Hasan Çelik - Böbrek Hastası',
            'comment': 'Böbrek yetmezliğimi su filtreleme sistemi gibi anlattıkları için diyaliz sürecinden artık o kadar korkmuyorum.',
            'timestamp': '2025-07-12 08:25:00',
            'likes': 18,
            'category': 'deneyim',
            'liked_by': []
        }
    ]
if 'user_likes' not in st.session_state:
    st.session_state.user_likes = set()

def get_text(key: str) -> str:
    """Dil çevirisi için yardımcı fonksiyon"""
    return TRANSLATIONS[st.session_state.language].get(key, key)

def create_animated_header():
    """Animasyonlu başlık oluştur"""
    colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c', '#4facfe', '#00f2fe']
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

def create_page_navigation():
    """Sayfa navigasyonu oluştur"""
    st.markdown(f"""
    <div class="page-nav">
        <h3 style="margin: 0; color: #333;">📖 Sayfa Seçimi</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(get_text("page_home"), key="nav_home", 
                    type="primary" if st.session_state.current_page == "home" else "secondary"):
            st.session_state.current_page = "home"
            st.rerun()
    
    with col2:
        if st.button(get_text("page_community"), key="nav_community",
                    type="primary" if st.session_state.current_page == "community" else "secondary"):
            st.session_state.current_page = "community"
            st.rerun()

def create_events_widget():
    """Yan panel için mini etkinlik widget'ı (GÜNCELLENEN TARİHLER - Ağustos-Eylül 2025)"""
    st.markdown("### " + get_text('upcoming_events'))
    
    events = [
        {
            "title": "🏥 Hasta İletişimi Workshop'u",
            "date": "20 Ağustos 2025",
            "time": "14:00",
            "description": "Hasta-doktor iletişiminde etkili analoji kullanımı teknikleri"
        },
        {
            "title": "🧠 Sağlıkta Yapay Zeka Zirvesi",  
            "date": "5 Eylül 2025",
            "time": "10:00",
            "description": "Tıp alanında AI uygulamaları ve hasta deneyimi"
        },
        {
            "title": "🎯 Hasta Hikayesi Paylaşım Etkinliği",
            "date": "15 Eylül 2025",
            "time": "16:30",
            "description": "Hastalık deneyimlerini paylaşma ve destek ağı kurma"
        },
        {
            "title": "📖 Görsel Hikaye Yaratıcılık Atölyesi",
            "date": "25 Eylül 2025",
            "time": "15:00",
            "description": "Tıbbi konuları hikaye formatında anlatma teknikleri"
        }
    ]
    
    for event in events:
        st.markdown(f"""
        <div class="announcement-mini">
            <h6>{event['title']}</h6>
            <p>📅 {event['date']} - ⏰ {event['time']}</p>
            <p style="font-size: 0.8rem; opacity: 0.8;">{event['description']}</p>
        </div>
        """, unsafe_allow_html=True)

def create_announcements_widget():
    """Yan panel için mini duyuru widget'ı"""
    st.markdown("### " + get_text('recent_announcements'))
    
    announcements = SAMPLE_ANNOUNCEMENTS[st.session_state.language]
    
    for announcement in announcements[:2]:
        st.markdown(f"""
        <div class="announcement-mini">
            <h6>{announcement['title']}</h6>
            <p>{announcement['content'][:80]}...</p>
        </div>
        """, unsafe_allow_html=True)

def handle_like_comment(comment_index: int):
    """Beğeni işlemlerini yönet - beğeni varsa kaldır, yoksa ekle"""
    comment_id = f"comment_{comment_index}"
    
    if comment_id in st.session_state.user_likes:
        st.session_state.user_likes.remove(comment_id)
        st.session_state.community_comments[comment_index]['likes'] -= 1
    else:
        st.session_state.user_likes.add(comment_id)
        st.session_state.community_comments[comment_index]['likes'] += 1
    
    st.rerun()

def create_community_page():
    """Topluluk sayfası oluştur"""
    st.header(f"👥 {get_text('community')}")
    
    # Topluluk istatistikleri
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(get_text("total_comments"), len(st.session_state.community_comments))
    with col2:
        st.metric(get_text("active_users"), len(set([c.get('name', 'Anonim') for c in st.session_state.community_comments])))
    with col3:
        st.metric("👨‍⚕️ Hasta & Yakınları", len([c for c in st.session_state.community_comments if 'Hasta' in c.get('name', '') or 'Anne' in c.get('name', '') or 'Yakın' in c.get('name', '')]))
    with col4:
        total_likes = sum([c.get('likes', 0) for c in st.session_state.community_comments])
        st.metric("💖 Toplam Beğeni", total_likes)
    
    st.markdown("---")
    
    # Ana içerik: Sol taraf duyurular, sağ taraf yorumlar
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Duyurular bölümü
        st.markdown(f'### 📢 {get_text("announcements")}')
        
        announcements = SAMPLE_ANNOUNCEMENTS[st.session_state.language]
        
        for announcement in announcements:
            announcement_type = announcement.get('type', 'update')
            st.markdown(f"""
            <div class="announcement-card {announcement_type}">
                <h5>{announcement['title']}</h5>
                <p>{announcement['content']}</p>
                <small style="color: #666;">📅 {announcement['date']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # Yorum ekleme formu
        st.markdown(f'### 💬 {get_text("add_comment")}')
        
        # Kategori seçimi
        comment_categories = {
            "tr": {
                "deneyim": "🏥 Hastalık Deneyimi",
                "ipucu": "💡 Tedavi İpucu", 
                "soru": "❓ Soru & Merak",
                "destek": "🤝 Destek & Motivasyon"
            },
            "en": {
                "experience": "🏥 Disease Experience",
                "tip": "💡 Treatment Tip", 
                "question": "❓ Question & Curiosity",
                "support": "🤝 Support & Motivation"
            }
        }
        
        with st.form("comment_form"):
            user_name = st.text_input(get_text("your_name"), placeholder="Adınızı ve durumunuzu girin (örn: Ayşe - Diyabet Hastası)")
            comment_category = st.selectbox(
                "Kategori", 
                list(comment_categories[st.session_state.language].values()),
                help="Yorumunuzun kategorisini seçin"
            )
            user_comment = st.text_area(get_text("your_comment"), placeholder="Deneyiminizi, sorunuzu veya ipucunuzu paylaşın...", height=120)
            
            if st.form_submit_button(get_text("submit_comment"), type="primary"):
                if user_name.strip() and user_comment.strip():
                    category_key = list(comment_categories[st.session_state.language].keys())[
                        list(comment_categories[st.session_state.language].values()).index(comment_category)
                    ]
                    
                    new_comment = {
                        'name': user_name.strip(),
                        'comment': user_comment.strip(),
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'likes': 0,
                        'category': category_key,
                        'liked_by': []
                    }
                    st.session_state.community_comments.append(new_comment)
                    st.success(get_text("comment_success"))
                    st.rerun()
                else:
                    st.warning("Lütfen isim ve yorum alanlarını doldurun!")
        
        st.markdown("---")
        
        # Yorum filtreleme
        st.markdown("### 🔍 Yorumları Filtrele")
        filter_category = st.selectbox(
            "Kategori Filtresi",
            ["Tümü"] + list(comment_categories[st.session_state.language].values())
        )
        
        # Yorumları göster
        st.markdown(f'### 💬 {get_text("community_comments")}')
        
        if st.session_state.community_comments:
            filtered_comments = st.session_state.community_comments
            if filter_category != "Tümü":
                category_key = list(comment_categories[st.session_state.language].keys())[
                    list(comment_categories[st.session_state.language].values()).index(filter_category)
                ]
                filtered_comments = [c for c in st.session_state.community_comments if c.get('category') == category_key]
            
            for i, comment in enumerate(reversed(filtered_comments)):
                category_emojis = {"deneyim": "🏥", "ipucu": "💡", "soru": "❓", "destek": "🤝"}
                category_emoji = category_emojis.get(comment.get('category', 'deneyim'), "💬")
                
                st.markdown(f"""
                <div class="comment-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <h6 style="color: #17a2b8; margin: 0;">{category_emoji} {comment['name']}</h6>
                        <span style="font-size: 0.8rem; color: #666;">🕒 {comment['timestamp']}</span>
                    </div>
                    <p style="margin-bottom: 0.5rem;">{comment['comment']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Beğeni butonu - toggle özelliği ile
                comment_idx = st.session_state.community_comments.index(comment)
                comment_id = f"comment_{comment_idx}"
                is_liked = comment_id in st.session_state.user_likes
                
                like_emoji = "❤️" if is_liked else "👍"
                like_text = f"{like_emoji} {comment.get('likes', 0)}"
                
                if st.button(like_text, key=f"like_btn_{comment_idx}_{i}"):
                    handle_like_comment(comment_idx)
                        
        else:
            st.info(get_text("no_comments"))

def create_usage_chart():
    """Kullanım istatistikleri için dinamik grafik oluştur"""
    if not st.session_state.history:
        return
    
    recent_queries = st.session_state.history[-10:]
    
    module_usage = {
        'analogy': sum(1 for q in recent_queries if 'analogy' in q.get('results', {})),
        'story': sum(1 for q in recent_queries if 'story' in q.get('results', {})),
        'warnings': sum(1 for q in recent_queries if 'warnings' in q.get('results', {}))
    }
    
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

class SynapseAI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.configure_model()
    
    def configure_model(self):
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
        age_group = patient_profile.get('age', '')
        interest = patient_profile.get('interest', '')
        gender = patient_profile.get('gender', '')
        education = patient_profile.get('education', '')
        job = patient_profile.get('job', '')

        prompt = f"""
        Sen deneyimli bir doktor ve yaratıcı bir iletişim uzmanısın.
        Görevin karmaşık tıbbi konuları hastalar için anlaşılır analojilerle açıklamak.
        
        TIBBİ KONU: {medical_topic}
        HASTA YAŞI: {age_group}
        CİNSİYET: {gender}
        EĞİTİM SEVİYESİ: {education}
        MESLEK: {job}
        İLGİ ALANI: {interest}
        
        Analoji parametreleri: {length}, {detail}, {tone}
        
        Lütfen bu tıbbi konuyu, hasta profiline uygun bir analojiyle açıkla.
        Analojin günlük yaşamdan örnekler içermeli, korku yaratmamalı ve akılda kalıcı olmalı.
        Hastanın ilgi alanını da dikkate alarak analoji seç.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            if "API_KEY_INVALID" in str(e):
                return """
                ❌ API ANAHTARI GEÇERSİZ
                
                Lütfen şu adımları takip edin:
                
                1️⃣ https://makersuite.google.com/app/apikey adresine gidin
                2️⃣ Yeni bir API anahtarı oluşturun
                3️⃣ Anahtarı kopyalayıp sol panele yapıştırın
                4️⃣ "✅ API bağlantısı başarılı!" mesajını bekleyin
                
                ⚠️ Geçici olarak örnek analoji:
                "Vücudunuz bir bahçe gibidir. Hastalık, bahçenizde istenmeyen otlar gibidir.
                Tedavi ise bu otları temizleyip güzel çiçeklerin büyümesini sağlayan 
                bahçıvan gibidir..."
                """
            else:
                return f"Analoji üretimi sırasında hata: {str(e)}"
    
    def generate_visual_story(self, medical_topic: str, patient_profile: Dict, analogy_content: str) -> str:
        """Görsel hikaye üretimi"""
        age_group = patient_profile.get('age', '')
        interest = patient_profile.get('interest', '')
        
        prompt = f"""
        Sen yaratıcı bir hikaye anlatıcısısın ve tıbbi konuları hikaye formatında açıklıyorsun.
        
        TIBBİ KONU: {medical_topic}
        HASTA YAŞI: {age_group}
        İLGİ ALANI: {interest}
        TEMEL ANALOJİ: {analogy_content}
        
        Lütfen bu tıbbi konuyu kısa bir görsel hikaye formatında anlat.
        Hikaye:
        - 3-5 paragraf uzunluğunda olsun
        - Görsel detaylar içersin (renkler, şekiller, hareketler)
        - Hastanın yaş grubu ve ilgi alanına uygun olsun
        - Verilen analojiden yararlan ama daha hikaye formatında genişlet
        - Umut verici ve olumlu bir sonla bitsin
        
        Hikayeyi "Bir varmış bir yokmuş..." tarzında başlat ve hasta için rahatlatıcı olacak şekilde kurgula.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            # API hatası durumunda geçici örnek hikaye döndür
            if "API_KEY_INVALID" in str(e):
                return f"""
                ⚠️ API Anahtarı Sorunu Tespit Edildi
                
                Lütfen geçerli bir Gemini API anahtarı girin.
                
                📋 Kontrol Listesi:
                ✓ Google AI Studio'dan yeni API anahtarı alın
                ✓ API anahtarının başında/sonunda boşluk olmadığından emin olun  
                ✓ Anahtarın AIza... ile başladığını kontrol edin
                ✓ 39 karakter uzunluğunda olduğunu doğrulayın
                
                🔗 API Anahtarı: https://makersuite.google.com/app/apikey
                
                --- ÖRNEK HİKAYE (Test Amaçlı) ---
                
                Bir varmış bir yokmuş, güzel bir bahçede renkli çiçekler varmış. 
                Bu bahçede her çiçeğin kendine özel bir görevi varmış - tıpkı vücudumuzda 
                her organın özel bir görevi olduğu gibi...
                
                (Gerçek hikaye için lütfen geçerli API anahtarı girin)
                """
            else:
                return f"Görsel hikaye üretimi sırasında hata: {str(e)}"
    
    def generate_word_warnings(self, medical_topic: str, patient_profile: Dict) -> str:
        """Kelime kullanım uyarıları üretimi"""
        age_group = patient_profile.get('age', '')
        education = patient_profile.get('education', '')
        
        prompt = f"""
        Sen hasta iletişimi konusunda uzman bir doktorsun.
        
        TIBBİ KONU: {medical_topic}
        HASTA YAŞI: {age_group}
        EĞİTİM SEVİYESİ: {education}
        
        Bu tıbbi konu hakkında hastalarla konuşurken:
        
        ✅ KULLANILMASI GEREKEN KELİMELER:
        - Hasta için anlaşılır ve rahatlatıcı kelimeler
        - Olumlu ve umut verici ifadeler
        - Günlük dilde karşılıkları olan terimler
        
        ❌ KAÇINILMASI GEREKEN KELİMELER:
        - Korkutucu ve endişe verici ifadeler
        - Ağır tıbbi terimler
        - Belirsizlik yaratan belirsiz ifadeler
        
        🎯 ÖNERİLER:
        - Bu yaş grubuna uygun iletişim teknikleri
        - Eğitim seviyesine göre dil kullanımı önerileri
        
        Lütfen bu kategorilerde öneriler ver.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            if "API_KEY_INVALID" in str(e):
                return """
                ❌ API ANAHTARI SORUNU
                
                Geçerli bir API anahtarı gerekmektedir.
                
                📋 GENEL KELİME KULLANIM REHBERİ:
                
                ✅ KULLANIN:
                • "İyileşme süreci" → "Hastalıkla mücadele" yerine
                • "Tedavi desteği" → "Müdahale" yerine  
                • "Vücut savunması" → "Bağışıklık sistemi" yerine
                • "İyiye gidiyor" → "Stabil" yerine
                
                ❌ KAÇININ:
                • "Ölümcül, kritik, kötü huylu"
                • "Metastaz, malign, invaziv"
                • "Prognoz belirsiz, risk yüksek"
                
                🎯 Hasta yaş grubuna göre dil uyarlayın.
                """
            else:
                return f"Kelime uyarıları üretimi sırasında hata: {str(e)}"

def create_home_page():
    """Ana sayfa (analoji üretimi) içeriği"""
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header(get_text("analogy_generation"))
        
        with st.form("analogy_form"):
            st.markdown('<div class="module-card">', unsafe_allow_html=True)
            
            medical_topic = st.text_area(
                get_text("medical_topic"),
                placeholder=get_text("medical_topic_placeholder"),
                height=100,
                help=get_text("medical_topic_help")
            )
            
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
            
            col_gender, col_edu, col_job = st.columns(3)
            with col_gender:
                patient_gender = st.selectbox(
                    "Cinsiyet" if st.session_state.language == "tr" else "Gender",
                    ["Kadın", "Erkek", "Diğer"] if st.session_state.language == "tr" else ["Female", "Male", "Other"]
                )
            with col_edu:
                patient_education = st.selectbox(
                    "Eğitim Seviyesi" if st.session_state.language == "tr" else "Education Level",
                    ["İlkokul", "Ortaokul", "Lise", "Üniversite"] if st.session_state.language == "tr" else ["Primary", "Secondary", "High School", "University"]
                )
            with col_job:
                patient_job = st.text_input("Meslek" if st.session_state.language == "tr" else "Occupation", "")
            
            st.subheader(get_text("analogy_settings"))
            col_len, col_det, col_tone = st.columns(3)
            with col_len:
                analogy_length = st.radio(
                    get_text("length"),
                    ANALOGY_PARAMS[st.session_state.language]["length"],
                    index=1
                )
            with col_det:
                analogy_detail = st.radio(
                    get_text("detail_level"),
                    ANALOGY_PARAMS[st.session_state.language]["detail"],
                    index=0
                )
            with col_tone:
                analogy_tone = st.radio(
                    get_text("tone"),
                    ANALOGY_PARAMS[st.session_state.language]["tone"],
                    index=1
                )
            
            # Çıktı modülleri seçimi
            st.subheader(get_text("output_modules"))
            col_mod1, col_mod2, col_mod3 = st.columns(3)
            with col_mod1:
                generate_analogy_check = st.checkbox(get_text("generate_analogy"), value=True)
            with col_mod2:
                generate_story_check = st.checkbox(get_text("generate_story"), value=False)
            with col_mod3:
                generate_warnings_check = st.checkbox(get_text("generate_warnings"), value=False)
            
            st.markdown('</div>', unsafe_allow_html=True)
            submitted = st.form_submit_button(get_text("submit_button"), type="primary")
        
        if submitted and medical_topic.strip():
            if st.session_state.api_key and st.session_state.model:
                patient_profile = {
                    'age': patient_age,
                    'interest': patient_interest,
                    'gender': patient_gender,
                    'education': patient_education,
                    'job': patient_job
                }
                
                results = {}
                
                # Analoji üretimi
                if generate_analogy_check:
                    with st.spinner(get_text("generating_analogy")):
                        analogy_result = st.session_state.model.generate_analogy(
                            medical_topic, patient_profile, analogy_length, analogy_detail, analogy_tone
                        )
                        results['analogy'] = analogy_result
                    
                    st.markdown(f"<div class='result-card'><h4>🎯 {get_text('generated_analogy')}</h4></div>", unsafe_allow_html=True)
                    st.text_area("", value=analogy_result, height=200, key="analogy_output", label_visibility="collapsed")
                    
                    import urllib.parse
                    wa_body = urllib.parse.quote(f"Synapse Analoji:\n\n{analogy_result}")
                    wa_link = f"https://wa.me/?text={wa_body}"
                    st.markdown(f'<a href="{wa_link}" target="_blank" style="text-decoration:none;font-weight:600;">🟢 {get_text("whatsapp_share")}</a>', unsafe_allow_html=True)
                
                # Görsel hikaye üretimi
                if generate_story_check:
                    with st.spinner(get_text("generating_story")):
                        base_analogy = results.get('analogy', medical_topic)
                        story_result = st.session_state.model.generate_visual_story(
                            medical_topic, patient_profile, base_analogy
                        )
                        results['story'] = story_result
                    
                    st.markdown(f"<div class='story-card'><h4>📖 {get_text('visual_story_suggestion')}</h4></div>", unsafe_allow_html=True)
                    st.text_area("", value=story_result, height=250, key="story_output", label_visibility="collapsed")
                
                # Kelime uyarıları üretimi
                if generate_warnings_check:
                    with st.spinner(get_text("generating_warnings")):
                        warnings_result = st.session_state.model.generate_word_warnings(
                            medical_topic, patient_profile
                        )
                        results['warnings'] = warnings_result
                    
                    st.markdown(f"<div class='warning-card'><h4>⚠️ {get_text('word_usage_guide')}</h4></div>", unsafe_allow_html=True)
                    st.text_area("", value=warnings_result, height=200, key="warnings_output", label_visibility="collapsed")
                
                # Geçmişe kaydet
                new_entry = {
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'medical_topic': medical_topic,
                    'patient_profile': patient_profile,
                    'results': results
                }
                st.session_state.history.append(new_entry)
                
            else:
                st.error(get_text("error_no_api"))
        elif submitted:
            st.warning(get_text("error_no_topic"))

    with col2:
        st.header(get_text("history_queries"))
        
        if st.session_state.history:
            for i, entry in enumerate(reversed(st.session_state.history[-5:])):
                with st.expander(f"Sorgu {len(st.session_state.history) - i}: {entry['timestamp'][:10]}"):
                    st.write(f"**Konu:** {entry['medical_topic'][:50]}...")
                    st.write(f"**Hasta:** {entry['patient_profile']['age']}, {entry['patient_profile']['interest']}")
                    
                    # Üretilen modülleri göster
                    generated_modules = list(entry['results'].keys())
                    if generated_modules:
                        st.write(f"**Üretilen:** {', '.join(generated_modules)}")
        else:
            st.info(get_text("no_history"))

def main():
    create_animated_header()
    create_page_navigation()

    with st.sidebar:
        st.header(get_text("settings"))
        
        selected_language = st.selectbox(
            "🌍 Dil / Language",
            list(LANGUAGES.keys()),
            index=0 if st.session_state.language == "tr" else 1
        )
        st.session_state.language = LANGUAGES[selected_language]
        
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
        
        st.header(get_text("project_info"))
        st.markdown(f"""
        **{get_text('team')}:** YZTA-Bootcamp-Grup-134  
        **{get_text('sprint')}:** 2/3  
        **{get_text('version')}:** 2.2  
        **{get_text('developers')}:** Hasan BUDAK, Cemre Dağ, Yusuf Sait Sakoğlu, Aydan Kaya
        """)
        
        st.markdown("---")
        
        create_announcements_widget()
        st.markdown("---")
        create_events_widget()
        st.markdown("---")
        
        if st.session_state.history:
            st.header(get_text("usage_stats"))
            create_usage_chart()
        
        if st.button(get_text("clear_history")):
            st.session_state.history = []
            st.success("Geçmiş temizlendi!")

    if st.session_state.current_page == "home":
        create_home_page()
    elif st.session_state.current_page == "community":
        create_community_page()

if __name__ == "__main__":
    main()