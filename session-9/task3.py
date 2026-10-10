import re

def extract_hashtags(text):
    return re.findall(r"#\w+", text)


caption = "Enjoying Navratri #Garba #Gujarat #GamanSanthal"

hashtags = extract_hashtags(caption)

print("Hashtags:", hashtags)