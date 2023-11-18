from sysconfig import get_paths
import PyPDF2
import pyttsx3
import pydub
import os
import ffmpeg

selector_voice = 1 #1 ing #2 esp
direc_pdf = "E:\\Audiolibros\\PDF\\"
direc_finish = 'E:\\Audiolibros\\Audiolibros\\'
direc_raw_to_compress = 'E:\\Audiolibros\\'

def get_paths_files(carpeta):

    # Get the list of file names in the folder.
    archivos = os.listdir(carpeta)

    # Combine the folder with each filename to obtain the full path.
    paths_archivos = [os.path.join(carpeta, archivo) for archivo in archivos]

    return paths_archivos

def voice_maker(f):

    file_name = os.path.basename(f)
    file_name = file_name.replace(".pdf","")

    print ("Audiobook creation in progress: ", file_name)

    with open(f, "rb") as readfile:
        readpdf = PyPDF2.PdfReader(readfile)
        i = 0
        textbook = ""
        while i < len(readpdf.pages):
            page = readpdf.pages[i]
            textbook += page.extract_text()
            i += 1
            print("Percent analyzed: ", round((i / (len(readpdf.pages) / 100)), 2), "%")

    s = pyttsx3.init()
    s.setProperty('rate', 150)
    s.setProperty('volume', 1)

    v = s.getProperty('voices')
    s.setProperty('voice', v[selector_voice].id)

    # s.say(textbook) with this function can play sound in real time
    # print(textbook) print all text

    output_audio_path = direc_raw_to_compress + "Rawpy.mp3"

    s.save_to_file(textbook, output_audio_path)
    s.runAndWait()

    print("Finished Audiobook: ", file_name)
    return file_name

def compressor(file_compress):
    input_file = direc_raw_to_compress + "Rawpy.mp3"
    output_file = direc_finish + file_compress + ".mp3"

    bitrate = '24k' #24-64, 24 k is a minimal rate i think is a minimal quality for audio.

    input_stream = ffmpeg.input(input_file)
    output_stream = ffmpeg.output(input_stream, output_file, **{'b:a': bitrate})
    ffmpeg.run(output_stream)

    print("Audio file compressed successfully: ", file_compress, ".")

paths_archivos = get_paths_files(direc_pdf)



for path_archivo in paths_archivos:
    print(path_archivo)
    file_compress = voice_maker(path_archivo)
    compressor(file_compress)

os.remove(direc_raw_to_compress + "Rawpy.mp3")





