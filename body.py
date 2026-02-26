from reportlab.platypus import Table
from reportlab.lib import colors

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

    return 'DESCRIPTION'


def _gen_about_table(width, height):

    return 'ABOUT'


