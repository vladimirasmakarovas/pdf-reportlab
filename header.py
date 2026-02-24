from reportlab.platypus import Table, Image

def gen_header_table(width, height):

    width_list = [
        width * 55 / 100,
        width * 45 / 100,
        0
    ]

    left_img_path = 'resources\\paradiseHotel.jpg'
    left_img_width = width_list[0]
    left_img = Image(left_img_path, left_img_width, height)

    right_img_path = 'resources\\logoParadise.png'
    right_img_width = width_list[1]
    right_img = Image(right_img_path, right_img_width, height, kind='proportional')

    right_text = 'HOTEL'

    res = Table([
        [left_img, right_img, right_text],
    ],
    width_list,
    height
    )

    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'),
        ('GRID', (0, 0), (-1, -1), 0, 'white'),

        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),

        # ('ALIGN', (1, 0), (1, 0), 'CENTER'),
        ('ALIGN', (1, 0), (2, 0), 'CENTER'),
        ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),

        ('FONTSIZE', (2, 0), (2, 0), 20),
        # ('LEFTPADDING', (2, 0), (2, 0), -width_list[1] + 98)
        ('LEFTPADDING', (2, 0), (2, 0), -width_list[1]),
        ('BOTTOMPADDING', (2, 0), (2, 0), 40)

    ])

    return res
