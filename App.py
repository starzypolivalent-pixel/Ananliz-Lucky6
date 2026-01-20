# Ananliz-Lucky6
Chance Lucky 
import streamlit as st
import pandas as pd
import collections

st.set_page_config(page_title="Lucky6 Analyzer", layout="centered")

st.title("🎰 Lucky6 Analizè (ParyajPam)")
st.write("Antre 37 boul dènye tiraj la pou w jwenn 6 boul pwochen an.")

# 1. Antre Done
input_data = st.text_input("Kole 37 boul yo isit la (separe ak koma):", "")

if st.button("Kalkile 6 Boul Pwochen yo"):
    if input_data:
        try:
            # Netwaye done yo
            lis_boul = [int(n.strip()) for n in input_data.split(",") if n.strip()]
            
            if len(lis_boul) >= 37:
                # 2. Algoritm Frekans
                frekans = collections.Counter(lis_boul)
                
                # 3. Kalkile Gap (Nou simulate li sou 48 boul posib)
                tout_boul = list(range(1, 49))
                boul_ki_pa_soti = [b for b in tout_boul if b not in lis_boul]
                
                # 4. Seleksyon 6 boul "Smart"
                # Nou pran 4 nan sa ki soti plis yo, ak 2 nan sa ki gen tan yo pa soti
                cho = [b for b, f in frekans.most_common(4)]
                fret = boul_ki_pa_soti[:2]
                rezilta_final = sorted(cho + fret)
                
                # Afiche Rezilta
                st.success(f"### 🎯 Pwochen 6 Boul: {rezilta_final}")
                
                # Tablo Frekans pou w wè detay yo
                st.write("---")
                st.subheader("Analiz detay:")
                df = pd.DataFrame(frekans.items(), columns=['Boul', 'Fwa li soti'])
                st.bar_chart(df.set_index('Boul'))
            else:
                st.error(f"Ou mete sèlman {len(lis_boul)} boul. Manke {37 - len(lis_boul)}.")
        except Exception as e:
            st.error("Format la pa bon. Mete nimewo sèlman ak koma.")
