from fpdf import FPDF

name_user = input("Name: ")

pdf = FPDF(orientation="Portrait", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 30)
pdf.cell(0, 0, txt="CS50 Shirtificate", align="C")

pdf.set_text_color(255, 255, 255)
pdf.cell(0, 100, txt=name_user + " took CS50", align="C")

pdf.image("shirtificate.png", x="C", y=50)

pdf.output("shirtificate.pdf")