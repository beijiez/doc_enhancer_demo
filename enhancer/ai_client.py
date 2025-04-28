from transformers import pipeline

class DocstringGeneratorClient:
    def __init__(self, model="gpt2"):  # Or a GPT-Neo model
        self.pipe = pipeline("text-generation", model=model)

    def generate_docstring(self, function_code):
        prompt = (
            "### Task: Generate a Python docstring for the following function.\n\n"
            f"{function_code}\n\n"
            "### Docstring:\n\"\"\""
        )
        result = self.pipe(prompt)[0]["generated_text"]

        # Extract the part inside triple quotes
        if '"""' in result:
            parts = result.split('"""')
            if len(parts) >= 2:
                return parts[1].strip()
        return result.strip()
