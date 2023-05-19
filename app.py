from backend import slicingData,DataInfo,DataHandeling
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


dataInput=st.sidebar.file_uploader("Input CSV file",type={"csv","txt"})

if dataInput:
    data=pd.read_csv(dataInput)
    df=pd.DataFrame(data)

    process=st.sidebar.button("Fill Empty Values")
    if process:
        data=DataHandeling.fillna(data)
        df=pd.DataFrame(data)
        st.write("Null values filled")
    
    drop=st.sidebar.button("Drop rows with null values")
    if drop:
        data.dropna(axis=0,how="any")
        df=pd.DataFrame(data)
        st.write("Null value Columns dropped")
        
    st.sidebar.download_button(
            "Download processed file",
            df.to_csv(index=False).encode('utf-8'),
            "file.csv",
            "text/csv",
            key='download-csv'
            )


    if st.sidebar.button("show data"):
        st.dataframe(df)
        st.write(DataInfo.info(data))
        st.write(DataInfo.description(data))
        

    num,cat=slicingData.slice(data)

    type=["categorical","numerical"]

    sel=st.sidebar.selectbox("SELECT DATATYPE",options=type)

    if sel=="categorical":
        sel_cat=st.sidebar.multiselect("SELECT CATEGORICAL DATA COLUMN",options=cat)
        line=st.sidebar.checkbox("Line Chart")
        bar=st.sidebar.checkbox("Bar Chart")

        if line:
            st.line_chart(df[sel_cat])
        
        if bar:
            st.bar_chart(df[sel_cat])
        
    
    elif sel=="numerical":
        sel_num=st.sidebar.multiselect("SEELECT NUMERICAL DATA COLUMN",options=num)
        line=st.sidebar.checkbox("Line Chart")
        bar=st.sidebar.checkbox("Bar Chart")
        area=st.sidebar.checkbox("Area Chart")
       

        if line:
            st.line_chart(df[sel_num])
        
        if bar:
            st.bar_chart(df[sel_num])

        if area:
            st.area_chart(df[sel_num])
        
       



    
with open('datasets/sample.zip', 'rb') as f:
    st.sidebar.download_button(
            label="Download Sample Data and Use It",
            data=f,
            file_name='smaple_data.zip',
            help = "Download some sample data and use it to explore this web app."
        )





