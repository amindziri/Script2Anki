class mistral_7b(LLM):
    def __init__(self, model_path, prompt):
        super().__init__(model_path, prompt)

    def create_prompt(prompt):
        messages = [
            {"role": "user", "content": prompt}]
        return messages

    def predict():
        prompt = self.create_prompt(self.prompt)
        encodeds = self.tokenizer.apply_chat_template(prompt, return_tensors="pt")
        model_inputs = encodeds.to(device)
        self.model.to(device)

        generated_ids = self.model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
        decoded = self.tokenizer.batch_decode(generated_ids)
        return decoded[0]