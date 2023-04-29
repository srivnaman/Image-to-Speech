import streamlit as st
from PIL import Image, ImageEnhance
import pytesseract
from gtts import gTTS
import regex as re

'''
tried this code for uploading multiple files at once
'''



# function to perform OCR on an image and extract the text
def ocr(image, lang):
    text = pytesseract.image_to_string(image, timeout=5, lang=lang)
    return text

# function to clean the text by removing non-alphabetic characters
def clean_text(text, lang):
    if lang == 'en':
        clean_text = re.sub('[^a-zA-Z\s]+', '', text)
    elif lang== 'hi':
        # Remove non-Hindi characters and digits
        clean_text = re.sub(r"[^\u0900-\u097F\s]+", "", text)

    else:
        clean_text = text
    return clean_text


def enhance_img(image):
    
    img = Image.open(image)

    # Apply contrast enhancement
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.8)

    # Apply brightness enhancement
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.3)
    return img


# function to generate an audio file from text in a given language
def generate_audio(text, lang, filename):
    audio_file = gTTS(text=text, lang=lang, slow=False)
    audio_file.save(filename)


# Streamlit app
def app():
    st.set_page_config(page_title="Image to Speech App", page_icon=":microphone:", layout="wide")
    st.title("Image to Speech App")
    
    # user to upload image files
    uploaded_files = st.file_uploader("Choose image files", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    # to select a language
    language = st.selectbox("Select a language", ["English", "Hindi", "Marathi"])
    if language == "English":
        lang_code_ocr = "eng"
        lang_code_aud = "en"
    elif language == "Hindi":
        lang_code_ocr = "hin"
        lang_code_aud = "hi"
    elif language == "Marathi":
        lang_code_ocr = "mar"
        lang_code_aud = "mr"

    # If image files have been uploaded, perform OCR and display the text for each image beside it
    if uploaded_files:
        for uploaded_file in uploaded_files:
            st.write("Image:")
            st.image(uploaded_file, use_column_width=True)

            # Enhance image
            img = enhance_img(uploaded_file)

            # Perform OCR and display the text
            text = ocr(img, lang_code_ocr)
            st.write("OCR Output:")
            st.write(text)

            # Clean the text
            clean_text_output = clean_text(text, lang_code_aud)
            st.write("Cleaned Text:")
            st.write(clean_text_output)

            # Generate audio file and display it
            audio_filename = "audio.mp3"
            generate_audio(clean_text_output, lang_code_aud, audio_filename)
            st.write("Audio Output:")
            audio_file = open(audio_filename, "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")

            st.download_button(
                label="Download Audio",
                data=audio_bytes,
                file_name="audio.mp3",
                mime="audio/mp3")

            st.write("-----")
    
    # Text-to-Speech section
    # audio_filename2 = "audio2.mp3"
