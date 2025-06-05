from transformers import pipeline
import torch

def initialize_summarizer():
    print("Lade KI Modell...")
    print("Erster Start kann 2-3 Minuten dauern!")
    try:
        summarizer = pipeline("summarization",model="facebook/bart-large-cnn")
        print("KI-Modell erfolgreich geladen!")
        return summarizer
    except Exception as e:
        print(f"Fehler beim Laden:{e}")
        return None

def summarize_article(summarizer, text):
    if len(text) < 100:
        return "Text zu kurz für Zusammenfassung"
    
    try:
        if len(text) > 1000:
            text = text[:1000]

        summary = summarizer(text, max_length=130, min_length=30)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Fehler bei Zusammenfassung: {e}"
    
# Am Ende von summarizer.py hinzufügen:
if __name__ == "__main__":
    # Test der initialize_summarizer Funktion
    summarizer = initialize_summarizer()
    if summarizer:
        print("✓ Summarizer erfolgreich geladen")
        
        # Test mit einem kurzen Text
        test_text = ("Das ist ein Testtext für die Zusammenfassung. Er sollte funktionieren." 
        "Künstliche Intelligenz verändert die Welt in vielen Bereichen, "
        "von der Medizin bis zur Mobilität. Immer mehr Unternehmen setzen "
        "auf automatisierte Systeme, um Prozesse zu optimieren und "
        "Kundenerfahrungen zu verbessern. Die Zukunft sieht spannend aus."
        "Das ist ein Testtext für die Zusammenfassung. Er sollte funktionieren." 
        "Künstliche Intelligenz verändert die Welt in vielen Bereichen, "
        "von der Medizin bis zur Mobilität. Immer mehr Unternehmen setzen "
        "auf automatisierte Systeme, um Prozesse zu optimieren und "
        "Kundenerfahrungen zu verbessern. Die Zukunft sieht spannend aus.")
        print(f"Text-Länge: {len(test_text)} Zeichen")
        result = summarize_article(summarizer, test_text)
        print(f"Test-Zusammenfassung: {result}")
    else:
        print("✗ Fehler beim Laden des Summarizers")    

