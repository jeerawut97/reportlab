from reportlab.platypus import Table
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

import csv

def genBodyTable(width, height, facility:str='FACILITY'):
    width_list = [
        width * 10 / 100,
        width * 80 / 100, 
        width * 10 / 100,
    ]

    height_list = [
        height * 5 / 100, #Title
        height * 95 / 100  #Detail
    ]

    res = Table([
        ['', facility, ''],
        ['', _genListTable(width_list[1], height_list[1]), ''],
    ],
        width_list,
        height_list
    )

    color = colors.HexColor("#000000")
    title_font_size = 20
    title_left_padding = 20
    title_bottom_padding = 20
    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), title_bottom_padding),

        ('FONTSIZE', (1,0), (1,0), title_font_size),

        ('LINEBELOW', (1,0), (1,0), 1, color),

        ('LEFTPADDING', (1,0), (1,0), title_left_padding),
        # ('BOTTOMPADDING', (1,0), (1,0), title_bottom_padding)
        # ('TEXTCOLOR', (0, 0), (-1, 0), '#6eda78')
    ])

    return res

def _genListTable(width, height):
    style = ParagraphStyle('Title Table')
    style.fontSize = 18
    style.fontName = 'TH'
    style.spaceAfter = 15

    title_paragraph = Paragraph('Work Request List', style)
    height = height * 70 / 100
    detail_table = _genDetailTable(width, height)

    elements_list = [title_paragraph, detail_table]

    res = Table(
        [
            [elements_list]
        ],
        width,
        height
    )
    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'), 
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 50),
        ('BOTTOMPADDING', (0, 0), (-1, -1), height / 2)
        
    ])
    return res

def _genDetailTable(width, height):
    '''
    Ex.value
        [[header], [detail] ... [detail]]
    '''
    style = ParagraphStyle('Detail Table')
    style.fontSize = 10
    style.fontName = 'TH'
    style.wordWrap = 12
    # text_wrap = Paragraph('User001, User002, User003, User003, User003, User003', style)

    martrix = [
        ['Priority', 'Document Code', 'Subject', 'Requestor', 'Process Status', 'Task Decision', 'Location', 'Ball In Court', 'Due Date'],
        ['Low Priority1', 'F001', Paragraph('test work order 20 by natcha', style), 'Requestor001', 'Status001', 'Task001', 'Location001', Paragraph('User001User002User003User003User003User003asdaczxcsacsacsacsacsacsacs', style), '11/26/2022'],
        ['Low Priority2', 'F002', 'Subject002', 'Requestor002', 'Status002', 'Task002', 'Location002', 'User002', '11/27/2022'],
        ['Low Priority3', 'F003', 'Subject003', 'Requestor003', 'Status003', 'Task003', 'Location003', 'User003', '11/28/2022'],
        ['Low Priority4', 'F004', 'Subject004', 'Requestor004', 'Status004', 'Task004', 'Location004', 'User004', '11/29/2022'],
        ['Low Priority5', 'F005', 'Subject005', 'Requestor005', 'Status005', 'Task005', 'Location005', 'User005', '11/30/2022'],
        ['Low Priority6', 'F006', 'Subject006', 'Requestor006', 'Status006', 'Task006', 'Location006', 'User006', '12/1/2022'],
        ['Low Priority7', 'F007', 'Subject007', 'Requestor007', 'Status007', 'Task007', 'Location007', 'User007', '12/2/2022'],
        ['Low Priority8', 'F008', 'Subject008', 'Requestor008', 'Status008', 'Task008', 'Location008', 'User008', '12/3/2022'],
        ['Low Priority9', 'F009', 'Subject009', 'Requestor009', 'Status009', 'Task009', 'Location009', 'User009', '12/4/2022'],
        ['Low Priority10', 'F010', 'Subject010', 'Requestor010', 'Status010', 'Task010', 'Location010', 'User010', '12/5/2022']
        ]
    # with open(r'list_table.csv', 'r') as file:
    #     martrix = list(csv.reader(file))
    if len(martrix) < 2 or len(martrix[0]) != 9:
        return Table([['no data']])
    # print(martrix)
    width_list = [
        width * 12 / 100,
        width * 12 / 100,
        width * 12 / 100,
        width * 12 / 100,
        width * 10 / 100,
        width * 10 / 100,
        width * 10 / 100,
        width * 12 / 100,
        width * 10 / 100,
    ]
    row_count = len(martrix)
    res = Table(martrix, width_list, (height / row_count) + 10)

    color = colors.toColor('#6eda78')

    res.setStyle(
        [
            ('GRID', (0, 0), (-1, -1), 0.5, 'black'),
            ('FONTSIZE', (0,0), (-1, -1), 10),
            ('FONTNAME', (0,0), (-1, -1), 'TH'),
            # ('INNERGRID', (0, 0), (-1, -1), 0.5, 'grey'),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

            ('BACKGROUND', (0, 0), (-1, 0), color),
            ('TEXTCOLOR', (0, 0), (-1, 0), 'black'),

            # ('ALIGN', (1,0), (-1,0), 'CENTER'),
            # ('ALIGN', (1,0), (-1,0), 'CENTER'),
            # ('ALIGN', (1,0), (-1,0), 'CENTER'),
            # ('ALIGN', (1,0), (-1,0), 'CENTER'),
            # ('ALIGN', (1,0), (-1,0), 'CENTER'),
            # ('ALIGN', (1,0), (-1,0), 'CENTER'),
            # ('ALIGN', (1,0), (-1,0), 'CENTER')

            # ('ROWBACKGROUNDS', (0, 1), (-1, -1), [
            #     'antiquewhite', 'beige'
            # ])
        ]
    )

    return res