
# 🎤 Voice-Based Dictionary & Translator

A Python project that allows you to find meanings, synonyms, antonyms of words and translate them into other languages with voice output.

---

## 🚀 Features
- Get **meanings, synonyms, and antonyms** using WordNet (nltk)
- **Translate words** into multiple languages using `deep-translator`
- **Voice output** for English and the translated word using `pyttsx3` and `gTTS`
- Works for typed words (backup) and voice input (if microphone is available)

---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Voice_Gen_Lang_Tran.git
cd Voice_Gen_Lang_Tran
````

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Download NLTK data (one-time setup):

```python
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
```

---

## ▶️ How to Run

```bash
python app.py
```

* Enter a word when prompted
* The program will:

  * Print meaning, synonyms, antonyms
  * Translate into a target language (default Spanish)
  * Speak the meaning and translated word

---

## 🛠️ Technologies Used

* **Python 3.x**
* **NLTK (WordNet)** – dictionary and synonyms/antonyms
* **deep-translator** – translation
* **pyttsx3** – text-to-speech (English)
* **gTTS** – text-to-speech (target language)
* **playsound** – play audio files

---

```


Do you want me to do that?
```
