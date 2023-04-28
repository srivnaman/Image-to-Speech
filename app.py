# Import necessary libraries
import streamlit as st
from PIL import Image
import pytesseract
from gtts import gTTS
import regex as re
from textblob import TextBlob

# Define a function to perform OCR on an image and extract the text
def ocr(image, lang):
    text = pytesseract.image_to_string(Image.open(image), timeout=5, lang=lang)
    return text

# Define a function to clean the text by removing non-alphabetic characters
def clean_text(text,lang):
    if lang == 'en':
        clean_text = re.sub('[^a-zA-Z\s]+', '', text)
    else: 
        clean_text =text
    return clean_text

# # Define a function to perform sentiment analysis on the text
# def sentiment_analysis(text):
#     blob = TextBlob(text)
#     sentiment = blob.sentiment.polarity
#     return sentiment

# Define a function to generate an audio file from text in a given language
def generate_audio(text, lang, filename):
    audio_file = gTTS(text=text, lang=lang, slow=False)
    audio_file.save(filename)

# Define the Streamlit app
def app():
    st.title("Image to Speech App")
    
    # Allow the user to upload an image file
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    
    # Allow the user to select a language
    language = st.selectbox("Select a language", ["English", "Hindi"])
    lang_code_ocr = "eng" if language == "English" else "hin"
    lang_code_aud = "en" if language == "English" else "hi"
    
    # If an image has been uploaded, perform OCR and sentiment analysis and generate audio files
    if uploaded_file is not None:
        st.write("Original Image:")
        st.image(uploaded_file, use_column_width=True)
        
        text = ocr(uploaded_file, lang_code_ocr)
        st.write("OCR Output:")
        st.write(text)
        
        clean_text_output = clean_text(text,lang_code_aud)
        st.write("Cleaned Text:")
        st.write(clean_text_output)
        
        # sentiment = sentiment_analysis(clean_text_output)
        # st.write("Sentiment Analysis Output:")
        # st.write(sentiment)
        
        audio_filename = "audio.mp3"
        generate_audio(clean_text_output, lang_code_aud, audio_filename)
        st.write("Audio Output:")
        audio_file = open(audio_filename, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

if __name__ == '__main__':
    app()
