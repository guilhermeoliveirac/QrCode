import segno

entrada = input('digite a URL: ')
qrcode = segno.make_qr(entrada)
qrcode.save('qrcode.png', scale=10)