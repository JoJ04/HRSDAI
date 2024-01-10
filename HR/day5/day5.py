import cv2
import numpy as np

# تحميل ملف تعريف الوجه
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# فتح الكاميرا
cap = cv2.VideoCapture(0)

while True:
    # قراءة الصورة من الكاميرا
    ret, frame = cap.read()

    # تحويل الصورة إلى الأبيض والأسود
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # الكشف عن الوجه في الصورة
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # عرض مربع حول الوجه المكتشف
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # عرض الصورة
    cv2.imshow('Camera', frame)

    # انتظار الضغط على مفتاح 'q' لإيقاف البرنامج
    if cv2.waitKey(1) == ord('q'):
        break

# إغلاق الكاميرا وتدمير النوافذ المفتوحة
cap.release()
cv2.destroyAllWindows()
