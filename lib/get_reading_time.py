import os

def get_reading_time(filename):

    if filename[-4:] != ".txt":
        text = filename
        reading_time = round(len(text.split())/200)

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