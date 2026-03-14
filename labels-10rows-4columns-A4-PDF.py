from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics

# Output PDF filename
output_pdf = "labels.pdf"

# Page settings
page_width, page_height = A4  # A4 in points

# Grid settings
rows = 10 # 10
cols = 4
num_of_pages = 1
#total_labels = 80 #rows * cols

# Label numbering
start_number = 850  # the number of the first label in batch

# Font settings
font_name = "Helvetica-Bold"   # <-- CHANGED (bold font)
font_size = 18

# Create the PDF canvas
c = canvas.Canvas(output_pdf, pagesize=A4)
c.setFont(font_name, font_size)

# Precompute cell size
cell_width = page_width / cols
cell_height = page_height / rows

# Compute vertical metrics for precise vertical centering
ascent_pt = pdfmetrics.getAscent(font_name) * font_size / 1000.0
descent_pt = pdfmetrics.getDescent(font_name) * font_size / 1000.0
vertical_offset = (ascent_pt + descent_pt) / 2.0

number = start_number

for page in range(num_of_pages):
    for row in range(rows):
        for col in range(cols):
            # Cell center coordinates
            center_x = col * cell_width + cell_width / 2.0
            center_y = page_height - (row * cell_height + cell_height / 2.0)

            # Label text
            label_text = f"PFR_{number:04d}"

            # Baseline Y for vertical centering
            baseline_y = center_y - vertical_offset

            # Draw centered horizontally & vertically
            c.drawCentredString(center_x, baseline_y, label_text)

            number += 1
        #     if number >= start_number + total_labels:
        #         break
        # if number >= start_number + total_labels:
        #     break

# Save PDF
c.save()
print(f"PDF generated: {output_pdf}")