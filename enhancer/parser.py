import ast

def find_functions_missing_docstrings(file_path):
    with open(file_path, "r") as file:
        source_code = file.read()

    tree = ast.parse(source_code)
    missing_docstrings = []
    
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            docstring = ast.get_docstring(node)
            if not docstring or len(docstring.strip()) < 10:  # Too short docstring
                missing_docstrings.append((node.name, node.lineno))
    
    return source_code, missing_docstrings
