from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
import qrcode


def generate_order_pdf(order):
    # Generate a unique filename for the PDF
    filename = f"order_{order.order_number}.pdf"
    filepath = os.path.join(settings.MEDIA_ROOT, "pdf", filename)
    app_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    relative_filepath = os.path.relpath(filepath, app_root)

    # Create a canvas and set the PDF properties
    c = canvas.Canvas(filepath, pagesize=letter)

    # Add content to the PDF
    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, 10 * inch, f"Order Number: {order.order_number}")
    c.drawString(1 * inch, 9 * inch, f"Recipient Name: {order.recipient_name}")
    c.drawString(1 * inch, 8 * inch, f"Recipient Address: {order.recipient_address}")
    c.drawString(1 * inch, 7 * inch, f"Business: {order.sender.name}")
    c.drawString(1 * inch, 6 * inch, f"Region: {order.recipient_region.name}")

    # Generate the QR code with order details
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(order.order_number)

    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(
        os.path.join(settings.MEDIA_ROOT, "qr_codes", f"order_{order.order_number}.png")
    )

    # Draw the QR code on the PDF
    qr_img_path = os.path.join(
        settings.MEDIA_ROOT, "qr_codes", f"order_{order.order_number}.png"
    )
    c.drawImage(qr_img_path, 1 * inch, 4 * inch, width=2 * inch, height=2 * inch)

    # Save and close the canvas
    c.showPage()
    c.save()

    # Return the file path for further use
    return relative_filepath
