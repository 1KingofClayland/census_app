# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'census_app.py'.

# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_option("deprecation.showPyplotGlobalUse", False)

@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race', 'gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

# Add title on the main page and in the sidebar.
st.title("Census Data Visualization Web App")
st.sidebar.title("Census Data Visualization Web App")
# Using the 'if' statement, display raw data on the click of the checkbox.
if st.sidebar.checkbox("Show raw data"):
  st.subheader("Census Dataset")
  st.dataframe(census_df)
# Add a multiselect widget to allow the user to select multiple visualisations.
# Add a subheader in the sidebar with the label "Visualisation Selector"
st.sidebar.subheader("Visualization Selector")
# Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
# Store the current value of this widget in a variable 'plot_list'.
plot_list = st.sidebar.multiselect("Plots/Charts", ["Pie Chart", "Box Plot", "Count Plot"])
# Display pie plot using matplotlib module and 'st.pyplot()'
if "Pie Chart" in plot_list:
	st.subheader("Pie Chart of Income Group")
	plt.figure(figsize=(20,5))
	class_count = census_df["income"].value_counts()
	plt.pie(class_count, labels=class_count.index, autopct="%1.2f%%", startangle=30)
	st.pyplot()
	st.subheader("Pie Chart of Gender")
	plt.figure(figsize=(20,5))
	class_count = census_df["gender"].value_counts()
	plt.pie(class_count, labels=class_count.index, autopct="%1.2f%%", startangle=30)
	st.pyplot()
# Display box plot using matplotlib module and 'st.pyplot()'
if "Box Plot" in plot_list:
	st.subheader("Box Plot of Income Group")
	plt.figure(figsize=(20,5))
	sns.boxplot(x="hours-per-week", y="income", data=census_df)
	st.pyplot()
	st.subheader("Box Plot of Gender Group")
	plt.figure(figsize=(20,5))
	sns.boxplot(x="hours-per-week", y="gender", data=census_df)
	st.pyplot()
# Display count plot using seaborn module and 'st.pyplot()' 
if "Count Plot" in plot_list:
	st.subheader("Count Plot")
	plt.figure(figsize=(20,5))
	sns.countplot(x="workclass", hue="income", data=census_df)
	st.pyplot()