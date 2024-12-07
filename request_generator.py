import os
from groq import Groq
client = Groq(
    api_key="API_KEY" #Replace with your own API_KEY, if you don't have please get one:
    #https://console.groq.com/ 
)
def process_text(input_text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input_text,
            }
        ],
        model="llama3-8b-8192",
    )
    answer= chat_completion.choices[0].message.content
    print(answer)
    return answer
def process_audio():

    #=======================
    # Specify the path to the audio file
    filename = os.path.dirname(__file__) + "\\audios\\audio.wav" # Replace with your audio file!
    # Open the audio file
    with open(filename, "rb") as file:
        # Create a transcription of the audio file
        transcription = client.audio.transcriptions.create(
        file=(filename, file.read()), # Required audio file
        model="whisper-large-v3-turbo", # Required model to use for transcription
        prompt="Specify context or spelling",  # Optional
        response_format="json",  # Optional
        language="en",  # Optional
        temperature=0.0  # Optional
        )
        # Print the transcription text
        print(transcription.text)
        return transcription.text

if __name__ == "__main__":
    output = "Check this text!"
    process_text(output)