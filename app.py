import streamlit as st
from analyze_contract import analyze_contract
from PyPDF2 import PdfReader

# Meta / Kopfbereich
st.set_page_config(page_title="Vertragsklar", page_icon="📄")

st.title("📄 Vertragsklar")
st.markdown("### Dein smarter Vertrags-Erklärer 🧠💬")
st.markdown("Verstehe Verträge einfach — klar, strukturiert und ohne Juristendeutsch.")

st.markdown("""
**Was du hier machen kannst:**
- Vertragstext reinkopieren **oder**
- PDF hochladen (z. B. Dienstleistungsvertrag, Mietvertrag, NDA)

Du bekommst eine strukturierte Zusammenfassung:
1. Worum geht es?
2. Was musst du tun?
3. Was muss die Gegenseite tun?
4. Geld / Strafen / Haftung
5. Laufzeit / Kündigung
6. Dinge, auf die du achten solltest

*Hinweis: Das ist keine Rechtsberatung, sondern eine sprachliche Erklärung.*
""")

# Tabs oben: Text / PDF
tab_text, tab_pdf = st.tabs(["✍️ Vertrag als Text einfügen", "📄 Vertrag als PDF hochladen"])

# --- TAB 1: TEXT EINFÜGEN ---
with tab_text:
    st.subheader("✍️ Text einfügen")
    contract_input = st.text_area(
        "Dein Vertragstext",
        placeholder="👉 Copy & Paste den kompletten Vertrag hier rein …",
        height=250
    )

    if st.button("Vertrag prüfen (Text)"):
        if not contract_input.strip():
            st.error("Bitte füge erst einen Vertragstext ein.")
        else:
            with st.spinner("Analysiere Vertrag …"):
                result = analyze_contract(contract_input)

            st.markdown("### 📌 Ergebnis")
            st.write(result)

# --- TAB 2: PDF HOCHLADEN ---
with tab_pdf:
    st.subheader("📄 PDF hochladen")
    uploaded_file = st.file_uploader(
        "Lade dein Vertrags-PDF hoch",
        type=["pdf"]
    )

    if st.button("Vertrag prüfen (PDF)"):
        if not uploaded_file:
            st.error("Bitte lade zuerst eine PDF hoch.")
        else:
            try:
                pdf_reader = PdfReader(uploaded_file)
                all_text = ""
                for page in pdf_reader.pages:
                    text = page.extract_text() or ""
                    all_text += text + "\n"

                if not all_text.strip():
                    st.error("Ich konnte keinen Text aus der PDF lesen. Manche PDFs sind nur gescannte Bilder ohne echten Text.")
                else:
                    with st.spinner("Analysiere Vertrag …"):
                        result = analyze_contract(all_text)

                    st.markdown("### 📌 Ergebnis")
                    st.write(result)

            except Exception as e:
                st.error("Beim Lesen der PDF ist ein Fehler passiert 😕")
                st.text(str(e))

# Footer / Hinweis
st.markdown("---")
st.caption("⚠️ Hinweis: Dies ist keine Rechtsberatung. Du erhältst eine sprachliche Zusammenfassung deines Vertragstextes.")
st.caption("© 2025 Vertragsklar – KI-Verständnis für deine Verträge.")
