import streamlit as st
from PIL import Image , ImageEnhance
import pytesseract
from gtts import gTTS
import regex as re
from textblob import TextBlob
import speech_recognition as sr



# function to perform OCR on an image and extract the text
def ocr(image, lang):
    text = pytesseract.image_to_string(image, timeout=5, lang=lang)
    return text

# function to clean the text by removing non-alphabetic characters
def clean_text(text, lang):
    if lang == 'en':
        clean_text = re.sub('[^a-zA-Z\s]+', '', text)
        text = text.replace('\n', ' ')
    # Remove extra spaces
        text = re.sub(' +', ' ', text)
    
    elif lang== 'hi':
        
        text = text.replace('\n', ' ')
        # Remove non-Hindi characters and digits

        clean_text = re.sub(r"[^\u0900-\u097F\s]+", "", text)
    else:
        clean_text = text
    return clean_text


def enhanceImg(image):
    
    img = Image.open(image)

    # Apply contrast enhancement
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)

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


def speech_to_text():
    # create a recognizer object
    r = sr.Recognizer()

    # use the default microphone as the audio source
    with sr.Microphone() as source:
        # listen for the user's input
        st.write("Listening...")
        audio = r.listen(source)

    try:
        # use the Google Web Speech API to transcribe the audio
        text = r.recognize_google(audio)
        st.write("You said: ", text)
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand your speech")
    except sr.RequestError as e:
        st.write("Sorry, could not request results from Google Speech Recognition service; {0}".format(e))




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
        col1, col2 = st.columns([1.5, 1])
        with col1:
            st.write("Enhanced Image:")

            img = enhanceImg(uploaded_file)
            st.image(img, use_column_width=True, width=800)

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
                mime="audio/mp3",
                )


    if st.button("Start Speech Recognition"):
        speech_to_text()

if __name__ == '__main__':
    app()
