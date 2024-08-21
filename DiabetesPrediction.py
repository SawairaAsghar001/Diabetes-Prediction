#pip install streamlit
#pip install pandas
#pip install sklearn

import streamlit as st 
import pandas as pd 
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from PIL import Image

#data collection and analysis
df = pd.read_csv(r'E:\Projects\Project 2\diabetes.csv')

#printing the first file 5 rowns of the dataset
st.title('Diabetes Checkup')

st.subheader('Training Data')
st.write(df.describe())

st.subheader('Visualtisation')
st.bar_chart(df)

x=df.drop([Outcome], axis= 1)
y = df.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test__split(x, y, test_size = 0.2, random_state = 0)
def user_report():
    pregancies = st.sliebar.slider('Pregancies', 0, 17, 3)
    glucose = st.sliebar.slider('Glucose', 0, 200, 120)
    bp = st.sliebar.slider('Blood   Pressure', 0, 122, 70)
    skinthickness = st.sliebar.slider('Skin Thickness', 0, 100, 20)
    insulin = st.sliebar.slider('Insulin', 0, 846, 79)
    bmi = st.sliebar.slider('BMI', 0, 67, 20)
    dpf = st.sliebar.slider('Diabetes Pedgree Function', 00., 2.4, 0.47)
    age = st.sliebar.slider('Age', 21, 88, 33)


    user_report ={
        'pregances': pregancies,
        'glucose': glucose,
        'bp':bp,
        'skinthickness': skinthickness,
        'insulin': insulin,
        'bmi': bmi,
        'dpf':dpf,
        'age' :age
    }

    report_data = pd.dataframe(user_report, index=[0])
    return report_data

    user_data = user_report()
    rf = RandomForestClassifier()
    rf.fit(x_train , y_train)

    st.subheader('Accuracy: ')
    st.write(str(accuracy_score(y_test, rf.predict(x_test))*100)+'%')

    user_result = rf.predict(user_data)
    st.subheader('Your Report: ')
    output= ''
    if user_result[0]==0:
        output = 'You are Healthy'
    else:
            output = 'You are Diabetic'


    st.write(output)


