import streamlit as st
import pickle
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import time

st.write("""
<style>
/* Move the sidebar to the right */
[data-testid="stSidebar"] {
    order: 2;
}
[data-testid="stHorizontalBlock"] > div:first-child {
    order: 1;
}
</style>
""", unsafe_allow_html=True)

st.title('Malaria Cell Detection Using CNN')

image = st.file_uploader('Upload Malaria Image' , type=['png'])

st.text('Acuuracy of Model:95%')


model = load_model("C:/Users/rohit/Data science/Major Project/model.h5")
#classifier = pickle.load(open("C:/Users/rohit/Data science/Major Project/Malaria.sav",'rb'))

bt1 = st.button('predict')

def prepareImage(img):
    input_shape = (64, 64)
    resized = cv2.resize(img, input_shape, interpolation=cv2.INTER_AREA)
    imgResult = np.expand_dims(resized, axis=0)
    imgResultult = imgResult / 255.0

    return imgResult


def classify(inp_image):
    #img = cv2.imread(inp_image)
    image_model = prepareImage(inp_image)
    result = model.predict(image_model, verbose=1)

    return result

if bt1:
    if image is not None:

        file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)

        # Predict the result
        result = classify(img)
        if result[0][0] == 1.0:
            st.success('Uninfected')
        else:
            st.error('infected')

        st.image(img, caption='Uploaded Image', use_column_width=True)
    else:
        st.warning('Upload the Image')
#st.file_uploade