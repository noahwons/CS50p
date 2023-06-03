from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Shirt
        self.image("shirtificate.png", 0, 50)
        # Font
        self.set_font("helvetica", "B", 50)
        # Title
        self.cell(0, 25, "CS50 Shirtificate", align='C')

        self.ln(20)

name = input("Name: ")
pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 20)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 150, f"{name} took CS50", align='C')

pdf.output("shirtificate.pdf")