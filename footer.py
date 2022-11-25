from reportlab.platypus import Table
from reportlab.lib import colors
import datetime

current_datetime = datetime.datetime.now()

def genFooterTable(width, height, index, n, exported_by='Superadmin swift-dynamics', exported_at=f'{current_datetime}'):
    width_list = [
        width * 20 / 100,
        width * 60 / 100,
        width * 20 / 100,
    ]
    text = f'PAGE {index} of {n}'
    res = Table([
            [f'Exported by : {exported_by}\nExported at : {exported_at}', text , 'Powered by Sitearound']
        ],
        width_list,
        height
    )
    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('FONTNAME', (0,0), (-1, -1), 'TH'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),

        ('LEFTPADDING', (0, 0), (0, 0), (width_list[0] * 50) / 100),

        ('BACKGROUND', (0, 0), (-1, -1), 'white'),
        ('TEXTCOLOR', (0, 0), (-1, -1), 'black'),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'), 
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])

    return res