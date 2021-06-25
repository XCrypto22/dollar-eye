import cv2 as cv
import database as db

info = {}



im = cv.imread('sample.png')
# cv.imshow('code', im)
det = cv.QRCodeDetector()

retval, points, straight_qrcode = det.detectAndDecode(im)

data = retval.split()


id, merchant, amount = data

print(f"Code ID: {id} \
    Merchant: {merchant} \
    Amount: ${amount}")

db.credit(amount)

print(f"Your remaining account Balance is ${db.check_balance()[0][0]}")