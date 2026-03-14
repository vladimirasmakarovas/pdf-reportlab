from reportlab.platypus import Paragraph, Image, Table
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle

def gen_body_table(width, height):

    width_list = [
        width * 10 / 100, # left 'padding'
        width * 80 / 100, # values
        width * 10 / 100  # right 'padding'
    ]

    height_list = [
        height * 10 / 100, # offer - idx 0
        height * 15 / 100, # contacts - idx 1
        height * 35 / 100, # price list - idx 2
        height * 30 / 100, # description - idx 3
        height * 10 / 100  # about - idx 4
    ]

    res = Table([
        ['', 'Offer', ''],
        ['', _gen_contacts_table(width_list[1], height_list[1]), ''],
        ['', _gen_price_list_table(width_list[1], height_list[2]), ''],
        ['', _gen_description_paragraphs(), ''],
        ['', _gen_about_table(width_list[1], height_list[4]), '']
    ],
    width_list,
    height_list)

    color = colors.HexColor('#003363')
    left_padding = 20

    res.setStyle([
        # ('GRID', (0,0), (-1,-1), 1, 'red'),

        ('LINEBELOW', (1,0), (1,1), 1, color),
        ('LINEBELOW', (1,3), (1,3), 1, color),

        ('LEFTPADDING', (1,0), (1,3), left_padding),

        ('FONTSIZE', (1,0), (1,0), 30),
        ('BOTTOMPADDING', (1,0), (1,3), 30),

        ('BOTTOMPADDING', (1,1), (1,2), 0),
        ('BOTTOMPADDING', (1,3), (1,3), 40),

        ('BOTTOMPADDING', (1,4), (1,4), 0),
        ('LEFTPADDING', (1,4), (1,4), 0),
    ])

    return res


def _gen_contacts_table(width, height):

    return 'CONTACTS'


def _gen_price_list_table(width, height):

    return 'PRICES'


def _gen_description_paragraphs():

    para_list = []

    para1_style = ParagraphStyle('para1d')
    para1_style.fontSize = 10
    para1_style.spaceAfter = 15
    para1_style.textColor = colors.HexColor('#003363')
    para1 = Paragraph("""
    <b>
    Thank you very much for using the services from us at Palms. 
    Here at Palms Hotel we have living rooms and well-equipped 
    meeting rooms of all sizes with a capacity from 8 - 300 people,
    so that we will be well prepared for most needs you may have.
    </b>       
    """"", para1_style)

    para2_style = ParagraphStyle('para2d')
    para2_style.fontSize = 10
    para2 = Paragraph("""
    <i>
    Palms Hotel is also known for its cuisine and good service, 
    therefore you can feel confident that your needs and desires 
    will be well taken care of, whether you choose to use our 
    beautiful Restaurant Palms or other living rooms, 
    we guarantee a <u>good experience with us.</u>
    </i>
    """, para2_style)

    para_list.append(para1)
    para_list.append(para2)

    return para_list


def _gen_about_table(width, height):

    width_list = [
        width * 20 / 100, # image
        width * 80 / 100 # paragraphs
    ]

    img = Image('resources\\logoParadise.png',
                width_list[0],
                height,
                kind = 'proportional'
    )

    para1Style = ParagraphStyle('para1')
    para1Style.fontSize = 14
    para1Style.spaceAfter = 15
    para1 = Paragraph('Palms Hotels', para1Style)

    para2Style = ParagraphStyle('para2')
    para2Style.fontSize = 8
    para2 = Paragraph("""
    Ever since 2004, Palms Hotel has received accommodation and
    dining guests. The hotel and restaurants has been run 
    and owned by th Dubai SGPS.    
    """, para2Style)

    para_list = [para1, para2]

    res = Table([
            [img, para_list]
        ],
        width_list,
        height)

    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),

        ('LEFTPADDING', (0, 0), (0, 0), 0),
        ('BOTTOMPADDING', (0, 0), (1, 0), 0),

        ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ('VALIGN', (0, 0), (1, 0), 'MIDDLE'),

        # ('FONTSIZE', (1,0), (1,0), 30),
    ])

    return res


