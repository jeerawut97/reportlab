from reportlab.platypus import Table, Image
from reportlab.lib import colors

def genHeaderTable(width, height):
    width_list = [
        width * 60 / 100, #left
        width * 40 / 100, #right
        0
    ]

    # left_img_path = 'smile.png'
    # left_img_width = width_list[0]
    # left_img = Image(left_img_path, left_img_width, height)
    left_text = ''

    right_img_path = 'icon.png'
    right_img_width = width_list[1]
    right_img = Image(right_img_path, right_img_width, height, kind='proportional')
    # right_text = 'SMILE'
    # right_list = [right_img, left_img]

    # res = Table([
    #     [left_img, right_img, right_text]
    # ],
    res = Table([
        [left_text, right_img]
    ],
    width_list,
    height)
    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('FONTNAME', (0,0), (-1, -1), 'TH'),
        ('FONTSIZE', (0, 0), (-1, -1), 30),
        ('LEFTPADDING', (0, 0), (-1, -1), 50),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 30),
        # ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        # ('BOTTOMPADDING', (0, 0), (-1, -1), width_list[0] + 1),

        ('ALIGN', (1, 0), (1, 0), 'CENTER'), 
        ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
        ('TOPPADDING', (1, 0), (1,0), 50),
        ('BOTTOMPADDING', (1, 0), (1,0), 50),
        ('RIGHTPADDING', (1, 0), (1, 0), 50),

        # ('FONTSIZE', (2, 0), (2, 0), 30),
        # ('LEFTPADDING', (2, 0), (2, 0), 10),
        # ('RIGHTPADDING', (2, 0), (2, 0), 100),
        # ('BOTTOMPADDING', (2, 0), (2, 0), 40),


    ])
    return res