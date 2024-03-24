import PyPDF2, pyttsx3

# Initialize PDF reader and text-to-speech engine
pdfreader = PyPDF2.PdfReader(open('ride_lifetime.pdf','rb'))
speaker = pyttsx3.init()

# Set speech rate and voice
rate = 145
speaker.setProperty("rate", rate)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)

# List to store text from pages
pages_text = []

# Loop through pages to extract text
for page in range(len(pdfreader.pages)):
    text = pdfreader.pages[page].extract_text()
    clean_text = text.strip().replace('\n','')
    pages_text.append(clean_text)

# Join all pages' text into a single string
full_text = '\n'.join(pages_text)

# Save the full text to an audio file
speaker.save_to_file(full_text,'story.mp3')
speaker.runAndWait()

# Stop the engine
speaker.stop()