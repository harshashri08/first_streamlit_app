import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Dinner Menu')
streamlit.text ('🍈Gobimanchurian, Noodles & Palak Paneer')
streamlit.text('Bluemoon spicy 🍊 & Pshyc soda')
streamlit.text('🍎Chicken Rice , 🍍Ghee Rice &🍚 Handi Biryani')

streamlit.title('Build your own customized smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
streamlit.dataframe(fruits_to_show)
