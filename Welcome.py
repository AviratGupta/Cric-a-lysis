import streamlit as st
from data.index import every_ball , matches


st.set_page_config( page_title="Multipage" , page_icon="f" )

st.title("Cricket-Analysis")
st.caption("A Project on Data Analysis and Machine Learning")
# st.markdown('''<hr style="margin-top : -5px">''' , unsafe_allow_html=True)
st.text('''The project includes a website that enables the user to check and analyze the performance of any Male or Female Cricketer with the help of *Graphs and Plots*. 
This website also helps to predict the score and win-lose ratio in any match.
An Exciting part of our project is that you can see which cricketers you look alike.''')
st.image(image="https://miro.medium.com/max/1074/1*-ZBb-KYdnQtrd8ZJ_6GLGA.png")

st.title("Our Datasets")
st.subheader("Meta data about each match that has ever happened in t20 international")
st.table(matches.head(8))
st.subheader("Ball by Ball data of every macth")
st.table(every_ball.head(8))

st.header("Objectives of our Project")
st.text('''Our objective for this project is to deeply analyze the performance of any male or female cricketer who played any international game. 
It is a one-stop platform where the user can analyze each cricketer and their performance in the T20 format against different teams and in different stadiums.
They can get score prediction and live win-lose ratio probability.''')


st.markdown('''## Tools Required/Platform Used


*Language:* Python.

*Platform:* Jupyter Notebook, PyCharm, Kaggle, Power BI.

*Library:* NumPy, pandas, Plotly, seaborn, matplotlib, Sklearn, TensorFlow, OpenCV2.

*Deployment:* AWS.

### Brief Profile of the Team

 1. **Name:** Abhilaksh Bansal
    
    **Roll No:** 19001015002
 2. **Name:** Avirat Gupta
    
    **Roll No:** 19001015009
 3. **Name:** Mayank Arya
 
    **Roll No:** 19001015032''')