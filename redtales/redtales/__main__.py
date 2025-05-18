import sys

if getattr(sys, 'frozen', False):
    if sys.stdout is None:
        import io
        sys.stdout = io.TextIOWrapper(io.BytesIO(), encoding='utf-8')

import os
from fpdf import FPDF

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(base_path)

def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=16)
    pdf.cell(0, 10, "Hello from RedTales!", ln=True)
    pdf.output("hello.pdf")
    print("PDF created: hello.pdf")

if __name__ == "__main__":
    main()
