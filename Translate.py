import googletrans
import speech_recognition as sr
import gtts
import playsound
import os  # Import os to handle file removal

def recognize_and_translate(input_lang: str, output_lang: str):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak now:")
        voice = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(voice, language=input_lang)
        print(f"Recognized Text: {text}")

        # Check if the user said "quit" or "exit"
        if text.lower() in ["230"]:
            print("Exiting the program...")
            return False
        
        translator = googletrans.Translator()
        translation = translator.translate(text, dest=output_lang).text
        print(f"Translated Text: {translation}")
        
        tts = gtts.gTTS(translation, lang=output_lang)
        filename = "TranslatedVoice.mp3"
        tts.save(filename)
        
        playsound.playsound(filename)
        
        # Remove the file after playing to avoid permission issues
        os.remove(filename)
        
        return True
    except (sr.UnknownValueError, sr.RequestError, Exception) as e:
        print(f"An error occurred: {e}")
        return True

def main():
    input_lang = input("Enter your spoken language code (e.g., 'en' for English, 'bn' for Bengali): ")
    output_lang = input("Enter the target language code (e.g., 'fr' for French, 'es' for Spanish): ")

    # Loop until the user says "quit" or "exit"
    while True:
        if not recognize_and_translate(input_lang, output_lang):
            break

if __name__ == "__main__":
    main()
