import os
import sys
import io
from fpdf import FPDF

# Force console output encoding to UTF-8 to avoid UnicodeEncodeError on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if getattr(sys, 'frozen', False):
    # Running as a bundled EXE
    base_path = sys._MEIPASS
else:
    # Running as a script
    base_path = os.path.dirname(os.path.abspath(__file__))

# Change working directory to where script or EXE resources are
os.chdir(base_path)

def main():
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", size=16)
        pdf.cell(0, 10, "Hello from RedTales!", ln=True)
        pdf.output("hello.pdf")
        print("PDF created: hello.pdf")
    except Exception as e:
        print("Error:", e)
    finally:
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
