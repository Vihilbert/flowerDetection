### English Description

# 🌸 Flower Classification Using Pre-trained CNN Models

This project aims to classify various types of flowers using a Convolutional Neural Network (CNN) model. The model is built on top of a pre-trained DenseNet121 model, which is fine-tuned to recognize five different categories of flowers: **Lilly, Orchid, Sunflower, Tulip,** and **Other**. The project is designed to be user-friendly and interactive, allowing users to upload images of flowers and receive predictions from the trained model.

## Features
- **Pre-trained Model**: Utilizes the DenseNet121 model pre-trained on the ImageNet dataset for feature extraction.
- **Transfer Learning**: Fine-tuned on a custom dataset of flower images to classify into five categories.
- **Data Augmentation**: Applied to improve the model's robustness and accuracy.
- **Web Interface**: The project includes a Streamlit-based web app that allows users to upload flower images and get real-time predictions.
- **Visualization**: The project provides visual insights into the dataset and model performance, including accuracy and loss curves.

## How to Run the Project
### Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flower-classification.git
   cd flower-classification
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

### Online Deployment
You can also deploy the project online using platforms like Streamlit Community Cloud:
1. Push the repository to GitHub.
2. Log in to [Streamlit Community Cloud](https://streamlit.io/cloud) with your GitHub account.
3. Deploy the app by selecting the repository and the `app.py` file.

## Dataset
The dataset used in this project consists of images of different flower types, organized into folders by category. The dataset is split into training, validation, and test sets. Data augmentation techniques are applied during the training process to enhance the model's performance.

## Model Architecture
- **Base Model**: DenseNet121 (without the top layer)
- **Custom Layers**:
  - Batch Normalization
  - Fully Connected Layer with ReLU activation
  - Dropout for regularization
  - Output Layer with Softmax activation

## Results
The model achieves competitive accuracy on the validation and test datasets, making it a reliable tool for flower classification tasks. The training process is visualized through accuracy and loss curves.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### توضیحات فارسی

# 🌸 دسته‌بندی گل‌ها با استفاده از مدل‌های CNN از پیش آموزش‌دیده

این پروژه به هدف دسته‌بندی انواع مختلف گل‌ها با استفاده از یک مدل شبکه عصبی کانولوشنی (CNN) طراحی شده است. مدل مورد استفاده، بر روی مدل DenseNet121 که از قبل بر روی مجموعه داده ImageNet آموزش دیده است، ساخته شده و برای تشخیص پنج دسته مختلف از گل‌ها، شامل **سوسن، ارکیده، آفتابگردان، لاله** و **دیگر**، تنظیم شده است. این پروژه به گونه‌ای طراحی شده که کاربرپسند و تعاملی باشد، به کاربران امکان می‌دهد تصاویر گل‌ها را آپلود کرده و پیش‌بینی‌های مدل آموزش‌دیده را دریافت کنند.

## ویژگی‌ها
- **مدل از پیش آموزش‌دیده**: استفاده از مدل DenseNet121 که بر روی مجموعه داده ImageNet آموزش دیده است برای استخراج ویژگی‌ها.
- **یادگیری انتقالی**: تنظیم مدل بر روی یک مجموعه داده سفارشی از تصاویر گل‌ها برای دسته‌بندی به پنج دسته مختلف.
- **افزایش داده‌ها**: به کار گرفته شده برای بهبود استحکام و دقت مدل.
- **رابط وب**: پروژه شامل یک اپلیکیشن وب مبتنی بر Streamlit است که به کاربران امکان می‌دهد تصاویر گل‌ها را آپلود کرده و پیش‌بینی‌های لحظه‌ای دریافت کنند.
- **بصری‌سازی**: پروژه ارائه‌دهنده‌ی بینش‌های بصری از مجموعه داده و عملکرد مدل، شامل نمودارهای دقت و خطا است.

## نحوه اجرای پروژه
### راه‌اندازی محلی
1. مخزن را کلون کنید:
   ```bash
   git clone https://github.com/yourusername/flower-classification.git
   cd flower-classification
   ```
2. بسته‌های مورد نیاز را نصب کنید:
   ```bash
   pip install -r requirements.txt
   ```
3. اپلیکیشن Streamlit را اجرا کنید:
   ```bash
   streamlit run app.py
   ```

### استقرار آنلاین
همچنین می‌توانید این پروژه را به صورت آنلاین با استفاده از پلتفرم‌هایی مانند Streamlit Community Cloud منتشر کنید:
1. مخزن را به GitHub پوش دهید.
2. وارد [Streamlit Community Cloud](https://streamlit.io/cloud) شوید و با حساب GitHub خود وارد شوید.
3. برنامه را با انتخاب مخزن و فایل `app.py` مستقر کنید.

## مجموعه داده
مجموعه داده مورد استفاده در این پروژه شامل تصاویر از انواع مختلف گل‌ها است که در پوشه‌های مختلف بر اساس دسته‌بندی سازماندهی شده‌اند. این مجموعه داده به سه بخش آموزش، اعتبارسنجی و تست تقسیم شده است. تکنیک‌های افزایش داده در طول فرآیند آموزش برای بهبود عملکرد مدل به کار گرفته شده‌اند.

## معماری مدل
- **مدل پایه**: DenseNet121 (بدون لایه‌های بالایی)
- **لایه‌های سفارشی**:
  - نرمال‌سازی دسته‌ای
  - لایه کاملاً متصل با فعال‌سازی ReLU
  - Dropout برای منظم‌سازی
  - لایه خروجی با فعال‌سازی Softmax

## نتایج
این مدل به دقت قابل توجهی بر روی مجموعه‌های اعتبارسنجی و تست دست یافته است که آن را به ابزاری قابل اعتماد برای وظایف دسته‌بندی گل‌ها تبدیل می‌کند. فرآیند آموزش از طریق نمودارهای دقت و خطا بصری‌سازی شده است.

## مجوز
این پروژه تحت مجوز MIT منتشر شده است - برای جزئیات به فایل [LICENSE](LICENSE) مراجعه کنید.
