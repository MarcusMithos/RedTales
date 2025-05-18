import os
import sys

if getattr(sys, 'frozen', False):
    # Running as EXE
    base_path = sys._MEIPASS
else:
    # Running as script
    base_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(base_path)
from fpdf import FPDF

def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=16)
    pdf.cell(0, 10, "Hello from RedTales!", ln=True)
    pdf.output("hello.pdf")
    print("PDF created: hello.pdf")

if __name__ == "__main__":
    main()
