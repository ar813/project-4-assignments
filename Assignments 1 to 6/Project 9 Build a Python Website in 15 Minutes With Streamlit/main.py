import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of the web app
st.title('Streamlit Data Dashboard')

# User input for name
user_name = st.text_input('Enter your name:')

if user_name:
    st.write(f'Hello, {user_name}!')

    # Generate sample data
    data = {
        'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 20, 30, 40]
    }
    df = pd.DataFrame(data)

    # Display the dataframe
    st.write('Sample DataFrame:', df)

    # Plotting
    fig, ax = plt.subplots()
    ax.bar(df['Category'], df['Value'])
    ax.set_xlabel('Category')
    ax.set_ylabel('Value')
    ax.set_title('Sample Bar Chart')

    # Display the plot
    st.pyplot(fig)
else:
    st.write('Please enter your name to see the dashboard.')
