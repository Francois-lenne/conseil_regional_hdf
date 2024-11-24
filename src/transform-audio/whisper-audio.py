import whisper
from whisper.utils import get_writer

# Load the base model
model = whisper.load_model('base')

def get_transcribe(audio: str, language: str = 'fr'):
    return model.transcribe(audio=audio, language=language, verbose=True)

def save_file(results, format: str = 'txt'):
    writer = get_writer(format, './texte/')
    writer(results, f'transcribe.{format}')

if __name__ == "__main__":
    result = get_transcribe(audio='/Users/francoislenne/conseil_regional_hdf/audio/Séance plénière du 1er février 2024 - Matin – WebTV Hauts-de-France.mp3')
    print('-'*50)
    print(result.get('text', ''))
    save_file(result)