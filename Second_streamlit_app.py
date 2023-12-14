import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Dinner Menu')
streamlit.text ('🍈Gobimanchurian, Noodles & Palak Paneer')
streamlit.text('Bluemoon spicy 🍊 & Pshyc soda')
streamlit.text('🍎Chicken Rice , 🍍Ghee Rice &🍚 Handi Biryani')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page
