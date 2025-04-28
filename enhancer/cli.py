import argparse
from enhancer.docstring_generator import enhance_file

def main():
    parser = argparse.ArgumentParser(description="AI-Powered Code Docstring Enhancer")
    parser.add_argument("--file", type=str, required=True, help="Path to Python file to enhance")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite the file instead of just previewing")

    args = parser.parse_args()

    enhance_file(args.file, overwrite=args.overwrite)

if __name__ == "__main__":
    main()
