import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# بارگذاری مدل و مدیریت استثنا
try:
    model = load_model('flower_classification_model.h5')
except Exception as e:
    st.error(f"مشکلی در بارگذاری مدل به وجود آمد: {e}")
    st.stop()

# لیست کلاس‌ها (برچسب‌های دسته‌ها)
class_labels = ['Lilly', 'Lutos', 'Orchid','Sun Flower' ,'Tulip' ]

# عنوان صفحه
st.title('تشخیص دسته‌بندی گل‌ها با استفاده از مدل از پیش آموزش‌دیده')

# آپلود تصویر
uploaded_file = st.file_uploader("لطفاً یک تصویر گل آپلود کنید", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # باز کردن تصویر
        img = Image.open(uploaded_file)
        
        # نمایش تصویر
        st.image(img, caption='تصویر آپلود شده.', use_column_width=True)
        
        # تبدیل تصویر به فرمت مناسب برای مدل
        img = img.resize((224, 224))  # تغییر سایز به 224x224
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # اضافه کردن بعد برای batch
        img_array /= 255.0  # مقیاس‌بندی پیکسل‌ها به [0, 1]

        # پیش‌بینی کلاس
        predictions = model.predict(img_array)
        predicted_class_index = np.argmax(predictions)
        predicted_class = class_labels[np.argmax(predictions)]
        prediction_confidence = np.max(predictions)  # درصد اطمینان پیش‌بینی

        # نمایش نتیجه
        st.write(f"مدل پیش‌بینی می‌کند که این گل: **{predicted_class}** است.")
        st.write(f"اطمینان پیش‌بینی: {prediction_confidence * 100:.2f}%")
    except Exception as e:
        st.error(f"مشکلی در پردازش تصویر به وجود آمد: {e}")
