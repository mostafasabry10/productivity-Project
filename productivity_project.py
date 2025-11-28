
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout= 'wide', page_title= 'Productivity Project')

st.image('https://news.blr.com/app/uploads/sites/3/2019/10/improve-productivity.jpg')

html_title = """<h1 style="color:white;text-align:center;"> Garment Employees Productivity EDA Project </h1>"""
st.markdown(html_title, unsafe_allow_html=True)

df = pd.read_csv('cleaned_df.csv', index_col= 0)

st.dataframe(df)

page = st.sidebar.radio('Pages', ['Univariate Analysis', 'Bivariate Analysis','MultiVariate Analysis'])

if page == 'Univariate Analysis':

    st.title('Univariate Analysis')

    for col in df.columns:

        st.plotly_chart(px.histogram(data_frame= df, x= col, title= col))

elif page == 'Bivariate Analysis' :
    
    st.plotly_chart(px.scatter(data_frame= df, x= 'team', y= 'actual_productivity',title= 'Does number of workers influence the productivity ?'))

    st.plotly_chart(px.box(data_frame= df, x= 'department', y= 'actual_productivity',title= 'Does department influence productivity ? '))

    prod_per_month = (df.groupby('month')['actual_productivity'].mean().sort_values(ascending= False).round(4) * 100).reset_index()

    st.plotly_chart(px.bar(data_frame= prod_per_month, x= 'month', y= 'actual_productivity', text_auto= True,
        title= 'What is the average productivity per month ?',
        labels= {'actual_productivity' : 'Average Productivity',},
        color_discrete_sequence= ['green']))

elif page == 'MultiVariate Analysis':

    prod_per_month_per_dept = (df.groupby(['month', 'department'])['actual_productivity'].mean().round(4) * 100).reset_index()
    
    st.plotly_chart(px.bar(data_frame= prod_per_month_per_dept, x= 'month', y= 'actual_productivity', text_auto= True, color= 'department',
        title= 'What is the average Productivity per Month per Department ?',
        labels= {'actual_productivity' : 'Average Productivity'}, barmode= 'group',
        color_discrete_sequence= ['green', 'purple']))
