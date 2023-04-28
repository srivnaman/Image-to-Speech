#library for image processing
import pytesseract

from PIL import Image

import pandas as pd
import numpy as np

#Gensim Library for Text Processing
import gensim.parsing.preprocessing as gsp
from gensim import utils

#TextBlob Library (Sentiment Analysis)
from textblob import TextBlob, Word

sample_images = 'positive-quotes1.jpeg'

text = pytesseract.image_to_string(Image.open(sample_images), timeout=5)


# file1 = open("textOutput.txt","w")

# file1.write(text)

# file1.close()