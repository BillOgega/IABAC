import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')


st.set_page_config(page_title="Dataset", page_icon="📈")
st.sidebar.header("Dataset")

st.title('Data Set')

st.markdown(''' 
            This is the data from employee performance rate of INX Future Inc.
            The data contains both numerical and object input variables. The data has twenty six features and one target variable which is the performance rating. The data has the following definitions:

            EmpEducationLevel 1 'Below College' 2 'College' 3 'Bachelor' 4 'Master' 5 'Doctor'

            EmpEnvironmentSatisfaction 1 'Low' 2 'Medium' 3 'High' 4 'Very High'

            EmpJobInvolvement 1 'Low' 2 'Medium' 3 'High' 4 'Very High'

            EmpJobSatisfaction 1 'Low' 2 'Medium' 3 'High' 4 'Very High'

            PerformanceRating 1 'Low' 2 'Good' 3 'Excellent' 4 'Outstanding'
            
            RelationshipSatisfaction 1 'Low' 2 'Medium' 3 'High' 4 'Very High'
            
            EmpWorkLifeBalance 1 'Bad' 2 'Good' 3 'Better' 4 'Best' ''')

#Load data
data = pd.read_csv('New_data.csv')

#get user input on how may rows to display
rows = st.slider('How many rows of data would you like to see?', 0,20,5)

#Display data
st.dataframe(data.head(rows))