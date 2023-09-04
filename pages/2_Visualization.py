import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
st.set_page_config(page_title="Visualisation", page_icon="📈")

st.sidebar.header("Visualisation")
st.title('Data Visualization')
#Load data
data = pd.read_csv('New_data.csv')

#Number of employees per department
st.set_option('deprecation.showPyplotGlobalUse', False)
st.header('Number of employees per Department')
# define Seaborn color palette to use
palette_color = sns.color_palette('autumn')
label = ['Sales','Development','Research & Development','Human Resources','Finance','Data Science ']
  
# plotting data on chart
plt.pie(data['EmpDepartment'].value_counts(), labels = label,
        shadow = True, explode = (0.05,0.1,0.05,0.05,0.05,0.05),
        colors=palette_color, autopct='%1.1f%%')

plt.title('Number of employees per department')
  
# displaying chart
st.pyplot()
st.markdown('''From the pie chart sales department has the highest number of employees.
             Data science has the least number of employees.''')


#Count Performance Visualisation
st.header('Count Performance Per Department')

#Count on perfomance rating in the departments
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize = (15,10))
sns.countplot(data = data, x ='EmpDepartment', hue ='PerformanceRating' )
st.pyplot()

st.markdown('''Despite sales department having the highest number of employees, Developement department had the highest number of both excellent and outstanding performance.''')
#Average performance rating
st.header('Average Performance Per Department')
st.markdown('''The graph below indicates how different departments performed averagely.
            ''')

x = data.groupby('EmpDepartment')['PerformanceRating'].mean().sort_values(ascending = True)

ax = x.plot(kind = 'barh', color = 'purple', title ='Average performance rating')
ax.bar_label(ax.containers[0], label_type='center', color='white', weight='bold')
plt.xlabel('Mean performance')
plt.ylabel('Departments')
st.pyplot()

st.markdown('''From this visualisation, Development department perfomed better in average performance. Data Science being a department with least number of employees was 
            the second best. Sales and Finance departments were the lowest in terms of average performance rating.''')