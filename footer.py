from reportlab.platypus import Table
from reportlab.lib import colors

def genFooterTable(width, height):
    text = 'ABCDEFGHIJKLMNOP'
    color = colors.HexColor('#003363')
    res = Table([[text, 'another column']], width, height)
    res.setStyle([
        ('GRID', (0, 0), (-1, -1), 1, 'red'),

        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),

        ('BACKGROUND', (0, 0), (-1, -1), color),
        ('TEXTCOLOR', (0, 0), (-1, -1), 'white'),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'), 
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])

    return res