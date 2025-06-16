from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

# Das erwartete Ausgabeformat definieren
# In diesem Fall wird ein JSON-Objekt mit einem Textfeld namens "answer" erwartet
class Answer(BaseModel):
    answer: str

# Einen Provider einrichten, der mit einer lokalen OpenAI-kompatiblen API kommuniziert
# Die URL zeigt auf den lokal laufenden GPT4All-Server
provider = OpenAIProvider(base_url="http://localhost:4891/v1")

# Das Sprachmodell über den Provider definieren
# Hier wird das Modell „Llama 3 8B Instruct“ verwendet, das lokal über GPT4All läuft
model = OpenAIModel(model_name="Llama 3 8B Instruct", provider=provider)

# Einen Agenten erstellen, der das Modell verwendet und das Antwortschema (Answer) erzwingt
# Der system_prompt gibt vor, dass die Antwort möglichst kurz und in einem Wort erfolgen soll
agent = Agent(
    model=model,
    output_model=Answer,
    system_prompt="Sei so kurz wie möglich. Antwort nur mit einem Wort"
)

# Den Agenten synchron mit einer Benutzerfrage ausführen
# Das Modell wird gefragt, was Einsteins wichtigste Entdeckung war
result = agent.run_sync("Was ist Einsteins größte Entdeckung?")

# Die strukturierte Antwort des Modells ausgeben
print("Answer:", result.output)
