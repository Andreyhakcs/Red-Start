import os
from datetime import datetime
from pathlib import Path

import speech_recognition as sr
import pyttsx3

LOG_PATH = Path("red_assistant/logs/log.txt")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)


def log_command(command: str) -> None:
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat()} - {command}\n")


def speak(text: str) -> None:
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def main() -> None:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите команду...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="ru-RU").lower()
        print(f"Вы сказали: {command}")
        log_command(command)
    except Exception as e:
        print("Не удалось распознать речь.", e)
        return

    if "открой браузер" in command:
        os.system("google-chrome")
    elif "создай файл" in command:
        with open("note.txt", "w", encoding="utf-8") as f:
            f.write(datetime.now().strftime("%Y-%m-%d"))
    elif "скажи привет" in command:
        speak("Привет!")


if __name__ == "__main__":
    main()
