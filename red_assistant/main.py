from .voice_input import listen
from .command_executor import parse_and_execute
from .ai_model import generate_response
from .logger import logger


def main():
    logger.info('Red Assistant started')
    try:
        while True:
            text = listen()
            if not text:
                continue
            logger.info('User said: %s', text)
            if parse_and_execute(text):
                continue
            response = generate_response(text)
            logger.info('Assistant: %s', response)
            print(response)
    except KeyboardInterrupt:
        logger.info('Assistant stopped by user')


if __name__ == '__main__':
    main()
