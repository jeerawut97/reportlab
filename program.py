from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import Table
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pdfencrypt import StandardEncryption

from header import genHeaderTable
from body import genBodyTable
from footer import genFooterTable

pdfmetrics.registerFont(TTFont('TH', 'TH Sarabun New Regular.ttf'))
senc = StandardEncryption('test', '1234', canPrint=1)\

def genPage(pdf: canvas.Canvas, index:int, n=int, size=A4):
    pdf.setFont('TH', 10)
    width, height = size
    height_list = [
        height * 10 / 100,
        height * 80 / 100,
        height * 10 / 100 
    ]

    main_table = Table([
        [genHeaderTable(width, height_list[0])],
        [genBodyTable(width, height_list[1])],
        [genFooterTable(width, height_list[2], index, n)],
    ],
    colWidths=width,
    rowHeights=height_list
    )

    main_table.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),

        ('LEFTPADDING', (0, 0), (0, 2), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ])

    main_table.wrapOn(pdf, 0, 0)
    main_table.drawOn(pdf, 0, 0)

    # page_index = pdf.getPageNumber()
    # '''
    #     positon: x
    #     - center: (width * 95 / 100) / 2
    #     - right: (width - 40)
    #     - left: (20)
    # '''
    # x = (width * 92 / 100) / 2
    # y = height_list[-1] * 50 / 100
    # pdf.drawString(x, y, f'Page {page_index} of {n}')

    pdf.showPage()

def genPageLandscape(pdf: canvas.Canvas, index:int, n=int, size=landscape(A4)):
    pdf.setFont('TH', 10)
    width, height = size
    height_list = [
        height * 10 / 100,
        height * 80 / 100,
        height * 10 / 100 
    ]

    main_table = Table([
        [genHeaderTable(width, height_list[0])],
        [genBodyTable(width, height_list[1])],
        [genFooterTable(width, height_list[2], index, n)],
    ],
    colWidths=width,
    rowHeights=height_list
    )

    main_table.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),

        ('LEFTPADDING', (0, 0), (0, 2), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ])

    main_table.wrapOn(pdf, 0, 0)
    main_table.drawOn(pdf, 0, 0)

    # page_index = pdf.getPageNumber()
    # '''
    #     positon: x
    #     - center: (width * 95 / 100) / 2
    #     - right: (width - 40)
    #     - left: (20)
    # '''
    # x = (width * 92 / 100) / 2
    # y = height_list[-1] * 50 / 100
    # pdf.drawString(x, y, f'Page {page_index} of {n}')

    pdf.showPage()

size = A4
# pdf = canvas.Canvas('report.pdf', pagesize=landscape(size)) # , encrypt=senc
pdf = canvas.Canvas('report2.pdf', pagesize=landscape(size)) # , encrypt=senc

index = 0
n = 3
for i in range(0,n):
    index += 1
    genPageLandscape(pdf, index, n)

pdf.save()