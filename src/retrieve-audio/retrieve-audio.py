import yt_dlp
import os

def download_webtv_audio(url, output_path):
    try:
        # Options de configuration pour l'audio uniquement
        ydl_opts = {
            'format': 'bestaudio/best',  # Meilleure qualité audio disponible
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': False
        }
        
        # Téléchargement de l'audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        print(f"Téléchargement audio terminé dans : {output_path}")
            
    except Exception as e:
        print(f"Une erreur est survenue : {str(e)}")
        return False
    
    return True

# Utilisation
url = "https://webtv.hautsdefrance.fr/Seance-pleniere-du-1er-fevrier-2024-Matin"
output_path = '/Users/francoislenne/conseil_regional_hdf/audio'
download_webtv_audio(url, output_path)