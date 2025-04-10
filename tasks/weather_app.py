import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pywhatkit as kit

# Initialize the speech engine
engine = pyttsx3.init()

# Function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice command
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"Command received: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was an issue with the speech service.")
            return None

# Function to respond to the user's command
def respond(command):
    if 'hello' in command:
        speak("Hello! How can I assist you today?")
    
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    
    elif 'search' in command:
        search_query = command.replace("search", "").strip()
        speak(f"Searching for {search_query} on the web.")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
    
    elif 'play' in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song}")
        kit.playonyt(song)
    
    elif 'goodbye' in command or 'exit' in command:
        speak("Goodbye! Have a nice day.")
        exit()

# Main loop to continuously listen for commands
def run_voice_assistant():
    speak("Hello, I'm your voice assistant. How can I help you?")
    
    while True:
        command = listen()
        if command:
            respond(command)

if __name__ == "__main__":
    run_voice_assistant()
