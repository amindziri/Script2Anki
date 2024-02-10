import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


class LLM:
    def __init__ (self, model_path, prompt):
        self.model_path = model_path
        self.model = AutoModelForCausalLM.from_pretrained(self.model_path, torch_dtype="auto", trust_remote_code=True, temperature= 1e-3)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, trust_remote_code=True)
        self.prompt = prompt

    def create_prompt():
        pass
    
    def predict():
        pass