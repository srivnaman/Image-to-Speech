#library for image processing
import pytesseract
from gtts import gTTS 

from PIL import Image

import pandas as pd
import numpy as np

#Gensim Library for Text Processing
import gensim.parsing.preprocessing as gsp
from gensim import utils

#TextBlob Library (Sentiment Analysis)
from textblob import TextBlob, Word

sample_image_eng = 'positive-quotes1.jpeg'

sample_image_hin = 'Hindi-quotes.jpg'

text = pytesseract.image_to_string(Image.open(sample_image_eng), timeout=5)

text2 = pytesseract.image_to_string(Image.open(sample_image_hin), timeout=5,lang='hin')

# file1 = open("textOutput.txt","w")

# file1.write(text)

# file1.close()

file1 = open("textOutput2.txt","w")

file1.write(text)

file1.write(text2)

file1.close()

i = 1
audio_file_eng = gTTS(text = text2, lang = "en", slow = False)
audio_file_eng.save("audio{}.mp3".format(i))



i = 2
audio_file_hin = gTTS(text = text2, lang = "hi", slow = False)
audio_file_hin.save("audio{}.mp3".format(i))

