#!/usr/bin/env python3

# 必要なライブラリをインポート
import cv2

# 画像を読み込み
image = cv2.imread("images/huukei.png")

# バウンディングボックスを描画
# cv2.rectangle(元画像, ボックスの左上の位置, ボックスの右下の位置, 色情報, 線の太さ)
# 位置(x, y)は画像左上の原点(0, 0)から指定する
edited_image = cv2.rectangle(image, (100, 150), (200, 300), (0, 0, 255), 2)

# 画像を表示
cv2.imshow("edited_image", edited_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
