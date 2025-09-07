import pyttsx3
from deep_translator import GoogleTranslator
from nltk.corpus import wordnet
from gtts import gTTS
import os

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_foreign(text, lang="es"):
    tts = gTTS(text=text, lang=lang)
    filename = "temp.mp3"
    tts.save(filename)
    os.system(f"afplay {filename}")  # Mac command for playing audio

def dictionary_lookup(word):
    meanings = []
    synonyms = set()
    antonyms = set()

    for syn in wordnet.synsets(word):
        meanings.append(syn.definition())
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())

    return meanings, list(synonyms), list(antonyms)

''' def translate_word(word, lang="fr"):
    result = GoogleTranslator(source='auto', target=lang).translate(word)
    return result

if __name__ == "__main__":
    word = input("Enter a word: ").strip()
    if word:
        meanings, synonyms, antonyms = dictionary_lookup(word)

        if meanings:
            print("Meaning:", meanings[:2])
            speak(f"The meaning of {word} is {meanings[0]}")
        else:
            print(f"No meaning found for '{word}'")

        if synonyms:
            print("Synonyms:", synonyms[:5])
        else:
            print(f"No synonyms found for '{word}'")

        if antonyms:
            print("Antonyms:", antonyms[:5])
        else:
            print(f"No antonyms found for '{word}'")

        translated = translate_word(word, "es")  # Spanish
        print("Spanish Translation:", translated)
        speak(f"In Spanish, {word} is {translated}")
        speak_foreign(translated, "es")  # <-- Speaks in Spanish '''
