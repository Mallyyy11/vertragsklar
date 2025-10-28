import streamlit as st
from analyze_contract import analyze_contract

st.set_page_config(page_title="Vertragsklar", page_icon="📄")

st.title("📄 Vertragsklar")
st.markdown("### Dein smarter Vertrags-Erklärer 🧠💬")
st.markdown("Verstehe Verträge einfach — klar, strukturiert und ohne Juristendeutsch.")

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
        st.caption("⚠️ Hinweis: Dies ist keine Rechtsberatung, sondern nur eine sprachliche Zusammenfassung deines Vertragstextes.")
        st.caption("© 2025 Vertragsklar – KI-Verständnis für deine Verträge.")
