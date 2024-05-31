import requests
import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib as plt 
from bokeh.plotting import figure


#st.title('Uber pickups in NYC')
st.write("Hello world")

st.title('This is a title') 

st.markdown(''' 
	:red[We] :orange[can] :green[write] :rainbow[colorful] 	:blue[text]''') 

code = '''def hello(): 
    print("Hello, Streamlit!")''' 
st.code(code, language='python') 


st.sidebar.title('Sidebar')
st.sidebar.write('This is where can add additional content or widgets.')

st.image('laura-cleffmann-EPJ3ptDEa0c-unsplash.jpg', caption='Moon')

with st.expander("See explanation"): 
    st.write(''' 
        Here we can show additional information. 
    ''') 

# Add more elements to the sidebar if needed
st.sidebar.header('Additional Information')


df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20))) 
st.dataframe(df)  # Same as st.write(df) 



arr = np.random.normal(1, 1, size=100) 
fig, ax = plt.pyplot.subplots() 
ax.hist(arr, bins=20) 
 
st.pyplot(fig) 

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

#p = figure(
#    title='simple line example',
#    x_axis_label='x',
#    y_axis_label='y')

#p.line(x, y, legend_label='Trend', line_width=2)

#st.bokeh_chart(p, use_container_width=True)

# Create the selectbox 
option = st.selectbox(
"How would you like to be contacted?", 
("Email", "Home phone", "Mobile phone") 
) 

# Display the selected option 
st.write("You selected:", option) 

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")

# Title of the app
st.title('CSV File Uploader and Analyzer')

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(uploaded_file)
    # Display the DataFrame
    st.write("DataFrame:")
    st.dataframe(df)

else:
    st.write("Please upload a CSV file to analyze.")