import whisper
import argparse
from whisper.utils import get_writer
import torch
import warnings


# Ignorer les avertissements
warnings.filterwarnings("ignore")


# Charger le modèle Whisper (peut être 'base', 'small', 'medium', 'large')
model = whisper.load_model('base')

print('Modèle chargé avec succès !')

class TranscribeResponse:
    def __init__(self, audio_path: str, text: str):
        self.audio_path = audio_path
        self.text = text

    def get_transcribe(audio: str, language: str = 'fr'):
        print(f'Transcription de {audio} en cours...')
        return model.transcribe(audio=audio, language=language, verbose=True)

    def save_file(results, format: str = 'txt'):
        writer = get_writer(format, './texte/')
        writer(results, f'transcribe.{format}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transcrire un fichier audio en texte.')
    parser.add_argument('audio_path', type=str, help='Chemin du fichier audio à transcrire')
    parser.add_argument('--language', type=str, default='fr', help='Langue de la transcription (par défaut: fr)')
    parser.add_argument('--format', type=str, default='txt', help='Format de sortie du fichier (par défaut: txt)')

    args = parser.parse_args()

    torch.set_default_dtype(torch.float32)

    result = TranscribeResponse.get_transcribe(audio=args.audio_path, language=args.language)
    print('-'*50)
    print(result.get('text', ''))
    TranscribeResponse.save_file(result, format=args.format)