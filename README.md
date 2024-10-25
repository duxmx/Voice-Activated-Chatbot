# Voice-Activated Chatbot with OpenAI's ChatGPT Integration

This is a voice-activated chatbot that uses OpenAI's ChatGPT model to answer spoken questions. The bot utilizes speech recognition to transcribe audio, OpenAI’s API to process the text, and a text-to-speech engine to deliver responses aloud.

## Prerequisites

- **Python 3.6+**
- **OpenAI API Key**: To use the chatbot, you will need an OpenAI API key, which you can get by signing up at [OpenAI's platform](https://platform.openai.com/signup).

## Installation

1. Install the required packages using pip:
    ```bash
    pip install openai
    pip install pyttsx3
    pip install SpeechRecognition
    ```

2. Place your OpenAI API key into the code:
    ```python
    openai.api_key = "INSERT YOUR OpenAi KEY"
    ```

## How It Works

The chatbot works by continuously listening for the trigger word “moss” to start recording your question. After recognizing the keyword, it records your voice, translates the audio into text using Google’s speech recognition, sends the text to OpenAI's ChatGPT, and reads the generated response back to you using text-to-speech.

## Code Breakdown

### Imports
- `openai`: Accesses OpenAI’s API for generating responses using the GPT model.
- `pyttsx3`: Converts text into speech for audio output.
- `speech_recognition`: Transcribes spoken input into text.
  
### Functions

- **`transcribe_audio_to_text(filename)`**:  
  Converts audio to text using Google Speech Recognition.

- **`generate_response(prompt)`**:  
  Sends user input to OpenAI’s ChatGPT and returns a generated response.

- **`speak_text(text)`**:  
  Uses `pyttsx3` to convert text into speech and reads it aloud.

### Main Functionality
The `main()` function listens for the keyword “moss” and, once detected, records the user's question. It transcribes the recorded audio, generates a response using ChatGPT, and then reads the response aloud.

```python
while True:
    print("Say 'moss' to start recording your questions...")
    # Listen for 'moss' trigger word, then record and process the question
    if transcription.lower() == "moss":
        text = transcribe_audio_to_text("input.wav")
        response = generate_response(text)
        speak_text(response)
