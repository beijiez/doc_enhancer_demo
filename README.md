# Doc Enhancer Demo

This project is an AI-powered tool designed to enhance Python code by generating high-quality docstrings for functions and classes. It uses a pre-trained language model to analyze code and generate meaningful documentation, improving code readability and maintainability.

## Features

- **Docstring Detection**: Identifies functions and classes missing docstrings or with insufficient documentation.
- **AI-Powered Docstring Generation**: Leverages a pre-trained model (`Salesforce/codegen2-1B`) to generate detailed and context-aware docstrings.
- **Preview or Overwrite**: Allows users to preview the enhanced code or overwrite the original file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/doc-enhancer-demo.git
   cd doc-enhancer-demo
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the CLI tool to enhance a Python file:

```bash
python -m enhancer.cli --file <path_to_python_file> [--overwrite]
```

- `--file`: Path to the Python file to enhance.
- `--overwrite`: Optional flag to overwrite the original file with the enhanced version. If not provided, a preview of the updated code will be displayed.

### Example

To enhance the file `examples/before.py` and preview the changes:

```bash
python -m enhancer.cli --file examples/before.py
```

To overwrite the file with the enhanced version:

```bash
python -m enhancer.cli --file examples/before.py --overwrite
```

## Project Structure

```
doc_enhancer_demo/
├── enhancer/
│   ├── __init__.py          # Package initializer
│   ├── ai_client.py         # AI-based docstring generator
│   ├── cli.py               # Command-line interface
│   ├── docstring_generator.py # Main logic for enhancing files
│   ├── parser.py            # Code parser to detect missing docstrings
├── examples/
│   ├── before.py            # Example Python file to enhance
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
```

## How It Works

1. **Parsing the Code**: The `parser.py` module analyzes the Python file to find functions and classes missing docstrings or with insufficient documentation.
2. **Generating Docstrings**: The `ai_client.py` module uses a pre-trained language model to generate docstrings based on the function or class code.
3. **Enhancing the File**: The `docstring_generator.py` module inserts the generated docstrings into the appropriate locations in the code.

## Dependencies

- `torch`
- `transformers`
- `accelerate`

Install them using the provided `requirements.txt`.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.