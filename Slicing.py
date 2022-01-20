import numpy as np
from google.colab.patches import cv2_imshow

import cv2
import glob

path = "科展研究/*.*" # 檔案資料夾路徑
for file in glob.glob(path): # 用 for 迴圈抓取每張照片
  print("==================")
  print(file) 

  img = cv2.imread(file) # 讀圖片

  ## convert to hsv
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 

  #　HSV　

  ## mask of green (36,25,25) ~ (86, 255,255)
  ## mask_green = cv2.inRange(hsv, (28, 25, 25), (86, 255,255))
  ## 將顏色二值化，屬於綠色的設為1，不屬於綠色的設為0
  mask_green = cv2.inRange(hsv, (28, 25, 25), (86, 255,255))

  ## mask of green (10,100,20) ~ (20, 255,200)
  ## mask_brown = cv2.inRange(hsv, (10, 100, 20), (20, 255, 200))
  ## 將顏色二值化，屬於咖啡色的設為1，不屬於咖啡色的設為0
  mask_brown = cv2.inRange(hsv, (10, 100, 20), (20, 255, 200))
  

  #  slice the green
  ## 將不屬於綠色的部分設為 0 就會不顯示了
  imask_green = mask_green > 0 
  green = np.zeros_like(img, np.uint8) 
  green[imask_green] = img[imask_green]

  # slice the brown
  ## 將不屬於咖啡色的部分設為 0 就會不顯示了
  imask_brown = mask_brown > 0
  brown = np.zeros_like(img, np.uint8)
  brown[imask_brown] = img[imask_brown]

  # save 
  print("img")
  cv2_imshow(img)
  print("green")
  cv2_imshow(green)
  print("brown")
  cv2_imshow(brown)

  # 計算有多少個綠色像素
  green_pixel = np.count_nonzero(green)

  # 計算有多少個咖啡色像素
  brown_pixel = np.count_nonzero(brown)

  print("綠色 pixel數 : %f " % green_pixel)
  print("咖啡色 pixel數 : %f " % brown_pixel)

  # 抓取綠色的比例
  ## 綠色像素點 / (咖啡色像素點 + 綠色像素點 )
  print("比例：", green_pixel / (brown_pixel + green_pixel))

  