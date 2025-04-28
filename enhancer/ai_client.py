from transformers import pipeline

class LocalDocstringGenerator:
    def __init__(self, model_name="Salesforce/codegen2-1B"):
        self.device = 0  # 0 = GPU; -1 = CPU
        self.pipe = pipeline(
            "text-generation",
            model=model_name,
            device=self.device,
            torch_dtype="auto",
            max_new_tokens=128,
            do_sample=True,
            temperature=0.5,
        )

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
