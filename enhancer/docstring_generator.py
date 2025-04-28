import ast
from enhancer.parser import find_functions_missing_docstrings
from enhancer.ai_client import LocalDocstringGenerator

def enhance_file(file_path, overwrite=False):
    source_code, missing = find_functions_missing_docstrings(file_path)
    if not missing:
        print("✅ All functions already have good docstrings!")
        return

    generator = LocalDocstringGenerator()

    source_lines = source_code.splitlines()
    updated_lines = source_lines.copy()

    for func_name, lineno in missing:
        print(f"🔍 Generating docstring for '{func_name}' (line {lineno})...")
        
        # Extract function code (roughly assume till next function/class or EOF)
        func_code_lines = []
        for line in source_lines[lineno - 1:]:
            if line.strip().startswith(("def ", "class ")) and len(func_code_lines) > 0:
                break
            func_code_lines.append(line)
        func_code = "\n".join(func_code_lines)

        # Ask AI to generate a docstring
        docstring = generator.generate_docstring(func_code)
        docstring_block = f'    """{docstring}"""'

        # Insert the docstring after function/class declaration
        insert_at = lineno
        updated_lines.insert(insert_at, docstring_block)

    # Final updated code
    updated_code = "\n".join(updated_lines)

    if overwrite:
        with open(file_path, "w") as f:
            f.write(updated_code)
        print(f"✨ File updated: {file_path}")
    else:
        print("\n--- Preview of Updated Code ---\n")
        print(updated_code)
