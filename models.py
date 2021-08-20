import streamlit as st
import modeling

def app(): 
    st.header("Shankara's Models")
    st.write("More models on more data are coming!")

    st.session_state.sel = st.selectbox('Model', ['Linear', 'Logistic'])

    with st.container():
        if st.session_state.sel == 'Linear': 
            fig, accuracy, r2, y_hats = modeling.linear_regression()
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            st.plotly_chart(fig)
        if st.session_state.sel == 'Logistic': 
            fig, accuracy, y_hats = modeling.logistic_regression()
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            st.plotly_chart(fig)

    
    
