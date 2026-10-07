import os

def get_reading_time(filename):

    if filename[-4:] != ".txt":
        text = filename
        text_length = len(text.split())

        if text_length == 1:
             return "There is only 1 word here so it won't take long to read at all. If you meant to upload a file, ensure that it is a .txt file."
        reading_time = round(text_length/200)

    else:
        with open(filename, "r") as contents:
                text = contents.read()
                reading_time = round(len(text.split())/200)

    if not text.strip():
        return "There is no text here to read."

    elif reading_time == 1:
        return f"This text will take around {reading_time} minute to read."
    elif reading_time == 0:
        return "This text will take less than a minute to read."
    
    return f"This text will take around {reading_time} minutes to read."