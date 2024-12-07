from pathlib import Path
from elevenlabs import ElevenLabs

def produce_audio(answer, output_filename='audios/audio.mp3'):
    client = ElevenLabs(
        api_key="sk_262b2e3f093f6b2082864e2475688a98ca95eb40b7262e98",  # Replace with your actual API key
    )

    audio_generator = client.generate(
        text=answer,
        voice="Brian",
        model="eleven_multilingual_v2"
    )

    # Ensure the directory exists
    output_path = Path(output_filename)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the audio to an MP3 file
    with open(output_path, "wb") as audio_file:
        for chunk in audio_generator:  # Iterate through the generator
            audio_file.write(chunk)

    print(f"Audio saved as {output_path}")

