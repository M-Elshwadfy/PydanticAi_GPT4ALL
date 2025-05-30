# PydanticAi_GPT4ALL
Integration von Pydantic AI mit GPT4All 

Überblick:  
Dieses Projekt zeigt, wie man Pydantic AI mit dem lokal laufenden Sprachmodell GPT4All kombiniert, um leistungsstarke, strukturierte KI-Antworten zu erzeugen – komplett ohne externe Cloud-APIs.  
Durch die Integration beider Tools wird eine lokale KI-Agenten-Architektur geschaffen, bei der natürliche Sprache verarbeitet, strukturiert analysiert und als typisierte Python-Objekte (mittels Pydantic) zurückgegeben wird. Das ermöglicht nicht nur eine saubere und nachvollziehbare Datenverarbeitung, sondern auch eine effiziente Weiterverarbeitung innerhalb von Python-Anwendungen.

Ziele:  
Verwendung von GPT4All als lokal laufendes LLM  
Einsatz von pydantic_ai.Agent, um GPT-Antworten in validierte Python-Objekte zu überführen  
Lokale Ausführung ohne Internetverbindung oder externe APIs  
Aufbau eines Grundgerüsts für lokal laufende KI-gestützte Tools mit strukturierter Ausgabe

Verwendete Technologien:  
Python 3.10+  
Pydantic AI – Framework zur KI-Modellierung mit Pydantic  
GPT4All Python API – zum Ansprechen lokal gespeicherter LLMs  
Meta Llama 3 oder andere .gguf-Modelle von GPT4All

Voraussetzungen:  
Installiertes GPT4All mit lokalem Modell (z. B. Meta-Llama-3-8B-Instruct.Q4_0.gguf)  

Installation der benötigten Bibliotheken:  
pip install pydantic-ai gpt4all
