from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image('shirtificate.png', 10, 60, 190, 200)
        self.set_font("Helvetica", "", 45)
        self.cell(0, 55, 'CS50 Shirtificate', align='C')
        self.ln(40)


def main():
    person = input("Name: ").strip()
    name_in_s(person)


def name_in_s(name):
    pdf = PDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_font("Helvetica", "B", size = 23)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 155, f"{name} took CS50", align ="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
