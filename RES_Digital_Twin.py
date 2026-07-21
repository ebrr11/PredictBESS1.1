import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium
import random

# Sayfa Konfigürasyonu
st.set_page_config(
    page_title="PredictBESS | Enerjisa Digital Twin",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Session State Kontrolü
if "santral" not in st.session_state:
    st.session_state["santral"] = "Çanakkale RES"

# Yan Menü
st.sidebar.title("⚡ PredictBESS")
st.sidebar.caption("Enerjisa Digital Twin Platformu")

page = st.sidebar.radio(
    "📂 Menü",
    [
        "🏠 Ana Sayfa",
        "📋 Proje Özeti",
        "⚙️ Türbin Sağlığı & RUL",
        "🔋 Hibrit Batarya Sistemi",
        "📈 Yatırım Optimizasyonu",
        "🌱 Sürdürülebilirlik"
    ]
)

# ==========================================================
# 🎨 ARKA PLAN YÖNETİMİ (Sadece Ana Sayfada Türbin Görseli)
# ==========================================================
if page == "🏠 Ana Sayfa":
    bg_image_url = "https://images.unsplash.com/photo-1466611653911-95081537e5b7?q=80&w=2000&auto=format&fit=crop"
    
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(10, 25, 50, 0.65), rgba(10, 25, 50, 0.85)), url('{bg_image_url}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        h1, h2, h3, h4, .stMarkdown, .stMetric label, div[data-testid="stMetricValue"] {{
            color: #ffffff !important;
            text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
        }}
        </style>
    """, unsafe_allow_html=True)

# ==========================================================
# 🏠 ANA SAYFA (SADECE BAŞLIK VE GÖRSEL)
# ==========================================================
if page == "🏠 Ana Sayfa":
    
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    
    # Devasa PredictBESS Başlığı
    st.markdown("""
        <h1 style='text-align: center; font-size: 90px; font-weight: 900; letter-spacing: 4px; margin-bottom: 0px;'>
            ⚡ PREDICTBESS ⚡
        </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h3 style='text-align: center; font-size: 26px; font-weight: 300; margin-top: 10px; color: #d0e8ff; letter-spacing: 1px;'>
            Yapay Zekâ Destekli Hibrit Enerji Depolama ve Türbin Ömür Yönetim Platformu
        </h3>
    """, unsafe_allow_html=True)

# ==========================================================
# 📋 PROJE ÖZETİ
# ==========================================================
elif page == "📋 Proje Özeti":

    st.title("📋 Proje Özeti & Platform Yetenekleri")
    st.write("PredictBESS platformunun temel amaçları, analitik yetenekleri ve mimari yapısı aşağıda özetlenmiştir.")

    st.divider()

    st.subheader("🎯 Platform Yetenekleri & Amaç")
    st.write("""
    • **Türbin Sağlığı:** Titreşim, yağ ve sıcaklık analizleri ile anlık durum takibi.
    • **Kalan Ömür (RUL) Tahmini:** Yapay zekâ tabanlı makine öğrenmesi modelleri.
    • **Hibrit Depolama:** Süper kapasitör, LFP ve Demir-Hava batarya entegrasyonu.
    • **Şebeke Kararlılığı:** Anlık frekans regülasyonu ve güç kalitesi artırımı.
    • **Sürdürülebilir Dönüşüm:** Karbon emisyon azaltımı ve ESG uyumluluğu.
    """)

    st.divider()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("⚙️ Türbin Sayısı", "73")
    c2.metric("🔋 Batarya Teknolojisi", "3")
    c3.metric("🤖 AI Modeli", "Aktif")
    c4.metric("📈 Geri Ödeme", "4.83 Yıl")

    st.divider()

    st.subheader("🔋 Hibrit Depolama Mimarisi")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("""
        ### ⚡ Süper Kapasitör
        • Frekans desteği
        • Milisaniye tepki süresi
        • Ani yük değişim yönetimi
        """)

    with col2:
        st.info("""
        ### 🔋 LFP Batarya
        • Günlük enerji yönetimi
        • Yüksek çevrim ömrü
        • Güvenli operasyon
        """)

    with col3:
        st.warning("""
        ### 🏭 Demir-Hava
        • Uzun süreli (sezonsal) depolama
        • Düşük yatırım maliyeti
        • Yüksek depolama kapasitesi
        """)

# ==========================================================
# ⚙️ TÜRBİN SAĞLIĞI & RUL
# ==========================================================
elif page == "⚙️ Türbin Sağlığı & RUL":

    st.title("⚙️ Türbin Sağlığı ve Ömür Tahmini")

    santral = st.radio(
        "Santral Seçin",
        ["Çanakkale RES", "Uygar RES"],
        horizontal=True
    )
    st.session_state["santral"] = santral

    st.divider()

    k1, k2 = st.columns(2)
    with k1:
        st.info("""
        ### Çanakkale RES
        • **Kurulu Güç:** 29.9 MW  
        • **Türbin Sayısı:** 13  
        • **Yıllık Üretim:** 91.6 GWh  
        """)

    with k2:
        st.info("""
        ### Uygar RES
        • **Kurulu Güç:** 250 MW  
        • **Türbin Sayısı:** 60  
        • **Konum:** İzmir / Bergama  
        """)

    canakkale_data = {
        "T01": [92, 14.8, 2.1, 110, 61, 0.21, 8],
        "T02": [88, 12.7, 2.8, 130, 63, 0.26, 9],
        "T03": [83, 10.1, 3.5, 180, 66, 0.31, 11],
        "T04": [61, 3.2, 8.3, 470, 84, 0.74, 19],
        "T05": [78, 8.4, 4.2, 220, 71, 0.43, 12],
        "T06": [91, 15.2, 2.0, 105, 60, 0.19, 7],
        "T07": [75, 7.1, 4.8, 260, 73, 0.49, 13],
        "T08": [69, 5.4, 5.6, 310, 77, 0.58, 15],
        "T09": [94, 16.3, 1.8, 95, 58, 0.15, 7],
        "T10": [86, 11.8, 3.1, 150, 65, 0.29, 10],
        "T11": [72, 6.0, 5.2, 290, 76, 0.61, 14],
        "T12": [89, 13.5, 2.7, 125, 62, 0.24, 8],
        "T13": [58, 2.4, 8.7, 520, 86, 0.81, 21]
    }

    if santral == "Çanakkale RES":
        kurulu_guc = 29.9
        turbin_sayisi = 13
        yillik_uretim = 91.6
        kritik_turbin = 2
        ortalama_rul = 9.8
        saglikli_sayisi = 8
        warning_sayisi = 3
        critical_sayisi = 2
    else:
        kurulu_guc = 250
        turbin_sayisi = 60
        yillik_uretim = 850
        kritik_turbin = 3
        ortalama_rul = 17.2
        saglikli_sayisi = 48
        warning_sayisi = 9
        critical_sayisi = 3

    st.divider()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Kurulu Güç", f"{kurulu_guc} MW")
    c2.metric("Türbin Sayısı", turbin_sayisi)
    c3.metric("Kritik Türbin", kritik_turbin)
    c4.metric("Ortalama RUL", f"{ortalama_rul} yıl")

    st.progress(min(int(ortalama_rul * 4), 100))
    st.caption("Filo Genel Sağlık Endeksi")

    st.divider()
    st.subheader("📊 Filo Özeti")

    f1, f2, f3 = st.columns(3)
    f1.success(f"🟢 Sağlıklı Türbin\n\n### {saglikli_sayisi}")
    f2.warning(f"🟡 İzleme Gereken\n\n### {warning_sayisi}")
    f3.error(f"🔴 Kritik Türbin\n\n### {critical_sayisi}")

    st.divider()

    st.subheader("🚨 Kritik Türbinler")
    if santral == "Çanakkale RES":
        st.error("🔴 T13 | Sağlık: 58 | RUL: 2.4 yıl")
        st.error("🔴 T04 | Sağlık: 61 | RUL: 3.2 yıl")
    else:
        st.error("🔴 U07 | Sağlık: 55 | RUL: 4.1 yıl")
        st.error("🔴 U21 | Sağlık: 52 | RUL: 3.8 yıl")
        st.error("🔴 U43 | Sağlık: 57 | RUL: 4.5 yıl")

    st.divider()

    # 🗺️ GERÇEK UYDU/FOTOĞRAF GÖRÜNTÜLÜ HARİTA (Esri World Imagery)
    st.subheader("🗺️ Santral Coğrafi Haritası (Uydu Görüntüsü)")
    
    satellite_tile = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
    tile_attr = "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community"

    if santral == "Çanakkale RES":
        m = folium.Map(
            location=[39.8690, 26.2230], 
            zoom_start=14, 
            tiles=satellite_tile, 
            attr=tile_attr
        )
        turbines = [
            ("T01", 39.8731, 26.2179), ("T02", 39.8747, 26.2259), ("T03", 39.8744, 26.2248),
            ("T04", 39.8771, 26.2281), ("T05", 39.8666, 26.2070), ("T06", 39.8666, 26.2119),
            ("T07", 39.8665, 26.2162), ("T08", 39.8654, 26.2198), ("T09", 39.8627, 26.2229),
            ("T10", 39.8643, 26.2262), ("T11", 39.8649, 26.2297), ("T12", 39.8615, 26.2328),
            ("T13", 39.8672, 26.2389)
        ]
        critical_list = ["T04", "T13"]
        warning_list = ["T07", "T08", "T11"]
    else:
        m = folium.Map(
            location=[39.268, 27.405], 
            zoom_start=14, 
            tiles=satellite_tile, 
            attr=tile_attr
        )
        turbines = [
            ("U01", 39.273640, 27.417121), ("U02", 39.273277, 27.413236), ("U03", 39.274661, 27.409466),
            ("U04", 39.275956, 27.406199), ("U05", 39.267273, 27.402777), ("U06", 39.266477, 27.392957),
            ("U07", 39.262325, 27.393297), ("U08", 39.260591, 27.401122), ("U09", 39.260151, 27.405387)
        ]
        critical_list = ["U07"]
        warning_list = ["U05", "U06"]

    for name, lat, lon in turbines:
        if name in critical_list:
            color = "red"
        elif name in warning_list:
            color = "orange"
        else:
            color = "green"
            
        folium.Marker(
            [lat, lon], 
            popup=f"<b>Türbin:</b> {name}", 
            tooltip=name, 
            icon=folium.Icon(color=color, icon="info-sign")
        ).add_to(m)

    st_folium(m, width=1100, height=450)

    st.divider()

    # DETAYLI TÜRBİN ANALİZİ
    st.subheader("🎯 Türbin Detay Analizi")
    
    if santral == "Çanakkale RES":
        selected_name = st.selectbox("Analiz Edilecek Türbini Seçin", list(canakkale_data.keys()))
        Saglik, rul, vib, oil, temp, miner, turb = canakkale_data[selected_name]
    else:
        selected_name = st.selectbox("Analiz Edilecek Türbini Seçin", [f"U{i:02d}" for i in range(1, 61)])
        Saglik = random.randint(60, 95)
        rul = round(random.uniform(5, 22), 1)
        vib = round(random.uniform(1, 8), 1)
        oil = random.randint(80, 350)
        temp = random.randint(55, 80)
        miner = round(random.uniform(0.15, 0.75), 2)
        turb = random.randint(6, 20)

    st.info(f"Seçilen Türbin: **{selected_name}**")

    st.write("### 📊 Türbin Durumu")
    st.progress(Saglik)

    tc1, tc2, tc3 = st.columns(3)
    if Saglik >= 80:
        tc1.success(f"Sağlık Skoru: %{Saglik}")
        tc3.success("🟢 Sağlıklı")
    elif Saglik >= 65:
        tc1.warning(f"Sağlık Skoru: %{Saglik}")
        tc3.warning("🟡 İzleme Altında")
    else:
        tc1.error(f"Sağlık Skoru: %{Saglik}")
        tc3.error("🔴 Kritik")

    tc2.metric("RUL (Kalan Ömür)", f"{rul} Yıl")

    st.divider()

    st.write("### 🔧 Sensör Verileri")
    sc1, sc2, sc3, sc4, sc5 = st.columns(5)
    sc1.metric("Titreşim", f"{vib} mm/s")
    sc2.metric("Yağ Partikül", f"{oil} ppm")
    sc3.metric("Sıcaklık", f"{temp} °C")
    sc4.metric("Yorulma Hasarı", miner)
    sc5.metric("Türbülans", f"%{turb}")

    st.divider()

    st.write("### 🤖 AI Karar Motoru")

    vib_loss = min(vib * 2, 20)
    oil_loss = min(oil / 30, 20)
    temp_loss = max((temp - 60) * 0.8, 0)
    miner_loss = miner * 30
    turb_loss = turb * 0.5

    Saglik_ai = max(0, round(100 - vib_loss - oil_loss - temp_loss - miner_loss - turb_loss))

    st.write(f"• Titreşim Etkisi: **-{vib_loss:.1f}**")
    st.write(f"• Yağ Aşınması: **-{oil_loss:.1f}**")
    st.write(f"• Sıcaklık Etkisi: **-{temp_loss:.1f}**")
    st.write(f"• Yorulma Hasarı: **-{miner_loss:.1f}**")
    st.write(f"• Türbülans Etkisi: **-{turb_loss:.1f}**")

    st.metric("AI Hesaplanan Sağlık Skoru", Saglik_ai)

    if Saglik_ai < 50:
        st.error("🔴 REPOWERING ÖNERİLİYOR")
    elif Saglik_ai < 70:
        st.warning("🟡 YAKIN TAKİP GEREKLİ")
    else:
        st.success("🟢 NORMAL OPERASYON")

    st.divider()

    st.write("### 📡 Türbin Sağlık Profili (Radar)")
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[
            max(0, 100 - vib * 10),
            max(0, 100 - oil / 5),
            max(0, 100 - temp),
            max(0, 100 - miner * 100),
            max(0, 100 - turb * 4)
        ],
        theta=["Titreşim", "Yağ", "Sıcaklık", "Yorulma", "Türbülans"],
        fill="toself"
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100])
        ),
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.write("### 📈 RUL Karşılaştırması")
    if santral == "Çanakkale RES":
        chart_df = pd.DataFrame({
            "Türbin": list(canakkale_data.keys()),
            "RUL": [v[1] for v in canakkale_data.values()]
        })
    else:
        chart_df = pd.DataFrame({
            "Türbin": [f"U{i:02d}" for i in range(1, 61)],
            "RUL": [10 + (i % 12) for i in range(1, 61)]
        })

    fig_bar = px.bar(chart_df, x="Türbin", y="RUL", color="RUL", color_continuous_scale="Viridis")
    st.plotly_chart(fig_bar, use_container_width=True)

# ==========================================================
# 🔋 HİBRİT BATARYA SİSTEMİ
# ==========================================================
elif page == "🔋 Hibrit Batarya Sistemi":

    st.title("🔋 Hibrit Batarya Sistemi")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("""
        ### ⚡ Süper Kapasitör
        • Milisaniye tepki süresi  
        • Frekans regülasyonu  
        • Ani yük değişimleri  
        """)

    with col2:
        st.info("""
        ### 🔋 LFP Batarya
        • Günlük enerji yönetimi  
        • Yüksek çevrim ömrü  
        • Güvenli çalışma  
        """)

    with col3:
        st.warning("""
        ### 🏭 Demir-Hava
        • Uzun süreli depolama  
        • Düşük maliyet  
        • Yüksek kapasite  
        """)

# ==========================================================
# 📈 YATIRIM OPTİMİZASYONU
# ==========================================================
elif page == "📈 Yatırım Optimizasyonu":

    st.title("📈 Yatırım Optimizasyonu")
    santral = st.session_state.get("santral", "Çanakkale RES")
    st.info(f"Analiz Edilen Santral: **{santral}**")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("CAPEX", "27.46 M$")
    c2.metric("Yıllık OPEX", "494 K$")
    c3.metric("Net Kazanç", "5.68 M$")
    c4.metric("Payback", "4.83 Yıl")

    st.divider()

    st.subheader("📊 Amortisman & Nakit Akış Analizi")
    years = [f"Yıl {i}" for i in range(1, 11)]
    cash_flow = [-27.46 + (i * 5.68) for i in range(1, 11)]
    payback_df = pd.DataFrame({"Yıllar": years, "Kümülatif Nakit Akışı (M$)": cash_flow})
    
    fig_payback = px.line(payback_df, x="Yıllar", y="Kümülatif Nakit Akışı (M$)", markers=True)
    fig_payback.add_hline(y=0, line_dash="dash", line_color="red", annotation_text="Başa Baş Noktası (Payback)")
    st.plotly_chart(fig_payback, use_container_width=True)

# ==========================================================
# 🌱 SÜRDÜRÜLEBİLİRLİK
# ==========================================================
elif page == "🌱 Sürdürülebilirlik":

    st.title("🌱 Sürdürülebilirlik")
    santral = st.session_state.get("santral", "Çanakkale RES")

    if santral == "Çanakkale RES":
        co2 = "2.400"
        enerji = "65"
    else:
        co2 = "11.000"
        enerji = "300"

    a, b, c = st.columns(3)
    a.metric("CO₂ Azaltımı", f"{co2} ton/yıl")
    b.metric("Yıllık Üretim", f"{enerji} GWh")
    c.metric("Yenilenebilir Enerji", "%100")

    st.divider()

    st.subheader("🌍 Birleşmiş Milletler Hedefleri")

    st.success("""
    ### SDG 7: Erişilebilir ve Temiz Enerji
    Yenilenebilir enerji üretimini artırarak şebekeye kesintisiz ve temiz güç sağlar.
    """)

    st.info("""
    ### SDG 9: Sanayi, Yenilikçilik ve Altyapı
    Yapay zekâ ve hibrit depolama ile akıllı şebeke altyapılarını destekler.
    """)

    st.warning("""
    ### SDG 13: İklim Eylemi
    Fosil yakıt bağımlılığını ve karbon emisyonlarını doğrudan azaltır.
    """)