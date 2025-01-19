import yt_dlp
import os
import argparse

class WebTVAudioDownloader:
    def __init__(self, url, output_path):
        self.url = url
        self.output_path = output_path

    def download_webtv_audio(self):
        try:
            # Options de configuration pour l'audio uniquement
            ydl_opts = {
                'format': 'bestaudio/best',  # Meilleure qualité audio disponible
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(self.output_path, '%(title)s.%(ext)s'),
                'quiet': False,
                'no_warnings': False
            }
            
            # Téléchargement de l'audio
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
                
            print(f"Téléchargement audio terminé dans : {self.output_path}")
                
        except Exception as e:
            print(f"Une erreur est survenue : {str(e)}")
            return False
        
        return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Téléchargeur audio WebTV')
    parser.add_argument('url', type=str, help='URL de la vidéo WebTV')
    parser.add_argument('output_path', type=str, help='Chemin de sortie pour l\'audio téléchargé')

    args = parser.parse_args()

    downloader = WebTVAudioDownloader(args.url, args.output_path)
    downloader.download_webtv_audio()