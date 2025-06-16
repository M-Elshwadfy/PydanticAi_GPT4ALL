import requests

# Diese Anfrage testet den lokalen OpenAI-kompatiblen API-Server von GPT4All
#Das ist notwendig für die Kommunikation zwischen PydanticAI und GPT4ALL
# Es wird ein Chat-Request an das Sprachmodell geschickt, das lokal unter http://localhost:4891 läuft

response = requests.post(
    "http://localhost:4891/v1/chat/completions",  # Endpoint für Chat-Modelle
    json={
        "model": "Llama 3 8B Instruct",
        "messages": [
            # Die Unterhaltung mit dem Modell beginnt hier – Rolle 'user' gibt die Eingabe an
            {"role": "user", "content": "Was ist die Hauptstadt von Deutschland? Antworte mit einem Wort."}
        ],
        "max_tokens": 50  # Maximale Anzahl an Token in der Antwort (zur Begrenzung der Ausgabe)
    }
)

# Ausgabe des HTTP-Statuscodes (z.B. 200 bei Erfolg)
print("Status:", response.status_code)

# Ausgabe der vollständigen Antwort im JSON-Format
print("Response:", response.json())
