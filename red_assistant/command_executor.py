import os
import webbrowser
from .logger import logger


def parse_and_execute(command: str) -> bool:
    command_lower = command.lower()
    if 'open browser' in command_lower or 'открой браузер' in command_lower:
        logger.info('Opening default web browser')
        webbrowser.open('https://www.google.com')
        return True
    if 'create file' in command_lower or 'создай файл' in command_lower:
        filename = 'new_file.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('')
        logger.info('Created file %s', filename)
        return True
    return False
