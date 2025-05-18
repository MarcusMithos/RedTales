import os
import sys
import io
from fpdf import FPDF

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

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
