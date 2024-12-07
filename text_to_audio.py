from gtts import gTTS
import os

# Function to convert text to speech
def text_to_audio(text, lang='en', filename='audio.mp3'):
    # Get the path to the audios directory
    base_dir = os.path.dirname(__file__)  # Get the current script's directory
    audio_dir = os.path.join(base_dir, "audios")

    # Ensure the audios directory exists
    os.makedirs(audio_dir, exist_ok=True)

    # Full path to the audio file
    audio_path = os.path.join(audio_dir, filename)
    
    # Create an audio object from the text
    tts = gTTS(text=text, lang=lang)
    
    # Save the audio file
    tts.save(audio_path)
    print(f"Audio saved to {audio_path}")
    
    # Play the audio file (optional, works if you have a media player installed)
    os.system(f'start "{audio_path}"')  # For Windows, use 'start'. For macOS, use 'afplay', for Linux, use 'mpg321' or 'aplay'.

# Example text
if __name__ == "__main__":
    text = "Hello, this is a test of text-to-speech conversion."
    text_to_audio(text)
