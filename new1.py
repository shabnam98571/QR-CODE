import qrcode # type: ignore

qr = qrcode.make("My Cartoon")

qr.save("qr.jpg")