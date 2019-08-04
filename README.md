# 処理
読み込んだ画像をフーリエ変換し、クリックした点の値をmask2,3に代入し、mask2は初期化する。その後、mask2,3の値を逆フーリエ変換することで、
mask2はsin波、mask3は復元された画像を表示する。
# 使い方
mask内でクリックし、reに画像を復元させる。
# 依存ライブラリとバージョン
numpy 1.16.2,matplotlib 3.0.3,cv2
# 参考にしたサイト
http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html   
↑フーリエ変換,逆フーリエ変換のプログラムを引用  
https://sites.google.com/site/lifeslash7830/home/hua-xiang-chu-li/opencvniyoruhuaxiangchulimausucaozuo  
↑マウス操作についてのプログラムを引用  
