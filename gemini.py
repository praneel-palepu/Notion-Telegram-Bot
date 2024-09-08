import google.generativeai as genai
from config import GOOGLE_AI_API_KEY

# Configure the Gemini API
genai.configure(api_key=GOOGLE_AI_API_KEY)

def process_with_gemini(transcript: str) -> str:
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-8b-exp-0827')
        
        prompt = f"""
        Analyze the following transcript and provide a concise summary, 
        highlighting key points and any action items if present:

        Transcript: {transcript}

        Please format your response in a clear and structured manner.
        """
        
        response = model.generate_content(prompt)
        
        return response.text
    except Exception as e:
        raise Exception(f"Error processing with Gemini: {str(e)}")
