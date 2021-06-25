import qrcode
from PIL import Image
import time
import random

# img = qrcode.make('I love my self')

# item and price
bread = 50
merchant = 'XCRYPTO-GOODS'


def IdGen():

    a = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    b = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    c = random.randrange(1000, 9999)

    d = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    return f'{a}{b}{c}{d}'



def Generator():

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(f'{IdGen()} {merchant} {bread}')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    img.save("sample.png")


Generator()