import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')




st.title('Employee Performance Web App')


#Data description
st.header('Data Description')
st.markdown('''
            INX Future Inc , (referred as INX ) , is one of the leading data analytics and automation solutions provider
with over 15 years of global business presence. INX is consistently rated as top 20 best employers past 5
years. INX human resource policies are considered as employee friendly and widely perceived as best
practices in the industry.
           The company decided to initiate a project involving data science department , which analyses the current employee data and find
the core underlying causes of this performance issues. The department expects the findings of this project will help the company to take right course of actions. The company also expects a clear indicators
of non performing employees, so that any penalization of non-performing employee, if required, may
not significantly affect other employee morals.
''')

