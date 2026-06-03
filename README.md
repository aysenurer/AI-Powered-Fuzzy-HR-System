# 🤖 AI-Powered Fuzzy HR Decision System

# PROJE AÇIKLAMASI:

Bu proje, insan kaynakları süreçlerinde aday değerlendirmesini otomatikleştirmek amacıyla geliştirilmiş bulanık mantık (Fuzzy Logic) tabanlı bir karar destek sistemidir.

Sistem, adayların sayısal performans kriterlerini analiz ederek uygunluk skoru üretir, sonuçları açıklanabilir yapay zeka yaklaşımı ile yorumlar ve etkileşimli bir dashboard üzerinden sunar.

## 🎯 PROJE AMACI:

Geleneksel işe alım süreçlerinde subjektif değerlendirmeleri azaltmak ve:

- Daha tutarlı aday değerlendirmesi yapmak
- Çok kriterli karar verme sürecini modellemek
- Kararların açıklanabilir olmasını sağlamak
- İnsan kaynakları analizini görselleştirmek

## 🏗️ SİSTEM YAPISI VE MODULLER

Proje bağımsız çalışan modüllerden oluşmaktadır:

## 📊 Modül 1: Veri Üretim Sistemi (data_generator.py)
NumPy kullanılarak sentetik aday verisi üretilir

Adaylar aşağıdaki kriterlerle modellenir:

   - GPA
   - Experience (Deneyim)
   - Projects (Proje sayısı)
   - Test Score
   - Communication Skills

Veri CSV formatında kaydedilir

## 🧠 Modül 2: Fuzzy Logic Karar Motoru (fuzzy_engine.py)
Mamdani Fuzzy Inference System kullanılır

Girdi değişkenleri bulanık kümelere ayrılır:
   Low / Medium / High (GPA)
   Weak / Strong (Communication)
   Few / Many (Projects)

IF–THEN fuzzy kuralları ile aday uygunluğu hesaplanır
### Çıktı: Suitability Score (0–100)

## 🔍 Modül 3: Açıklanabilir Yapay Zeka (explainability.py)
Aday skorlarının neden oluştuğunu metinsel olarak açıklar

Kural tabanlı yorum üretir:
   - Yüksek GPA pozitif etki
   - Düşük iletişim negatif etki
   - Yüksek deneyim olumlu katkı sağlar

## 📈 Modül 4: Dashboard Arayüzü (app.py)
Streamlit tabanlı etkileşimli panel:

CSV dosyası yükleme

Aday sıralama sistemi

KPI kartları:
   - Toplam aday
   - Ortalama skor
   - En yüksek skor
   - Excellent aday sayısı

Filtreleme sistemi

Grafikler:
   - Skor dağılımı
   - Kategori dağılımı (pie chart)

En iyi aday önerisi

AI açıklama paneli

CSV export özelliği

## ⚙️ Kullanılan Teknolojiler
- Python
- Streamlit
- NumPy
- Pandas
- Matplotlib
- Scikit-Fuzzy

## 📂 Proje Yapısı
HR-Fuzzy-System/
│
├── app.py
├── fuzzy_engine.py
├── explainability.py
├── data_generator.py
├── requirements.txt
├── README.md
├── candidates.csv
└── data/

## 🚀 Kurulum ve Çalıştırma
Projeyi yerel makinenizde çalıştırmak için:

### 1. Depoyu klonlayın
   git clone <repo-link>
   cd HR-Fuzzy-System
### 2. Gerekli kütüphaneleri yükleyin
   pip install -r requirements.txt
### 3. Uygulamayı çalıştırın
   streamlit run app.py

## 📊 Sistem Özeti
Aday Verisi
    ↓
Fuzzy Logic Engine
    ↓
Uygunluk Skoru
    ↓
Explainability Module
    ↓
Streamlit Dashboard

# SONUÇ:
Bu proje, bulanık mantık yaklaşımı kullanarak insan kaynakları süreçlerinde:

- Çok kriterli değerlendirme
- Açıklanabilir yapay zeka
- Görselleştirilmiş karar destek sistemi sunmayı amaçlamaktadır.

### AYŞENUR ER - 23430070070