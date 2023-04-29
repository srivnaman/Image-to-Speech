import streamlit as st
from PIL import Image , ImageEnhance
import pytesseract
from gtts import gTTS
import regex as re
from textblob import TextBlob




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


def enhanceImg(image):
    
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

# function to convert text to speech in a given language
def text_to_speech(text, lang):
    speech = gTTS(text=text, lang=lang, slow=False)
    return speech


# Streamlit app
def app():
    st.set_page_config(page_title="Image to Speech App", page_icon=":microphone:", layout="wide")
    st.title("Image to Speech App")
    

    # user to upload an image file
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

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

    # If an image has been uploaded, perform OCR and generate audio files
    if uploaded_file is not None:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.write("Enhanced Image:")

            img = enhanceImg(uploaded_file)
            st.image(img, use_column_width=True)

        with col2:
            # st.write("OCR Output:")
            text = ocr(img, lang_code_ocr)
            # st.write(text)

            st.write("Cleaned Text:")
            clean_text_output = clean_text(text, lang_code_aud)
            st.write(clean_text_output)

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

        # Text-to-Speech section
        audio_filename2 = "audio2.mp3"
        generate_audio(clean_text_output, lang_code_aud, audio_filename)

        st.write(" ")
        st.write("Convert text to speech:")
        text_input = st.text_input("Enter text to convert to speech:")
        if text_input:
            generate_audio(text_input, lang_code_aud, audio_filename2)
            st.write("Audio Output:")
            audio_file2 = open(audio_filename2, "rb")
            audio_bytes2 = audio_file2.read()
            st.audio(audio_bytes2, format="audio/mp3")

if __name__ == '__main__':
    app()
