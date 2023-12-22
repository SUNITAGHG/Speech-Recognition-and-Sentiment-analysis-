import speech_recognition as sr
from textblob import TextBlob

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        
        analysis = TextBlob(text)

        
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            sentiment = "positive"
        elif polarity < 0:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        print("Sentiment:", sentiment)

    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    recognize_speech()
