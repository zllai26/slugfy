import re
import string

def dash(text):
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return cleaned.lower().strip().replace(" ", "-")

def underscore(text):
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return cleaned.lower().strip().replace(" ", "_")

def dashlimit(text, limit):
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    check = cleaned.lower().strip().replace(" ", "_")
    if len(check) > limit:
        return "Limit overused"
    else:
        return check

def underscorelimit(text, limit):
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    check = cleaned.lower().strip().replace(" ", "_")

    if len(check) > limit:
        return "Limit overused"
    else:
        return check


    