import os
from telegram import Voice
import aiohttp
import aiofiles

async def handle_audio_message(voice: Voice) -> str:
    """
    Download and save the audio file from a Telegram voice message.
    
    :param voice: Voice object from the Telegram message
    :return: Path to the saved audio file
    """
    file_id = voice.file_id
    file = await voice.get_file()
    file_path = file.file_path
    
    # Create a temporary directory for audio files if it doesn't exist
    os.makedirs("temp_audio", exist_ok=True)
    
    local_filename = os.path.join("temp_audio", f"{file_id}.ogg")
    
    async with aiohttp.ClientSession() as session:
        async with session.get(file_path) as resp:
            if resp.status == 200:
                async with aiofiles.open(local_filename, mode='wb') as f:
                    await f.write(await resp.read())
    
    return local_filename
