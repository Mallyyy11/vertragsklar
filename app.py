import streamlit as st
from analyze_contract import analyze_contract

st.set_page_config(
    page_title="Vertragsklar",
    page_icon="📄",
)

st.title("📄 Vertragsklar")
st.subheader("Verträge verstehen – ohne Juristendeutsch")

st.markdown("""
Füge unten den Text deines Vertrags ein (z. B. Dienstleistungsvertrag, NDA, Angebot, AGB).
Du bekommst eine leicht verständliche Zusammenfassung mit Risiken, Fristen und Pflichten.

**Wichtig:** Das ist keine Rechtsberatung. Du bekommst eine sprachliche Erklärung.
""")

# Eingabefeld für Vertragstext
contract_input = st.text_area(
    "Dein Vertragstext",
    placeholder="👉 Copy & Paste den kompletten Vertrag hier rein …",
    height=250
)

analyze_button = st.button("Vertrag prüfen")

if analyze_button:
    if not contract_input.strip():
        st.error("Bitte füge erst einen Vertragstext ein.")
    else:
        with st.spinner("Analysiere Vertrag …"):
            result = analyze_contract(contract_input)

        st.markdown("### 📌 Ergebnis")
        st.write(result)

        st.markdown("---")
        st.caption("Hinweis: Dies ist keine Rechts- oder Steuerberatung.")
