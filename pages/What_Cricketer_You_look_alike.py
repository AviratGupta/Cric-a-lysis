from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
from PIL import Image
import os
import cv2
from mtcnn import MTCNN
import numpy as np
from pathlib import Path

detector = MTCNN()
model = VGGFace(model='resnet50',include_top=False,input_shape=(224,224,3),pooling='avg')
#st.write(Path(__file__).parent.parent)

feature_list = pickle.load(open(os.path.join(Path(__file__).parent.parent,'embeddings.pkl'),'rb'))
filenames = pickle.load(open(os.path.join(Path(__file__).parent.parent,'filenames.pkl'),'rb'))

def save_uploaded_image(uploaded_image):
    try:
        with open(os.path.join(Path(__file__).parent.parent,'what_cricketer_you_look_alike','uploads',uploaded_image.name),'wb') as f:
            f.write(uploaded_image.getbuffer())
        return True
    except:
        return False

def extract_features(img_path,model,detector):
    img = cv2.imread(img_path)
    results = detector.detect_faces(img)
    # st.text(results)

    x, y, width, height = results[0]['box']

    face = img[y:y + height, x:x + width]

    #  extract its features
    image = Image.fromarray(face)
    image = image.resize((224, 224))

    face_array = np.asarray(image)

    face_array = face_array.astype('float32')

    expanded_img = np.expand_dims(face_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img)
    result = model.predict(preprocessed_img).flatten()
    return result

def recommend(feature_list,features):
    similarity = []
    for i in range(len(feature_list)):
        similarity.append(cosine_similarity(features.reshape(1, -1), feature_list[i].reshape(1, -1))[0][0])

    index_pos = sorted(list(enumerate(similarity)), reverse=True, key=lambda x: x[1])[0][0]
    return index_pos

st.title('Which Cricketer are you?')
file_image = st.file_uploader('Choose an image')
with st.expander("Click a image"):
    camera_image =  st.camera_input("Take a snap")
    if camera_image is not None:
        file_image = None
        
        
uploaded_image = file_image if file_image is not None else camera_image 

if uploaded_image is not None:
    st.image(uploaded_image ,width=300)
    # save the image in a directory
    if save_uploaded_image(uploaded_image):
        # load the image
        display_image = Image.open(uploaded_image)

        # extract the features
        features = extract_features(os.path.join(Path(__file__).parent.parent,'what_cricketer_you_look_alike' ,'uploads',uploaded_image.name),model,detector)


        # recommend
        index_pos = recommend(feature_list,features)
        predicted_c = " ".join(filenames[index_pos].split('\\')[-2].split('_'))
        
        # display
        col1,col2 = st.columns(2)

        with col1:
            st.header('Your uploaded image')
            # st.title(display_image)
            st.image(display_image , width=300 )
        with col2:
            im = cv2.imread(filenames[index_pos])
            im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            st.header("Seems like " + predicted_c)
            st.image(im,width=300)