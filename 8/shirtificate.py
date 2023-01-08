






from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, "Hello World!")
pdf.output("tuto1.pdf")


pdf = FPDF()
pdf.add_page()
pdf.image("docs/fpdf2-logo.png", x=20, y=60)
pdf.output("pdf-with-image.pdf")

class PDF(FPDF):
    def header(self):
        
        self.image("shirtificate.png", 10, 8, 33)
        self.set_font("helvetica", "B", 15)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", border=1, align="C")
        self.ln(20)