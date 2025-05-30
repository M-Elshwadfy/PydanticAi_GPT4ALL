# Importiere die GPT4All-Bibliothek
from gpt4all import GPT4All

# Lade das Modell "Meta-Llama-3-8B-Instruct" im komprimierten Format (Q4_0)
# HINWEIS: Das Modell muss vorher heruntergeladen und im gleichen Verzeichnis wie dieses Skript gespeichert werden,
# oder es muss der vollständige Pfad zur Datei angegeben werden – sonst kann der Code nicht ausgeführt werden.
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

# Starte eine neue Chat-Sitzung mit dem Modell
with model.chat_session():
    # Die generate()-Funktion erzeugt eine Antwort basierend auf dem gegebenen Prompt ("Hello World")
    # Der Parameter max_tokens gibt an, wie viele Tokens (Wörter + Sonderzeichen) maximal generiert werden dürfen
    # Eine höhere Token-Anzahl erlaubt längere Antworten, kann aber zu längerer Rechenzeit führen
    print(model.generate("Hello World", max_tokens=1024))
