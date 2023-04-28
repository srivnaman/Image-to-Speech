import regex as re
text = "जीवन में सुख"


def clean_text(text):
    clean_text = re.sub('[^a-zA-Z\s]+', '', text)
    return clean_text


txt = clean_text(text)
print(txt)