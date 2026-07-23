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
    c1.metric("⚙️ Toplam Türbin Sayısı", "73")
    c2.metric("🔋 Batarya Teknolojisi", "3 Katmanlı")
    c3.metric("🤖 AI Modeli", "Aktif")


    st.divider()

    st.subheader("🔋 Hibrit Depolama Mimarisi (Uygar RES)")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("""
        ### ⚡ Süper Kapasitör
        • Milisaniye tepki süresi  
        • Sentetik atalet (RoCoF)  
        • Anlık yük sarsıntı yönetimi  
        """)

    with col2:
        st.info("""
        ### 🔋 LFP Batarya
        • PFK / SFK Yan hizmetler  
        • Yüksek çevrim ve güç  
        • 2 saatlik hızlı deşarj  
        """)

    with col3:
        st.warning("""
        ### 🏭 Metal-Hava LDES
        • 24 saatlik uzun süreli depolama  
        • Çok düşük birim maliyet 
        • Rüzgârsız gün döngü yönetimi  
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
        • **Türbin Sayısı:** 13 Türbin  
        • **Yıllık Üretim:** 91.6 GWh  
        """)

    with k2:
        st.info("""
        ### Uygar RES (35 MW Hibrit BESS Entegre)
        • **Kurulu Güç:** 250 MW  
        • **Türbin Sayısı:** 60 Türbin  
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

    uygar_data = {
        f"U{i:02d}": [random.randint(70, 95), round(random.uniform(5.0, 18.0), 1), round(random.uniform(1.5, 5.0), 1), random.randint(100, 300), random.randint(60, 75), round(random.uniform(0.2, 0.5), 2), random.randint(6, 15)] for i in range(1, 61)
    }

    aktif_veri = canakkale_data if santral == "Çanakkale RES" else uygar_data

    if santral == "Çanakkale RES":
        kurulu_guc = 29.9
        turbin_sayisi = 13
        ortalama_rul = 9.8
        saglikli_sayisi = 8
        warning_sayisi = 3
        critical_sayisi = 2
    else:
        kurulu_guc = 250
        turbin_sayisi = 60
        ortalama_rul = 17.2
        saglikli_sayisi = 48
        warning_sayisi = 9
        critical_sayisi = 3

    st.divider()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Kurulu Güç", f"{kurulu_guc} MW")
    c2.metric("Türbin Sayısı", turbin_sayisi)
    c3.metric("Kritik Türbin", critical_sayisi)
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

    # 1. HARİTA BÖLÜMÜ (Sadece tam ve kesin verilen Çanakkale 13 türbin ve Uygar örnek koordinat listesi kullanıldı)
    st.subheader("🗺️ Santral Coğrafi Haritası ve İnteraktif Türbin Seçimi")
    satellite_tile = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
    tile_attr = "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community"

    if santral == "Çanakkale RES":
        map_center = [39.8690, 26.2230]
        # İlk kodda net olarak verilen 13 Çanakkale türbin koordinat listesi
        turbines = [
            ("T01", 39.8731, 26.2179, "Sağlıklı"),
            ("T02", 39.8710, 26.2195, "Sağlıklı"),
            ("T03", 39.8695, 26.2210, "Sağlıklı"),
            ("T04", 39.8771, 26.2281, "Kritik"),
            ("T05", 39.8650, 26.2250, "Sağlıklı"),
            ("T06", 39.8720, 26.2150, "Sağlıklı"),
            ("T07", 39.8630, 26.2290, "İzleme"),
            ("T08", 39.8610, 26.2310, "İzleme"),
            ("T09", 39.8740, 26.2130, "Sağlıklı"),
            ("T10", 39.8660, 26.2200, "Sağlıklı"),
            ("T11", 39.8590, 26.2340, "İzleme"),
            ("T12", 39.8700, 26.2180, "Sağlıklı"),
            ("T13", 39.8672, 26.2389, "Kritik")
        ]
    else:
        map_center = [39.268, 27.405]
        # İlk kodda Uygar RES için verilen temel örnek referans koordinat noktaları
        turbines = [
            ("U01", 39.2736, 27.4171, "Sağlıklı"),
            ("U07", 39.2623, 27.3932, "Kritik"),
            ("U21", 39.2550, 27.3900, "Kritik"),
            ("U12", 39.2680, 27.4050, "İzleme"),
            ("U30", 39.2700, 27.4100, "Sağlıklı")
        ]

    m = folium.Map(location=map_center, zoom_start=13, tiles=satellite_tile, attr=tile_attr)

    for name, lat, lon, durum in turbines:
        if durum == "Kritik":
            color = "red"
        elif durum == "İzleme":
            color = "orange"
        else:
            color = "green"
            
        folium.Marker(
            [lat, lon], 
            popup=f"<b>Türbin:</b> {name}<br><b>Durum:</b> {durum}", 
            tooltip=f"{name} ({durum})", 
            icon=folium.Icon(color=color, icon="info-sign")
        ).add_to(m)

    map_data = st_folium(m, width=1100, height=450)

    # Harita üzerinde tıklanan noktaya göre türbin seçimi entegrasyonu
    secilen_turbin = list(aktif_veri.keys())[0]
    if map_data and map_data.get("last_clicked"):
        clicked_lat = map_data["last_clicked"]["lat"]
        clicked_lon = map_data["last_clicked"]["lng"]
        
        min_dist = float("inf")
        closest_turbine = secilen_turbin
        for name, lat, lon, durum in turbines:
            dist = (lat - clicked_lat)**2 + (lon - clicked_lon)**2
            if dist < min_dist:
                min_dist = dist
                closest_turbine = name
        if min_dist < 0.005:
            secilen_turbin = closest_turbine

    st.divider()

    # 2. TÜRBAZLI DETAY VE SEÇİM BÖLÜMÜ
    st.subheader("🔍 Türbin Bazlı Detay ve RUL Analizi")
    
    turbin_listesi = list(aktif_veri.keys())
    secilen_index = turbin_listesi.index(secilen_turbin) if secilen_turbin in turbin_listesi else 0
    
    secilen_turbin = st.selectbox("İncelemek İçin Türbin Seçin", turbin_listesi, index=secilen_index)
    t_vals = aktif_veri[secilen_turbin]

    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Sağlık Skoru", f"{t_vals[0]} / 100")
    col_b.metric("Kalan Ömür (RUL)", f"{t_vals[6]} Yıl")
    col_c.metric("Titreşim Seviyesi", f"{t_vals[3]} mm/s")

    st.divider()

    # 3. RUL GRAFİĞİ BÖLÜMÜ
    st.subheader("📈 Tüm Türbinler RUL (Kalan Ömür) Karşılaştırma Grafiği")
    df_chart = pd.DataFrame(
        [{"Türbin": k, "RUL (Yıl)": v[6], "Sağlık Skoru": v[0]} for k, v in aktif_veri.items()]
    )
    fig = px.bar(
        df_chart, 
        x="Türbin", 
        y="RUL (Yıl)", 
        color="Sağlık Skoru", 
        color_continuous_scale="Viridis",
        text="RUL (Yıl)"
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.1)")
    )
    st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# 🔋 HİBRİT BATARYA SİSTEMİ
# ==========================================================
elif page == "🔋 Hibrit Batarya Sistemi":

    st.title("🔋 Hibrit Batarya Sistemi (Uygar RES)")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("""
        ### ⚡ Süper Kapasitör 
        • Milisaniye tepki süresi  
        • Frekans regülasyonu  
        • Sentetik atalet  
        """)

    with col2:
        st.info("""
        ### 🔋 LFP Batarya 
        • PFK / SFK Yan hizmetler  
        • Yüksek çevrim ömrü  
        • 2 saatlik hızlı deşarj  
        """)

    with col3:
        st.warning("""
        ### 🏭 Metal-Hava LDES 
        • 24 saat kesintisiz depolama  
        • Çok düşük birim maliyet  
        • Rüzgârsız gün emniyeti  
        """)

    st.divider()


# ==========================================================
# 🌱 SÜRDÜRÜLEBİLİRLİK
# ==========================================================
elif page == "🌱 Sürdürülebilirlik":

    st.title("🌱 Sürdürülebilirlik & ESG Performansı")
    santral = st.session_state.get("santral", "Çanakkale RES")

    if santral == "Çanakkale RES":
        co2 = "2.400"
        enerji = "65"
    else:
        co2 = "11.000"
        enerji = "850"

    a, b, c = st.columns(3)
    a.metric("CO₂ Azaltımı", f"{co2} ton/yıl")
    b.metric("Yıllık Üretim", f"{enerji} GWh")
    c.metric("Yenilenebilir Enerji", "%100")

    st.divider()

    st.subheader("🌍 Birleşmiş Milletler Sürdürülebilir Kalkınma Hedefleri")

    st.success("""
    ### SDG 7: Erişilebilir ve Temiz Enerji
    Yenilenebilir enerji üretimini hibrit depolama ile destekleyerek şebekeye kesintisiz güç sağlar.
    """)

    st.info("""
    ### SDG 9: Sanayi, Yenilikçilik ve Altyapı
    Yapay zekâ tabanlı dijital ikiz ve 3 katmanlı gelişmiş batarya altyapılarını entegre eder.
    """)

    st.warning("""
    ### SDG 13: İklim Eylemi
    Fosil yakıt bağımlılığını azaltarak karbon emisyonlarını kalıcı olarak düşürür.
    """)