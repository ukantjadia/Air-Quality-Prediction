import cv2
import streamlit as st
import numpy as np 
from PIL import Image, ImageFilter, ImageEnhance

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.ukantjadia.me/linkedin" target="_blank">Ukant Jadia</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             <div class='footer'>
#             <p>LinkedIn<a style='display:block;text-align:center;' 
#             href='https://ukantjadia.me/linkedin' target='_blank'>Ukant Jadia</a></p>
#             </div>
#                 """

# st.markdown(hide_streamlit_style, unsafe_allow_html=True)


col1, col2 = st.columns([0.8,0.2])

with col1:
    st.markdown(""" <style> .font {
        font-size:35px,font-family:'Copper Black';color:#FF9633;
    }
    """,unsafe_allow_html=True)
    st.markdown('<p class="font"> Upload your photo here...</p>',unsafe_allow_html=True)
    file = st.file_uploader("",type=['png','jpg','jpeg'])


# with col2:
#     st.image()

st.sidebar.markdown('<p class="font"> Low Level Image Processing App</p>',unsafe_allow_html=True)

with st.sidebar.expander("About the App"):
    st.write("""
        This is a Simple Low level image processing app build with library Pillow, numpy, and streamlit in python. 
    """)
    

if file is not None:
    img = Image.open(file)

    col1,col2 = st.columns([0.5,0.5])
    with col1:
        st.markdown('<p style="text-align:centher;"> Before</p>',unsafe_allow_html=True)
        st.image(img,width=300)
        st.markdown("with Pillow ")

        st.image(img,width=300)

    with col2:
        st.markdown('<p style="text-align:center;"> After</p>',unsafe_allow_html=True)
        filter = st.sidebar.radio('Play with you Image:',['Original','Gray Image','Edge','Bright','Dark','Contrast'])
        if filter == 'Gray Image':
            gray_img = img.convert('L')
            np_gray = np.array(gray_img)
            st.image(gray_img,width=300)
            st.markdown('<p margin-top:5px><br> </p>',unsafe_allow_html=True)
            gray_img_cv = np.array(img.convert('RGB'))
            cv_gray = cv2.cvtColor(gray_img_cv,cv2.COLOR_RGB2GRAY)
            st.image(cv_gray,width=300)

        elif filter == "Bright":
            gray_img_cv = np.array(img.convert('RGB'))
            cv_gray = cv2.cvtColor(gray_img_cv,cv2.COLOR_RGB2GRAY)
            slider = st.sidebar.slider('Adjust the intensity(OpenCV)',1,255,127,step=1)
            (thresh, blackAndWhiteImage) = cv2.threshold(cv_gray,slider,255,cv2.THRESH_BINARY)
            st.image(blackAndWhiteImage,width=300)
            st.markdown(' ')
            st.markdown('<p margin-top:5px><br> </p>',unsafe_allow_html=True)
            gray_img = img.convert('L')
            np_gray = np.array(gray_img)
            shape = np_gray.shape
            img2 = np_gray.copy()
            slider = st.sidebar.slider("Adjust intensity",1,255,127,step=2)
            for row in range(0,shape[0]):
                for col in range(0,shape[1]):
                    img2[row][col] += slider
                    if img2[row][col] > 255:
                        img2[row][col]  = 255
            img1 = Image.fromarray(img2)
            st.image(img1,width=300)

        elif filter == "Dark":
            gray_img_cv = np.array(img.convert('RGB'))
            cv_gray = cv2.cvtColor(gray_img_cv,cv3.COLOR_RGB2GRAY)
            slider = st.sidebar.slider('Adjust the intensity(OpenCV)',1,255,127,step=1)
            (thresh, blackAndWhiteImage) = cv2.threshold(cv_gray,slider,255,cv2.THRESH_BINARY)
            st.image(blackAndWhiteImage,width=300)
            st.markdown('<p margin-top:5px><br> </p>',unsafe_allow_html=True)
            gray_img = img.convert('L')
            np_gray = np.array(gray_img)
            shape = np_gray.shape
            img2 = np_gray.copy()
            slider = st.sidebar.slider("Adjust intensity",2,255,step=2)
            for row in range(0,shape[0]):
                for col in range(0,shape[1]):
                    img2[row][col] -= slider
                    if img2[row][col] < 0:
                        img2[row][col]  = 0  
            img1 = Image.fromarray(img2)
            st.image(img1,width=300)

        elif filter == "Edge":
            gray_img_cv = np.array(img.convert('RGB'))
            cv_gray = cv2.cvtColor(gray_img_cv,cv2.COLOR_RGB2GRAY)
            inv_gray = 255 - gray_img_cv
            slider = st.sidebar.slider('Adjust the intensity(OpenCV)',25,255,125,step=2)
            blur_image = cv2.GaussianBlur(inv_gray,(slider,slider),0,0)
            sketch = cv2.divide(gray_img_cv,255-blur_image,scale=256)
            st.image(sketch,width=300)
            st.markdown('<p margin-top:5px><br> </p>',unsafe_allow_html=True)
            gray_img = img.convert('L')
            edges = gray_img.filter(ImageFilter.FIND_EDGES)
            st.image(edges,width=300)
            
        elif filter == "Contrast":
            gray_img = img.convert('L')
            np_gray = np.array(gray_img)
            shape = np_gray.shape
            img2 = np_gray.copy()
            slider = st.sidebar.slider("Adjust intensity",2,255,step=2)
            for row in range(0,shape[0]):
                for col in range(0,shape[1]):
                    img2[row][col] *= slider
                    if img2[row][col] > 255 :
                        img2[row][col]  = 255
                    if img2[row][col] < 0 :
                        img2[row][col]  = 0 

            img1 = Image.fromarray(img2)
            st.image(img1,width=300)
            st.markdown('<p margin-top:5px><br> </p>',unsafe_allow_html=True)
