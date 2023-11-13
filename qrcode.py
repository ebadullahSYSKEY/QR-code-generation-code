#generating QR code 
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=9,
)

data = 'you can write here any thing you the qr code of it'
qr.add_data(data)  # Use the 'data' variable as the data for the QR code
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr-code.png")


