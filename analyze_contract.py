from openai import OpenAI
from dotenv import load_dotenv
import os
from textwrap import dedent

# Lädt den API-Key aus .env und baut den Client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_contract(contract_text: str) -> str:
    """
    Nimmt den Inhalt eines Vertrags (als Text) und gibt eine leicht verständliche,
    strukturierte Zusammenfassung zurück.
    """

    # Sicherheitsnetz: falls jemand aus Versehen leeren Text schickt
    if not contract_text or contract_text.strip() == "":
        return "Kein Vertragstext erkannt. Bitte füge den kompletten Text ein."

    # Prompt an die KI
    system_msg = dedent("""
        Du hilfst dabei, Verträge in einfachem, verständlichem Deutsch zu erklären.
        Du bist KEIN Rechtsanwalt. Du gibst keine rechtliche oder steuerliche Beratung.
        Du erklärst nur, was im Vertrag drinsteht, in Alltagssprache.

        Wichtig:
        - Sprich die Nutzerin / den Nutzer mit "du" an.
        - Mach es klar, knapp, ohne Juristendeutsch.
        - Markiere kritische Stellen klar als "⚠ Achtung:".
        - Antworte IMMER in der folgenden Struktur:

        1. Kurz zusammengefasst
        2. Deine Pflichten
        3. Pflichten der anderen Partei
        4. Geld / Haftung / Strafen
        5. Laufzeit & Kündigung
        6. Dinge, die du prüfen solltest

        Wenn eine Kategorie im Text nicht vorkommt, schreib "nicht klar geregelt".
    """)

    user_msg = f"""
        Hier ist der Vertragstext. Erkläre ihn nach den oben genannten Regeln:

        --- START VERTRAG ---
        {contract_text}
        --- ENDE VERTRAG ---
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        temperature=0.3  # eher sachlich, wenig Fantasie
    )

    analysis_text = response.choices[0].message.content
    return analysis_text


# Kleiner manueller Test, falls du die Datei direkt ausführst:
if __name__ == "__main__":
    demo_contract = """
    Dienstleistungsvertrag zwischen Kunde A und Freelancer B.
    B verpflichtet sich, Social-Media-Content (5 Beiträge pro Woche) zu erstellen.
    Der Kunde zahlt 1500 Euro pro Monat.
    Der Vertrag läuft 6 Monate. Kündigung nur mit 30 Tagen Frist zum Monatsende.
    Bei Verzug zahlt B 200 Euro Vertragsstrafe pro verspäteter Woche.
    Alle erstellten Inhalte gehören nach Zahlung vollständig dem Kunden.
    """

    result = analyze_contract(demo_contract)
    print(result)
