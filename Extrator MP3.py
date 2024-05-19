# pip install moviepy
from moviepy.editor import VideoFileClip

arquivo = input('Selecione o arquivo de video: ').replace('"', '')

clip = VideoFileClip(arquivo)
clip.audio.write_audiofile(arquivo[:-4] + ".mp3")
clip.close()

input('\nAudio extraido com sucesso!\nAperte ENTER para sair...')