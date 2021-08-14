import streamlit as st
import modeling

def app(): 
    st.write("This is where models will go.")

    sel = st.selectbox('Model', ['Linear', 'Logistic'])

    with st.container():
        if sel == 'Linear': 
            accuracy, r2, y_hats = modeling.linear_regression()
            st.write ('Yooo we ran some lin reg')
        if sel == 'Logistic': 
            st.write ('We can some logistic biya')
    
    
