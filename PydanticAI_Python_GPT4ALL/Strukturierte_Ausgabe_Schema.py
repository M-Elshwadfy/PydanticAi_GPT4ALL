# Standardbibliothek zum Parsen von JSON importieren
import json

# Importieren von Pydantic für Datentyp-Validierung und Fehlerbehandlung
from pydantic import BaseModel, ValidationError

# Importieren der PydanticAI-Komponenten für lokale LLM-Integration
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

# 1. Definition des erwarteten strukturierten Formats der Antwort
# Das Modell muss ein JSON mit zwei Feldern liefern: city (Stadt) und country (Land)
class CityInfo(BaseModel):
    stadt: str
    land: str

# 2. Verbindung zum lokalen GPT4All API-Server (OpenAI-kompatibel)
# Wichtig: Der Server muss vorher gestartet und das Modell geladen sein
provider = OpenAIProvider(base_url="http://localhost:4891/v1")
model = OpenAIModel("Llama 3 8B Instruct", provider=provider)

# Agenten erstellen, um mit dem Modell zu interagieren (noch ohne Validierung)
agent = Agent(model=model)

# 3. Prompt formulieren: Das Modell soll im exakten JSON-Format antworten
prompt = (
    "Wie heißt die Hauptstadt von Deutschland? Antwort nur mit diesem genauen Format:\n"
    '{ "stadt": "Stadt", "land": "Land" }'
)

# 4. Anfrage synchron senden und die rohe Text-Antwort erhalten
# Hinweis: Kein output_model angegeben, da die Validierung manuell erfolgt
result = agent.run_sync(prompt)
raw = result.output.strip()  # Whitespace entfernen

# 5. Versuch, die Antwort als JSON zu interpretieren und zu validieren
try:
    parsed = json.loads(raw)  # JSON-String in Python-Daten umwandeln
    validated = CityInfo(**parsed)  # Mit dem Pydantic-Modell validieren

    # Wenn erfolgreich, strukturierte Ausgabe anzeigen
    print("Structured Output:")
    print("Stadt:", validated.stadt)
    print("Land:", validated.land)

# 6. Fehlerbehandlung: Entweder JSON-Fehler oder Schema-Verletzung
except (json.JSONDecodeError, ValidationError) as e:
    print("Failed to parse structured JSON:")
    print(e)
    print("Raw output:", raw)  # Zur Fehlersuche wird der Originaltext ausgegeben
