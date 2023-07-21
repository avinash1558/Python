# pip install qrcode
import qrcode
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=10)
qr.add_data("https://www.amazon.com")
qr.make(fit=True)
img=qr.make_image(fill_color="red",black_color="white")
img.save("avi.png")





# import qrcode as qr
# img=qr.make("aviandjjdabauhfin ")
# img.save("avinash.png")