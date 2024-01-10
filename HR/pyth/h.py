# استيراد مكتبة OpenCV وتسميتها بـ cv
import cv2 as cv
from matplotlib import pyplot as plt

# قراءة الصورة من الملف 'messi.jpg' وتخزينها في متغير img
img = cv.imread('img.png')

# عرض الصورة باستخدام مكتبة matplotlib
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title('window')
plt.axis('off')  # إيقاف عرض المحاور
plt.show()

 