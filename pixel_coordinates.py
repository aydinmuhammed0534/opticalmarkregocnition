import cv2
import numpy as np

def get_rectangle_coordinates(image_path):
    """
    Görüntüyü görüntüle ve kullanıcının koordinatlarını almak için dikdörtgenler çizmesine izin verir.
    Dikdörtgen çizmek için sol tıklayıp sürükleyin.
    Mevcut dikdörtgeni sıfırlamak için 'r' tuşuna basın.
    Çıkmak için 'q' tuşuna basın.

    """
    # Görüntüyü oku
    image = cv2.imread(image_path)
    if image is None:
        print(f"Hata: {image_path} adresindeki görüntü okunamadı")
        return []

    # Çizim için görüntünün bir kopyasını oluştur
    display_image = image.copy()

    # Dikdörtgen çizimi için değişkenler
    drawing = False
    ix, iy = -1, -1
    rectangles = []

    def mouse_callback(event, x, y, flags, param):
        nonlocal display_image, drawing, ix, iy

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y

        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing:
                # Çizim için geçici bir görüntü oluştur
                temp_image = display_image.copy()
                cv2.rectangle(temp_image, (ix, iy), (x, y), (0, 255, 0), 2)
                cv2.imshow('Image', temp_image)

        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            # Dikdörtgen koordinatlarını ekle
            rectangles.append((ix, iy, x, y))
            # Son dikdörtgeni çiz
            cv2.rectangle(display_image, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow('Image', display_image)
            print(f"Dikdörtgen koordinatları: ({ix}, {iy}, {x}, {y})")

    # Bir pencere oluştur ve fare geri çağrısını ayarla
    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', mouse_callback)

    # Görüntüyü görüntüle
    cv2.imshow('Image', image)

    # Kullanıcının çıkmak için 'q' veya sıfırlamak için 'r' tuşuna basmasını bekle
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r'):
            # Mevcut çizimi sıfırla
            display_image = image.copy()
            cv2.imshow('Image', display_image)

    # Temizle
    cv2.destroyAllWindows()

    return rectangles

if __name__ == "__main__":
    # Örnek kullanım
    image_path = "/Users/muhammedaydin/Desktop/opticForm/kirpilmis_cevaplar_alani.png"  # Görüntü yolunuzla değiştirin
    rectangles = get_rectangle_coordinates(image_path)

    # Toplanan tüm dikdörtgen koordinatlarını yazdır
    print("\nToplanan tüm dikdörtgen koordinatları:")
    for i, (x1, y1, x2, y2) in enumerate(rectangles, 1):
        print(f"Dikdörtgen {i}: ({x1}, {y1}, {x2}, {y2})")