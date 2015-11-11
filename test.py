
import qrcode, StringIO
s = StringIO.StringIO()
qr = qrcode.QRCode()
qr.add_data("zertsdgsfds")
qr.make()
qr.print_ascii(out=s, invert=True)

m = s.getvalue()
mm = m.split('\n')
print len(mm)
for i in mm:
    print i
