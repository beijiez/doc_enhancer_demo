import ast
from enhancer import parser
from enhancer.ai_client import DocstringGeneratorClient

def clean_docstring(docstring):
    """Basic clean-up to prevent crashes when writing."""
    if not docstring:
        return "TODO: Add description"

    # Remove triple quotes inside the docstring
    docstring = docstring.replace('"""', "'''")
    # Remove non-ASCII characters
    docstring = docstring.encode('ascii', errors='ignore').decode()
    # Trim whitespace
    docstring = docstring.strip()

    # If after cleaning, the docstring is empty or too short, fallback
    if not docstring or len(docstring.split()) < 3:
        return "TODO: Add description"

    return docstring

def enhance_file(file_path, overwrite=False):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    # Parse the file into an AST
    tree = ast.parse(code)

    # Find functions missing docstrings
    functions = parser.find_functions_missing_docstrings(tree)

    if not functions:
        print("✅ No missing docstrings found!")
        return

    # Initialize the AI client
    ai_client = DocstringGeneratorClient()

    updated_code = code
    for func_name, lineno in functions:
        prompt = f"Write a clear, professional Python docstring for a function named '{func_name}'."
        generated = ai_client.generate_docstring(prompt)  # Generate docstring with the AI client
        cleaned = clean_docstring(generated)
        updated_code = parser.insert_docstring(updated_code, lineno, cleaned)

    # Handle saving or overwriting based on 'overwrite' flag
    if overwrite:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated_code)
        print(f"✅ Overwrote {file_path} with enhanced docstrings!")
    else:
        output_path = file_path.replace(".py", "_enhanced.py")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(updated_code)
        print(f"✅ Saved enhanced version to {output_path} (original untouched)")
