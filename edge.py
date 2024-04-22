#!/usr/bin/env python3

# 必要なライブラリをインポート
import cv2

# 画像の読み込み
image = cv2.imread("images/huukei.png")
# 画像からエッジを検出
edge_image = cv2.Canny(image, 100, 200)

# 検出結果を表示
cv2.imshow("Result", edge_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
