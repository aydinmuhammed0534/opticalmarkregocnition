# Optik Form İsim Tanıma Sistemi / Optical Form Name Recognition System

[🇬🇧 English Version Below](#english-version)

## Türkçe

Bu proje, optik formlarda işaretlenen harflerden isim tanıma işlemini gerçekleştiren bir Python uygulamasıdır. OpenCV kütüphanesi kullanılarak geliştirilmiştir.

### Özellikler

- Optik formda işaretlenen kutuların tespiti
- Türkçe alfabeye uygun harf tanıma
- Görsel debug desteği
- Adaptif eşikleme ile farklı ışık koşullarına uyum
- Gürültü temizleme ve görüntü ön işleme

### Gereksinimler

```bash
pip install opencv-python
pip install numpy
```

### Kullanım

1. Projeyi klonlayın:
```bash
git clone [proje-url]
cd opticForm
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

3. Programı çalıştırın:
```bash
python name_recognition.py
```

### Kod Yapısı

#### Temel Fonksiyonlar

1. `preprocess_image(img)`: 
   - Görüntüyü gri tonlamaya çevirir
   - Adaptif eşikleme uygular
   - Gürültü temizleme işlemi yapar

2. `find_checkboxes(thresh, min_area=15, max_area=200)`:
   - İşaretlenen kutuları tespit eder
   - Alan bazlı filtreleme yapar
   - Kenar payı ekler

3. `group_checkboxes_by_row(checkboxes, row_threshold=15)`:
   - Tespit edilen kutuları satırlara göre gruplar
   - Dikey pozisyona göre sıralama yapar

4. `recognize_ad_soyad_final(image_path)`:
   - Ana tanıma fonksiyonu
   - ROI (İlgi Alanı) seçimi
   - Karakter tanıma ve görselleştirme

### Parametreler

- `min_area`: Minimum kutu alanı (varsayılan: 15 piksel)
- `max_area`: Maksimum kutu alanı (varsayılan: 200 piksel)
- `row_threshold`: Satır gruplama eşiği (varsayılan: 15 piksel)
- ROI koordinatları: x=38, y=183, w=280, h=352

### Debug Özellikleri

Program çalışırken iki pencere gösterir:
1. Debug penceresi: Tespit edilen kutuları yeşil çerçevelerle gösterir
2. Sonuç penceresi: Tanınan karakterleri kırmızı renkle gösterir

### Türkçe Karakter Desteği

Program aşağıdaki Türkçe karakterleri destekler:
```python
['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 
 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 
 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z']
```

### Hata Ayıklama

Eğer program istenilen sonucu vermiyorsa:
1. Eşik değerlerini ayarlayın (`min_area`, `max_area`)
2. ROI koordinatlarını kontrol edin
3. Debug penceresinden kutu tespitini gözlemleyin

### Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

### Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

### İletişim

Muhammed Aydın - [GitHub](https://github.com/muhammedaydiiinn)

---

# English Version

This project is a Python application that performs name recognition from marked letters on optical forms. It is developed using the OpenCV library.

### Features

- Detection of marked boxes on optical forms
- Turkish alphabet-compatible character recognition
- Visual debug support
- Adaptive thresholding for different lighting conditions
- Noise removal and image preprocessing

### Requirements

```bash
pip install opencv-python
pip install numpy
```

### Usage

1. Clone the project:
```bash
git clone [project-url]
cd opticForm
```

2. Install required libraries:
```bash
pip install -r requirements.txt
```

3. Run the program:
```bash
python name_recognition.py
```

### Code Structure

#### Core Functions

1. `preprocess_image(img)`: 
   - Converts image to grayscale
   - Applies adaptive thresholding
   - Performs noise removal

2. `find_checkboxes(thresh, min_area=15, max_area=200)`:
   - Detects marked boxes
   - Performs area-based filtering
   - Adds margin to boxes

3. `group_checkboxes_by_row(checkboxes, row_threshold=15)`:
   - Groups detected boxes by rows
   - Sorts by vertical position

4. `recognize_ad_soyad_final(image_path)`:
   - Main recognition function
   - ROI (Region of Interest) selection
   - Character recognition and visualization

### Parameters

- `min_area`: Minimum box area (default: 15 pixels)
- `max_area`: Maximum box area (default: 200 pixels)
- `row_threshold`: Row grouping threshold (default: 15 pixels)
- ROI coordinates: x=38, y=183, w=280, h=352

### Debug Features

The program shows two windows while running:
1. Debug window: Shows detected boxes with green frames
2. Result window: Shows recognized characters in red

### Turkish Character Support

The program supports the following Turkish characters:
```python
['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 
 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 
 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z']
```

### Debugging

If the program is not giving the desired results:
1. Adjust threshold values (`min_area`, `max_area`)
2. Check ROI coordinates
3. Observe box detection in the debug window

### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

### Contact

Muhammed Aydın - [GitHub](https://github.com/muhammedaydiiinn) 