import cv2
import serial
import time
from pyzbar.pyzbar import decode
if __name__ == '__main__':
    ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
    ser.reset_input_buffer()
# Khởi tạo camera
cap = cv2.VideoCapture(0)

# Khởi tạo danh sách để lưu trữ nội dung của mã QR
qr_codes = []
dem1=0
dem2=0
dem3=0

# Loop chạy camera và đọc mã QR
while True:
    _, frame = cap.read() 
    # Chuyển ảnh thành grayscale để xử lý QR code
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Decode QR code
    decoded = decode(gray)
    # Hiển thị và lưu nội dung của mã QR
    for obj in decoded:
        # Lấy nội dung của mã QR
        data = obj.data.decode('utf-8')
        # Tách nội dung của mã QR bằng phép toán chuỗi
        content = data[7:]
        # Tách nội dung của mã QR thành từng phần
        if (content not in qr_codes) :
    # Lưu trữ nội dung đã tách 
            qr_codes.append((content))
            with open('qr_codes.txt', 'a') as f:
                f.write(content + '\n')
    # Gửi dữ liệu đã tách được  
        if content == "xanh":
		time.sleep(0.1)
		cap.release()
		time.sleep(2)
		cap = cv2.VideoCapture(0)
                ser.write(b"xanh\n")
                print('Da nhan duoc san pham:' , content)
                print('So san pham xanh la: ', dem1)
        elif content == "do":
		time.sleep(0.1)
		cap.release()
		time.sleep(2)
		cap = cv2.VideoCapture(0)
                ser.write(b"do\n")
                print('Da nhan duoc san pham:' , content)
                print('So san pham do la: ', dem2)
        else:
		time.sleep(0.1)
		cap.release()
		time.sleep(2)
		cap = cv2.VideoCapture(0)
                ser.write(b"vang\n")
                print('Da nhan duoc san pham:' , content)
                print('So san pham vang la: ', dem3)
        # Hiển thị nội dung của mã QR
        cv2.putText(frame, data, (obj.rect.left, obj.rect.top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.rectangle(frame, (obj.rect.left, obj.rect.top), (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height), (0, 255, 0), 2)
    # Hiển thị khung camera
    cv2.imshow('NHAN DIEN QR', frame)
    # Thoát khỏi loop nếu nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):   
        break
# Giải phóng camera và đóng cửa sổ hiển thị ảnh
cap.release()
cv2.destroyAllWindows()   
        


