import speech_recognition as sr
from .logger import logger

def listen() -> str:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='ru-RU')
        return text
    except sr.UnknownValueError:
        logger.error('Could not understand audio')
    except sr.RequestError as exc:
        logger.error('Speech recognition error: %s', exc)
    return ''
