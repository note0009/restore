import numpy as np
from numpy import uint8
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
plt.gray();
import cv2

im = cv2.imread('sw.jpg')
im = rgb2gray(im)

width,height=200,260
im= cv2.resize(im,(width,height))
rows,cols = im.shape

fx =  np.fft.fft2(im)
fx2 =  np.fft.fftshift(fx) #読み込んだ画像をフーリエ変換
im3 = 20*np.log(np.abs(fx2))

mask = np.zeros((rows,cols))
img_back = np.zeros((rows,cols),dtype=complex)
img_backs = np.zeros((rows,cols),dtype=complex)
mask2 = np.zeros((rows,cols),dtype=complex)
mask3 = np.zeros((rows,cols),dtype=complex)

cv2.namedWindow(winname='mask')
cv2.namedWindow(winname='wave')
cv2.namedWindow(winname='re')
cv2.namedWindow(winname='spe')
cv2.namedWindow(winname='ori')

def draw_circle(event,x,y,flags,param):
    global img_back, img_backs, mask3, mask2, mask
    if flags == cv2.EVENT_LBUTTONDOWN:
        mask[y,x]=1
        mask3[y,x] = fx2[y,x] #クリックした値を代入
        mask2 = np.zeros((rows,cols),dtype=complex) #mask2は波形を出すために初期化
        mask2[y,x] = fx2[y,x]
        img_backs = np.fft.ifftshift(mask2)
        img_back = np.fft.ifftshift(mask3)

cv2.setMouseCallback('mask',draw_circle)
 
while True:
    im3_u = im3.astype(uint8)
    cv2.imshow('spe',im3_u)
    cv2.imshow('mask',mask)
    cv2.imshow('wave',np.fft.ifft2(img_backs).real) #逆フーリエ変換して表示
    cv2.imshow('re',np.fft.ifft2(img_back).real)
    cv2.imshow('ori',im)
    cv2.namedWindow(winname='mask')
    cv2.setMouseCallback('mask',draw_circle)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()