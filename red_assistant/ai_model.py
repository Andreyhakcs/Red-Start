from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from .logger import logger

MODEL_NAME = 'distilgpt2'

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)


def generate_response(prompt: str, max_length: int = 50) -> str:
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    with torch.no_grad():
        outputs = model.generate(inputs, max_length=max_length, do_sample=True)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text
