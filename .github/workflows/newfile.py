import streamlit as st

# Konfigirasyon paj mobil
st.set_page_config(page_title="Lucky6 Live Tracker", layout="centered")

if 'istorik' not in st.session_state:
    st.session_state['istorik'] = []

st.title("📊 Lucky 6 Live Tracker")
st.write("Paske sit la pa bay istorik, n ap kreye pa nou an an dirèk!")

# 1. Antre tiraj ki fèk soti a
nouvo_tiraj = st.text_input("Antre 37 boul ki fèk soti yo (separé ak espas):")

if st.button("Anrejistre Tiraj Sa a"):
    if nouvo_tiraj:
        chif_yo = [int(x) for x in nouvo_tiraj.split() if x.isdigit()]
        if len(chif_yo) > 0:
            st.session_state['istorik'].append(chif_yo)
            st.success("Tiraj anrejistre ak siksè!")
        else:
            st.error("Antre chif ki valab.")

# 2. Analiz Frekans
if len(st.session_state['istorik']) > 0:
    st.subheader("📈 Analiz Frekans an Dirèk")
    
    tout_boul = [b for t in st.session_state['istorik'] for b in t]
    frekans = {boul: tout_boul.count(boul) for boul in set(tout_boul)}
    
    # Triye pou jwenn 6 ki pi cho yo
    boul_cho = sorted(frekans.items(), key=lambda x: x[1], reverse=True)[:6]
    
    st.write("### 🎯 Pwochen 6 boul rekòmande:")
    rezilta_final = [str(b[0]) for b in boul_cho]
    st.markdwon(f"## **{', '.join(rezilta_final)}**")
    
    # Montre konbe tiraj ki nan memwa a
    st.info(f"Analiz baze sou {len(st.session_state['istorik'])} dènye tiraj ou antre yo.")

if st.button("Efase Tout Istorik"):
    st.session_state['istorik'] = []
    st.rerun()