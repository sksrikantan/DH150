import streamlit as st 

def app(): 
    st.title("Theory")
    st.write("""I am working on this section. It will eventually contain 
    descriptions of the methods of data collection and modeling in this project. I 
    also hope to overview some of the theory of election predictions that inspired 
    this work.""")
    st.write("""We can appreciate that social class, and group and individual identities
    can predict, with high accuracy, election results.  
    Modeling elections based off of characteristics of the individual people that compose larger jurisdictions
    fails to account for many regional peculiarities. Perhaps many of these factors would be uncovered by 
    inclusion of more data. Perhaps not. This modeling approach also fails to consider anything related to 
    a particular election cycle. The relative strength of candidates, their campaign strategies, and the state of the nation (though I will try to control for
    time variables in a future edition of this), are ignored.
    I'm interested in how good these models are at predicting competitive races. My guess is, not that good. That might
    be a topic of future study. 
    Despite the result (you may say it's an obvious one) is that we can forecast the vast majority of electoral results 
    based on patterns of similar people voting in similar ways. """)
    st.write("""Below are important sources I used for this project. """)
    st.write("[MIT Data Lab]()")
    st.write ("[data.census.gov](https://data.census.gov/cedsci/)")
    st.write("[SMU Data Science Review](https://scholar.smu.edu/cgi/viewcontent.cgi?article=1005&context=datasciencereview)")