import ast

def find_functions_missing_docstrings(tree):
    """Find all functions in the AST that are missing docstrings."""
    functions_missing_docstrings = []
    
    # Walk through the nodes in the AST
    for node in ast.walk(tree):
        # We're interested in function definitions
        if isinstance(node, ast.FunctionDef):
            # Check if the function does not have a docstring (it will be None)
            if not ast.get_docstring(node):
                # Add function name and line number to the list
                functions_missing_docstrings.append((node.name, node.lineno))
    
    return functions_missing_docstrings

def insert_docstring(code, lineno, docstring):
    """Insert the generated docstring at the appropriate place in the code."""
    
    lines = code.splitlines()  # Split the code into lines
    
    # We need to find the function's position in the code based on the line number
    for i, line in enumerate(lines):
        if i == lineno - 1:  # Since line numbers in Python are 1-based
            indent = len(line) - len(line.lstrip())  # Get the indentation level of the function
            docstring_line = f"{' ' * indent}\"\"\"{docstring}\"\"\""
            lines.insert(i + 1, docstring_line)  # Insert the docstring after the function signature
    
    return "\n".join(lines)  # Join the lines back together