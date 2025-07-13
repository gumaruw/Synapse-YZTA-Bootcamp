import streamlit as st
import google.generativeai as genai
import os
from datetime import datetime
import time
import json
from typing import Dict, List, Optional

# Sayfa yapılandırması
st.set_page_config(
    page_title="Synapse - Medikal Analoji Üreteci",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS stilleri
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .module-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .result-card {
        background: #e8f5e8;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #28a745;
        margin-top: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .warning-card {
        background: #fff3cd;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #ffc107;
        margin-top: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .error-card {
        background: #f8d7da;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #dc3545;
        margin-top: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .story-card {
        background: #e3f2fd;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2196f3;
        margin-top: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .stats-card {
        background: #f0f0f0;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .history-item {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        border-left: 3px solid #667eea;
    }
</style>
""", unsafe_allow_html=True)

# Session state başlatma
if 'history' not in st.session_state:
    st.session_state.history = []
if 'api_key' not in st.session_state:
    st.session_state.api_key = None
if 'model' not in st.session_state:
    st.session_state.model = None

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
    
    def generate_analogy(self, medical_topic: str, patient_profile: Dict) -> str:
        """Tıbbi analoji üret"""
        age_group = patient_profile.get('age', '')
        interest = patient_profile.get('interest', '')
        
        prompt = f"""
        Sen deneyimli bir doktor ve yaratıcı bir iletişim uzmanısın. 
        Görevevin karmaşık tıbbi konuları hastalar için anlaşılır analojiler haline getirmek.
        
        TIBBİ KONU: {medical_topic}
        HASTA YAŞI: {age_group}
        İLGİ ALANI: {interest}
        
        Lütfen bu tıbbi konuyu, hasta profiline uygun, basit ve anlaşılır bir analoji ile açıkla.
        
        Analojin:
        - Günlük yaşamdan örnekler içermeli
        - Hasta profiline uygun olmalı
        - Korku yaratmamalı, umut vermeli
        - Basit ve akılda kalıcı olmalı
        - Türkçe olmalı
        
        Analoji:
        """
        
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
    st.markdown("""
    <div class="main-header">
        <h1>🧠 Synapse</h1>
        <p>Yapay Zeka Destekli Medikal Analoji Üreteci</p>
        <p><i>Karmaşık tıbbi konuları basit analojilerle açıklayın</i></p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar - API Key ve Ayarlar
    with st.sidebar:
        st.header("⚙️ Ayarlar")
        
        # API Key girişi
        api_key = st.text_input(
            "Gemini API Key", 
            type="password", 
            value=st.session_state.api_key or "",
            help="Google AI Studio'dan aldığınız API anahtarını girin"
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
        st.header("📋 Proje Bilgileri")
        st.markdown("""
        **Takım:** YZTA-Bootcamp-Grup-134  
        **Sprint:** 2/3  
        **Versiyon:** 2.0  
        **Geliştirici:** Hasan BUDAK, Cemre Dağ, Yusuf Sait Sakoğlu
        """)
        
        st.markdown("---")
        
        # Kullanım istatistikleri
        st.header("📊 Kullanım İstatistikleri")
        st.markdown(f"""
        <div class="stats-card">
            <h4>Toplam Sorgu</h4>
            <h2>{len(st.session_state.history)}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="stats-card">
            <h4>Aktif Oturum</h4>
            <h3>{datetime.now().strftime('%H:%M')}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Geçmiş temizleme
        if st.button("🗑️ Geçmişi Temizle"):
            st.session_state.history = []
            st.success("Geçmiş temizlendi!")

    # Ana içerik alanı
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("🎯 Analoji Üretimi")
        
        # Form alanları
        with st.form("analogy_form"):
            st.markdown('<div class="module-card">', unsafe_allow_html=True)
            
            # Tıbbi konu
            medical_topic = st.text_area(
                "📝 Tıbbi Konu",
                placeholder="Örn: Diyabet Tip 1 - Pankreasın insülin üretememesi",
                height=100,
                help="Hastaya açıklamak istediğiniz tıbbi konuyu detaylı olarak yazın"
            )
            
            # Hasta profili
            col_age, col_interest = st.columns(2)
            with col_age:
                patient_age = st.selectbox(
                    "👤 Hasta Yaşı",
                    ["0-5 yaş", "6-12 yaş", "13-18 yaş", "19-65 yaş", "65+ yaş"],
                    help="Hastanın yaş grubunu seçin"
                )
            
            with col_interest:
                patient_interest = st.selectbox(
                    "🎨 İlgi Alanı",
                    ["Arabalar", "Hayvanlar", "Spor", "Müzik", "Bahçıvanlık", "Teknoloji", "Yemek", "Kitaplar"],
                    help="Hastanın ilgi alanını seçin"
                )
            
            # Modül seçimi
            st.subheader("📚 Çıktı Modülleri")
            col_mod1, col_mod2, col_mod3 = st.columns(3)
            
            with col_mod1:
                gen_analogy = st.checkbox("🔄 Analoji Üret", value=True)
            with col_mod2:
                gen_story = st.checkbox("📖 Görsel Hikaye")
            with col_mod3:
                gen_warnings = st.checkbox("⚠️ Kelime Uyarıları")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Gönder butonu
            submitted = st.form_submit_button("🚀 Analoji Üret", type="primary")
            
            if submitted:
                if not st.session_state.api_key:
                    st.error("❌ Lütfen önce API anahtarınızı girin!")
                elif not medical_topic:
                    st.error("❌ Lütfen bir tıbbi konu girin!")
                else:
                    # Loading animasyonu
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    try:
                        patient_profile = {
                            'age': patient_age,
                            'interest': patient_interest
                        }
                        
                        results = {}
                        
                        # Analoji üretimi
                        if gen_analogy:
                            status_text.text("🔄 Analoji üretiliyor...")
                            progress_bar.progress(30)
                            
                            analogy_result = st.session_state.model.generate_analogy(
                                medical_topic, patient_profile
                            )
                            results['analogy'] = analogy_result
                            
                            st.markdown(f"""
                            <div class="result-card">
                                <h4>🎯 Üretilen Analoji</h4>
                                <p>{analogy_result}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Görsel hikaye modülü
                        if gen_story:
                            status_text.text("📖 Görsel hikaye üretiliyor...")
                            progress_bar.progress(60)
                            
                            story_result = st.session_state.model.generate_visual_story(
                                medical_topic, patient_profile
                            )
                            results['story'] = story_result
                            
                            st.markdown(f"""
                            <div class="story-card">
                                <h4>📖 Görsel Hikaye Önerisi</h4>
                                <p>{story_result}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Kelime uyarıları
                        if gen_warnings:
                            status_text.text("⚠️ Kelime uyarıları üretiliyor...")
                            progress_bar.progress(90)
                            
                            warnings_result = st.session_state.model.generate_word_warnings(
                                medical_topic, patient_profile
                            )
                            results['warnings'] = warnings_result
                            
                            st.markdown(f"""
                            <div class="warning-card">
                                <h4>⚠️ Kelime Kullanım Rehberi</h4>
                                <p>{warnings_result}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Geçmişe kaydet
                        history_entry = {
                            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            'medical_topic': medical_topic,
                            'patient_profile': patient_profile,
                            'results': results
                        }
                        st.session_state.history.append(history_entry)
                        
                        progress_bar.progress(100)
                        status_text.text("✅ Tamamlandı!")
                        time.sleep(1)
                        progress_bar.empty()
                        status_text.empty()
                        
                    except Exception as e:
                        st.markdown(f"""
                        <div class="error-card">
                            <h4>❌ Hata</h4>
                            <p>Bir hata oluştu: {str(e)}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        progress_bar.empty()
                        status_text.empty()

    with col2:
        st.header("📚 Geçmiş Sorgular")
        
        if st.session_state.history:
            for i, entry in enumerate(reversed(st.session_state.history[-10:])):
                with st.expander(f"Sorgu {len(st.session_state.history) - i}: {entry['timestamp']}"):
                    st.write(f"**Konu:** {entry['medical_topic'][:50]}...")
                    st.write(f"**Hasta:** {entry['patient_profile']['age']}, {entry['patient_profile']['interest']}")
                    
                    if st.button(f"Tekrar Kullan {len(st.session_state.history) - i}", key=f"reuse_{i}"):
                        # Tekrar kullanma özelliği için state'i güncelleyelim
                        st.session_state.reuse_data = {
                            'topic': entry['medical_topic'],
                            'age': entry['patient_profile']['age'],
                            'interest': entry['patient_profile']['interest']
                        }
                        st.rerun()
        else:
            st.info("Henüz sorgu geçmişi yok.")
            
        st.markdown("---")
        
        # Yardım ve bilgi
        st.header("❓ Yardım")
        st.markdown("""
        **Nasıl kullanılır?**
        1. API anahtarınızı girin
        2. Tıbbi konuyu yazın
        3. Hasta profilini seçin
        4. İstediğiniz modülleri işaretleyin
        5. 'Analoji Üret' butonuna tıklayın
        
        **İpuçları:**
        - Tıbbi konuyu detaylı yazın
        - Hasta profilini doğru seçin
        - Birden fazla modül deneyebilirsiniz
        """)

if __name__ == "__main__":
    main()
