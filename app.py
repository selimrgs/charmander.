import streamlit as st
import pandas as pd

# 1. BOLUM: BITCOIN HESAPLAMA
st.title("Bitcoin TL Cevirici")
kur = st.number_input("Guncel BTC Kuru:", value=2150000)
btc_miktar = st.number_input("BTC Miktari:", min_value=0.0, format="%.6f")

if btc_miktar > 0:
    st.write("Sonuc:", btc_miktar * kur, "TL")

st.markdown("---")

# 2. BOLUM: SIFRE ANALIZI
st.title("Sifre Analiz Sistemi")
sifre = st.text_input("Sifre giriniz:", type="password")

if sifre:
    puan = 0
    if len(sifre) >= 8: puan += 1
    if any(c.isupper() for c in sifre): puan += 1
    if any(c.islower() for c in sifre): puan += 1
    if any(c.isdigit() for c in sifre): puan += 1
    if any(c in "!@#$%^&*()_+-=" for c in sifre): puan += 1

    if puan <= 2:
        st.write("Durum: Charmander")
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png", width=200)
    elif 3 <= puan <= 4:
        st.write("Durum: Charizard")
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png", width=250)
    else:
        st.write("Durum: Mega Charizard X")
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/10059.png", width=300)

st.markdown("---")

# 3. BOLUM: HAL FIYAT HESAPLAMA
st.title("Hal Fiyat Hesaplama")
site_url = st.text_input("Fiyat listesi URL:")

if site_url:
    try:
        veriler = pd.read_html(site_url)
        st.dataframe(veriler[0])
        
        secili_fiyat = st.number_input("Birim Fiyat (Siteden bakip girin):", min_value=0.0)
        kilo = st.number_input("Kilo:", min_value=0.0)
        
        if st.button("Hesapla"):
            st.write("Toplam:", secili_fiyat * kilo, "TL")
    except:
        st.write("Veri cekilemedi.")
