
# Image to Speech App

This is a simple Streamlit app that allows users to upload an image and converts its text into speech. The app utilizes Optical Character Recognition (OCR) to extract the text from the uploaded image and then converts the text to speech using Google's Text-to-Speech API.

## Getting Started

To get started, make sure that you have Python 3.x and pip installed on your system. You can then install the required libraries using the following command:


    pip install streamlit pytesseract pillow gtts regex textblob

Once you have installed the required libraries, run the following command to start the Streamlit app:

    streamlit run app.py

## Usage
- Upload an image file using the file uploader widget.
- Select a language (either English or Hindi) from the dropdown menu.
- Wait for the app to perform OCR on the uploaded image and generate the speech     output.

Listen to the speech output by playing the generated audio file.

## Contributing
Contributions are welcome! If you would like to contribute to the project, please fork the repository and submit a pull request.

