import streamlit as st
import pandas as pd
from io import StringIO

# Function to convert raw input to a single column
def convert_to_single_column(raw_text):
    # Split the input text into lines and then flatten to a single column
    lines = raw_text.splitlines()
    data = {'Column': lines}
    df = pd.DataFrame(data)
    return df

# Streamlit app
st.title('Raw to Single Column Converter')

# Input text area
raw_text = st.text_area('Enter your raw text here:', height=200)

# Convert button
if st.button('Convert'):
    if raw_text.strip() == "":
        st.error("Please enter some text.")
    else:
        # Convert raw text to a single column
        result_df = convert_to_single_column(raw_text)

        # Display the resulting DataFrame
        st.write('Converted Data:')
        st.dataframe(result_df)

        # Provide an option to download the result as a CSV
        csv = result_df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="single_column.csv">Download CSV file</a>'
        st.markdown(href, unsafe_allow_html=True)
