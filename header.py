from reportlab.platypus import Table, Image
from reportlab.lib import colors

def genHeaderTable(width, height):
    width_list = [
        width * 55 / 100, #left
        width * 45 / 100, #right
        0
    ]

    left_img_path = 'smile.png'
    left_img_width = width_list[0]
    left_img = Image(left_img_path, left_img_width, height)

    right_img_path = 'smile2.png'
    right_img_width = width_list[1]
    right_img = Image(right_img_path, right_img_width, height, kind='proportional')
    right_text = 'SMILE'
    right_list = [right_img, left_img]

    res = Table([
        [left_img, right_img, right_text]
    ],
    width_list,
    height)

    res.setStyle([
        ('GRID', (0, 0), (-1, -1), 1, 'red'),

        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),

        ('ALIGN', (1, 0), (1, 0), 'CENTER'), 
        ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
        
        ('FONTSIZE', (2, 0), (2, 0), 20),
        ('LEFTPADDING', (2, 0), (2, 0), -width_list[1] + 98),
        ('BOMTOMPADDING', (2, 0), (2, 0), 40),


    ])
    return res