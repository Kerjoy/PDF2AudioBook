import PyPDF2
from gtts import gTTS
from io import BytesIO
from tkinter.filedialog import askopenfilename

f = askopenfilename()

lenguage = "en"

with open(f, "rb") as readfile:
    readpdf = PyPDF2.PdfReader(readfile)
    i=0
    textbook = ""
    while i<len(readpdf.pages):
        page = readpdf.pages[i]
        textbook += page.extract_text()
        i+=1

#tts = gTTS(text=text1, lang='en')
print(textbook)
tts = gTTS(text=textbook, lang=lenguage)

tts.save("RAW.mp3")

print("Pdf is already baked :D")
