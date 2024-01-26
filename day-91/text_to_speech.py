import PyPDF2
from gtts import gTTS
import os

def pdf_to_text(pdf_path):
    """
    Extract text from a PDF file.

    Parameters:
    - pdf_path: The path to the PDF file.

    Returns:
    - A string containing the extracted text.
    """
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
    return text

def text_to_speech(text, language='en', output_file='output.mp3'):
    """
    Convert text to speech and save it as an audio file.

    Parameters:
    - text: The text to be converted to speech.
    - language: The language of the text (default is English 'en').
    - output_file: The name of the output audio file (default is 'output.mp3').
    """
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    play_audio(output_file)

def play_audio(audio_file):
    """
    Play the audio file using the default audio player.

    Parameters:
    - audio_file: The name of the audio file to be played.
    """
    try:
        os.system(f'start {audio_file}')  # For Windows
    except Exception as e:
        print(f"Error playing audio: {e}")

if __name__ == "__main__":
    pdf_path = 'sample_text.pdf'  # Replace with the path to your PDF file
    pdf_text = pdf_to_text(pdf_path)
    text_to_speech(pdf_text)


