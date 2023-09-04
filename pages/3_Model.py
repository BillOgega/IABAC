import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Modelling", page_icon="🌍")
st.sidebar.header("Modelling Demo")


st.title('Machine Learning Modelling')

st.markdown('''This demo can be used to predict the performance rating of an employee.''')

#Load data
data = pd.read_csv('New_data.csv')

#dropping the first column
data.drop('EmpNumber', inplace = True, axis = 1)

#encode categorical variables using ordinal encoding
from sklearn.preprocessing import OrdinalEncoder

#select all categorical variables
cat = data.select_dtypes(include = ['object'])

#apply ordinal encoder to categorical variables
encoder = OrdinalEncoder()
data[cat.columns] = encoder.fit_transform(cat)

# create my features and the target variable.
#Splitting the data into training and test sets
X = data.drop('PerformanceRating', axis = 1)
y = data['PerformanceRating']

# split the data into train and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier

# Create and fit the model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# show progress bar for model training
import time
with st.spinner('Training Model...'):
    time.sleep(5)
    st.success('Done')

# print model accuracy
st.subheader('Model Accuracy')
st.write(f'Model Accuracy: {rf.score(X, y)}')

# get user input
Age = st.number_input('Age')
MaritalStatus = st.selectbox('MaritalStatus:0-Divorced, 1-Married, 3-Single',('0','1','2'))
Gender = st.selectbox('Gender: 0-Female,1-Male',  ('0','1'))
EducationBackground = st.selectbox('EducationBackground: 0-Human Resources, 1-Life Sciences, 2-Marketing, 3-Medical, 4-Other,5-Technical Degree',('0', '1','2','3', '4','5'))
EmpDepartment = st.selectbox('Empdepartment:0-Data Science, 1-Development, 2-Finance, 3-Human Resources, 4-Research & Development, 5-Sales',('0','1','2','3','4','5'))
EmpJobRole = st.selectbox('EmpJobRole:0-Business Analyst ,1-Data Scientist ,2-Delivery Manager,3-Developer ,4-Finance Manger ,5-HealthCare Representative ,6-Human Resources ,7-Laboratory Technician ,8-Manager, 9-Maneger R&D ,10-Manufacturing Director ,11-Research Director ,12-Research Scientist ,13-Sales Executive ,14-Sales Representative ,15-Senior Developer ,16-Senior Manager R&D ,17-Technical Architect ,18-Technical Lead ', ('0','1','2','3','4','5','6','7','8','9','10','11','12','13', '14','15','16','17','18'))
BusinessTravelFrequency = st.selectbox('BusinessTravelFrequency:0-Non-Travel, 1-Travel_Frequently, 2-Travel_Rarely',('0','1','2'))
DistanceFromHome = st.number_input('DistanceFromHome')
EmpEducationLevel = st.selectbox('EmpEducationLevel: 1-Below College, 2-College, 3-Bachelor, 4-Master, 5-Doctor',('1','2','3','4','5'))
EmpEnvironmentSatisfaction = st.selectbox('EmpEnvironmentSatisfaction: 1-Low, 2-Medium, 3-High, 4-Very High',('1','2','3','4'))
EmpHourlyRate = st.number_input('EmpHourlyRate')
EmpJobInvolvement = st.selectbox('EmpJobInvolvement: 1-Low, 2-Medium, 3-High, 4-Very High ',('1','2','3','4'))
EmpJobLevel = st.number_input('EmpJobLevel')
EmpJobSatisfaction = st.selectbox('EmpJobSatisfaction: 1-Low, 2-Medium, 3-High, 4-Very High',('1','2','3','4'))
NumCompaniesWorked = st.number_input('NumCompaniesWorked')
OverTime = st.selectbox('OverTime:0-No , 1-Yes',('0','1'))
EmpLastSalaryHikePercent = st.number_input('EmpLastSalaryHikePercent')
EmpRelationshipSatisfaction = st.selectbox('EmpRelationshipSatisfaction: 1-Low, 2-Medium, 3-High, 4-Very High',('1','2','3','4'))
TotalWorkExperienceInYears = st.number_input('TotalWorkExperienceInYears')
TrainingTimesLastYear = st.number_input('TrainingTimesLastYear')
EmpWorkLifeBalance = st.selectbox('EmpWorkLifeBalance: 1-Low, 2-Medium, 3-High, 4-Very High',('1','2','3','4'))
ExperienceYearsAtThisCompany = st.number_input('ExperienceYearsAtThisCompany')
ExperienceYearsInCurrentRole = st.number_input('ExperienceYearsInCurrentRole')
YearsSinceLastPromotion = st.number_input('YearsSinceLastPromotion')
YearsWithCurrManager = st.number_input('YearsWithCurrManager')
Attrition = st.selectbox('Attrition: 0-No ,1-Yes ',('0', '1'))





# create a new dataframe 
X_new = pd.DataFrame({'Age': Age, 
                      'Gender': Gender, 
                      'EducationBackground': EducationBackground,
                      'MaritalStatus': MaritalStatus,
                      'EmpDepartment' : EmpDepartment,
                      'EmpJobRole' : EmpJobRole,
                      'BusinessTravelFrequency' : BusinessTravelFrequency,
                      'DistanceFromHome' : DistanceFromHome,
                       'EmpEducationLevel' : EmpEducationLevel,
                       'EmpEnvironmentSatisfaction': EmpEnvironmentSatisfaction,
                       'EmpHourlyRate' : EmpHourlyRate,
                       'EmpJobInvolvement' : EmpJobInvolvement,
                       'EmpJobLevel': EmpJobLevel,
                       'EmpJobSatisfaction': EmpJobSatisfaction,
                       'NumCompaniesWorked': NumCompaniesWorked,
                       'OverTime': OverTime,
                       'EmpLastSalaryHikePercent': EmpLastSalaryHikePercent,
                       'EmpRelationshipSatisfaction': EmpRelationshipSatisfaction,
                       'TotalWorkExperienceInYears': TotalWorkExperienceInYears,
                       'TrainingTimesLastYear': TrainingTimesLastYear,
                       'EmpWorkLifeBalance': EmpWorkLifeBalance,
                       'ExperienceYearsAtThisCompany': ExperienceYearsAtThisCompany,
                       'ExperienceYearsInCurrentRole': ExperienceYearsInCurrentRole,
                       'YearsSinceLastPromotion': YearsSinceLastPromotion,
                       'YearsWithCurrManager': YearsWithCurrManager,
                       'Attrition': Attrition}, 
                      index=[0])
#print the user input
st.subheader('User Input')
st.dataframe(X_new)


# make predictions and print them 
prediction = rf.predict(X_new)
st.subheader('Performance rating Prediction')
st.write(f'Employee Performance Rating is: {prediction}')
                      


