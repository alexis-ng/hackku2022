import speech_recognition as sr


class Recognize:
    def __init__(self, audio_file) -> None:
        self._audio_file = audio_file
        self._r = sr.Recognizer()
        

    def convert_to_text(self):
        with sr.AudioFile(self._audio_file) as source:
            self._r.adjust_for_ambient_noise(source)
            audio = self._r.record(source) 
   
        query = str(self._r.recognize_google(audio,  language='en-US'))
        return query
        
