import sys
import os
import subprocess

def main():
    if len(sys.argv) != 3:
        print("Usage: python compile_latex.py <input_file.tex> <output_file.pdf>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    # Get the directory and the base name without extension for the output
    output_dir = os.path.dirname(output_file)
    if not output_dir:
        output_dir = "."
    
    # jobname is used by pdflatex to determine the output filename
    # it shouldn't contain the .pdf extension
    jobname = os.path.splitext(os.path.basename(output_file))[0]

    print(f"Compiling '{input_file}' to '{output_file}'...")
    
    # Run pdflatex
    try:
        # We use pdflatex to compile the latex file into a PDF
        result = subprocess.run([
            "pdflatex",
            "-interaction=nonstopmode",
            f"-output-directory={output_dir}",
            f"-jobname={jobname}",
            input_file
        ], text=True, capture_output=True)

        pdf_path = os.path.join(output_dir, jobname + ".pdf")
        if not os.path.exists(pdf_path):
            print("Compilation failed with the following output:")
            print(result.stdout)
            sys.exit(1)

        print("Compilation successful!")

        for ext in ['.aux', '.log', '.out']:
            aux_file = os.path.join(output_dir, jobname + ext)
            if os.path.exists(aux_file):
                try:
                    os.remove(aux_file)
                except OSError as err:
                    print(f"Warning: Could not remove {aux_file} ({err})")

        print(f"Your PDF is ready at: {pdf_path}")
    except FileNotFoundError:
        print("Error: 'pdflatex' command not found. Please ensure a LaTeX distribution (like MiKTeX or TeX Live) is installed and added to your system PATH.")
        sys.exit(1)

if __name__ == "__main__":
    main()
