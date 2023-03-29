import pnadas as pd 
import streamplit as st 
from prediction import predict

st.title("Air Quality Prediction")
st.markdown('A model for predicting the level of PM2.5 molecule in environment using factors are')
st.markdown('Dew Point(DEWP), Temperature(TEMP), Presser(PRES), Iws')


st.header("Environment Factors")
col1, col2 = st.columns(2)

with col1:
    st.text("Dew Point")
    dew = st.slider('Dew Point',30,10,0,-5,-15,-20)
    st.test('Temperature')
    temp = st.slider('Temperature',45,30,15,0,-10,-19)
    
with col2:
    st.text("Pressure")
    pres = st.slider('Pressure',1046,1005,1030,991,1015,1000)
    st.text('Iws')
    iws = st.slider('Iws',565,465,345,254,15,0.15)
    
st.text('')
if st.button("Predict level of Pm2.5"):
    result = predict(np.array([[dew,temp,pres,iws]]))
    st.test(result[0])

st.text