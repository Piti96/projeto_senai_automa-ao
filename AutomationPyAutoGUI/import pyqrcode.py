import pyqrcode
import selenium
qr_url = 'https://www.instagram.com/'

qr_code = pyqrcode.create(qr_url)

qr_code.png(outfile='qr_code.png', scale=8)
