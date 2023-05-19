from backend import slicingData,DataInfo
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

dataInput=st.sidebar.file_uploader("Input CSV file",type={"csv","txt"})

if dataInput:
    data=pd.read_csv(dataInput)
    df=pd.DataFrame(data)
    if st.sidebar.button("show data"):
        st.dataframe(df)
        st.write(DataInfo.info(data))
        st.write(DataInfo.description(data))
        

    num,cat=slicingData.slice(data)

    type=["categorical","numerical"]

    sel=st.sidebar.selectbox("SELECT DATATYPE",options=type)

    if sel=="categorical":
        sel_cat=st.sidebar.multiselect("SELECT CATEGORICAL DATA COLUMN",options=cat)
        st.line_chart(df[sel_cat])
        st.bar_chart(df[sel_cat])
        st.area_chart(df[sel_cat])
    
    elif sel=="numerical":
        sel_num=st.sidebar.multiselect("SEELECT NUMERICAL DATA COLUMN",options=num)
        st.line_chart(df[sel_num])
        st.bar_chart(df[sel_num])
        st.area_chart(df[sel_num])


    
with open('datasets/sample.zip', 'rb') as f:
    st.sidebar.download_button(
            label="Download Sample Data and Use It",
            data=f,
            file_name='smaple_data.zip',
            help = "Download some sample data and use it to explore this web app."
        )





