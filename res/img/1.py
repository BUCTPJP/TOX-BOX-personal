import cv2
import numpy as np
img = cv2.imdecode(np.fromfile('1.jpg', dtype=np.uint8), cv2.IMREAD_COLOR)
out = cv2.resize(img,(1066,600),cv2.INTER_AREA)
cv2.imwrite('out.jpg',out)