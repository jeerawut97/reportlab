from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from header import genHeaderTable
from body import genBodyTable
from footer import genFooterTable

pdf = canvas.Canvas('report.pdf', pagesize=A4)
pdf.setTitle('Palms Hotel')

width, height = A4
height_list = [
    height * 20 / 100,
    height * 77 / 100,
    height * 3  / 100 
]

main_table = Table([
    [genHeaderTable(width, height_list[0])],
    [genBodyTable(width, height_list[1])],
    [genFooterTable(width, height_list[2])],
 ],
 colWidths=width,
 rowHeights=height_list
)

main_table.setStyle([
    ('GRID', (0, 0), (-1, -1), 1, 'red'),

    ('LEFTPADDING', (0, 0), (0, 2), 0),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
])

main_table.wrapOn(pdf, 0, 0)
main_table.drawOn(pdf, 0, 0)

pdf.showPage()
pdf.save()