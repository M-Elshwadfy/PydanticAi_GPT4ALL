import logfire

from typing import Union, List
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

# Logfire konfigurieren und Pydantic AI instrumentieren (für Beobachtbarkeit)
logfire.configure()  
logfire.instrument_pydantic_ai()
# logfire.instrument_httpx(capture_all=True)  # Optional: HTTP-Aufrufe überwachen

# Typ: entweder Liste von Farben (Strings) oder Liste von Größen (Ints)
ColorsOrSizes = Union[List[str], List[int]]

# GPT4All-Provider über lokalen Server (OpenAI-kompatibel)
provider = OpenAIProvider(base_url="http://localhost:4891/v1")
model = OpenAIModel(model_name="Llama 3 8B Instruct", provider=provider)

# Agent erstellen mit Modell und Ausgabeschema
agent = Agent(
    model=model,
    output_model=ColorsOrSizes,
    system_prompt=(
        # Anweisung an das Modell: Nur ein JSON-Array zurückgeben
        "When given a list of shapes, respond ONLY with a JSON array:\n"
        "- If the shapes include colors, return a list of color strings, e.g. [\"color1\",\"color2\",\"color3\"].\n"
        "- If they include sizes, return a list of integers, e.g. [size1,size2,size3].\n"
        "No extra text or explanation."
    )
)

# 1️⃣ Erster Lauf: Farben extrahieren
res1 = agent.run_sync("red square, blue circle, green triangle")
print(res1.output)  # Erwartet: ['red', 'blue', 'green']
print(res1.usage())  # Zeigt Token-Nutzung

# 2️⃣ Zweiter Lauf: Größen extrahieren
res2 = agent.run_sync("square size 10, circle size 20, triangle size 30")
print(res2.output)  # Erwartet: [10, 20, 30]
print(res2.usage())  # Zeigt Token-Nutzung
