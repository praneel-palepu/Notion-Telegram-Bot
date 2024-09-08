import os
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(base_url="https://api.groq.com/openai/v1",
    api_key=OPENAI_API_KEY)

def transcribe_audio(audio_file_path: str) -> str:
    """
    Transcribe the audio file using OpenAI's Whisper API.
    
    :param audio_file_path: Path to the audio file
    :return: Transcribed text
    """
    try:
        with open(audio_file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-large-v3", 
                file=audio_file
            )
        return transcript.text
    except Exception as e:
        raise Exception(f"Error transcribing audio: {str(e)}")
    finally:
        # Clean up the temporary audio file
        os.remove(audio_file_path)
