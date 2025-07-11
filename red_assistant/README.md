# Red Assistant

Python prototype of a voice controlled assistant. It uses `SpeechRecognition` for microphone input, executes simple desktop commands and generates answers with a free neural network (the `distilgpt2` model from the `transformers` library). All responses and errors are logged to `logs/assistant.log`.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the assistant:
   ```bash
   python -m red_assistant
   ```

The assistant listens to the microphone. Try phrases like "open browser" or "create file".
