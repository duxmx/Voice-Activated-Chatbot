import openai  # ai library
import pyttsx3  # converts text to speech
import speech_recognition as sr  # translates audio into text
import time

# OpenAI API Key
openai.api_key = "INSERT YOUR OpenAi KEY"

# Initialize text-to-speech engine
engine = pyttsx3.init()

# List available voices
voices = engine.getProperty('voices')
print("Available voices:")
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} ({voice.id})")

# Set the desired voice by index (e.g., voice[1] often corresponds to a female voice)
# Change the index below to the one you prefer based on the printed list
engine.setProperty('voice', voices[1].id)  # You can change the index to set a different voice

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            print('Skipping unknown error')

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],  # Using messages instead of prompt
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["message"]["content"]  # Correct key to access the response

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        # Wait for user to say 'moss'
        print("Say 'moss' to start recording your questions...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "moss":
                    # Record Audio
                    filename = "input.wav"
                    print("Say your question...")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    # Transcribe text
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print(f"You said: {text}")

                        # Generate GPT Responses
                        response = generate_response(text)
                        print(f"GPT-4 says: {response}")

                        # Read response using text-to-speech
                        speak_text(response)
            except Exception as e:
                print("An error occurred: {}".format(e))

if __name__ == "__main__":
    main()
