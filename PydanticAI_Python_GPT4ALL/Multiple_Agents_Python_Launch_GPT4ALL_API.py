# Ich nutze bewusst kleine Prompts, um viel Zeit bei großen Prompts zu sparen.
# Dieser Code dient dazu, den Nachrichtenverlauf (Chat-History) mit mehreren LLMs bzw. Agenten zu testen.

from pydantic_ai import Agent  # Agent-Klasse importieren
from pydantic_ai.models.openai import OpenAIModel  # OpenAIModel importieren
from pydantic_ai.providers.openai import OpenAIProvider  # OpenAIProvider importieren

provider = OpenAIProvider(base_url="http://localhost:4891/v1")  # Lokalen Server als Provider festlegen

llama_model = OpenAIModel(model_name="Llama 3 8B Instruct", provider=provider)  # LLaMA-Modell erstellen
llama_agent = Agent(model=llama_model)  # Agent mit LLaMA-Modell erstellen

result1 = llama_agent.run_sync("Type a random word.")  # Anfrage an LLaMA senden
print("LLaMA says:", result1.output)  # Antwort von LLaMA ausgeben

mistral_model = OpenAIModel(model_name="Mistral OpenOrca", provider=provider)  # Mistral-Modell erstellen
mistral_agent = Agent(model=mistral_model)  # Agent mit Mistral-Modell erstellen

result2 = mistral_agent.run_sync(  # Anfrage an Mistral senden
    "Repeat",
    message_history=result1.new_messages()  # Nachrichtenverlauf von LLaMA mitgeben
)
print("Mistral says:", result2.output)  # Antwort von Mistral ausgeben
