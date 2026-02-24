from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table

from header import gen_header_table
from body import gen_body_table
from footer import gen_footer_table

def create_pdf_file():
    pdf = canvas.Canvas(filename='report.pdf', pagesize=A4)
    pdf.setTitle('Palms Hotel')

    width, height = A4
    heigh_list = [
        height * 20 / 100, # header
        height * 77 / 100, # body
        height * 3 / 100   # footer
    ]

    main_table = Table([
            [gen_header_table(width, heigh_list[0])],
            [gen_body_table(width, heigh_list[1])],
            [gen_footer_table(width, heigh_list[2])]
        ],
        colWidths = width,
        rowHeights = heigh_list
    )

    main_table.setStyle([
        ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('LEFTPADDING', (0, 0), (0, 2), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0)
    ])

    main_table.wrapOn(pdf, 0, 0)
    main_table.drawOn(pdf, 0, 0)

    pdf.showPage()
    pdf.save()


create_pdf_file()
