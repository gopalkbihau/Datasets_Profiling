import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components

# --- App Title and Description ---
st.title("CSV Data Profiler")
st.write("Upload a CSV file and get an automated data profile report.")
st.write("The report provides a comprehensive overview of the dataset, including statistics, correlations, and missing values.")

# --- File Uploader Widget ---
uploaded_file = st.file_uploader("Upload a file for profiling", type="csv")

# --- Process file and generate report when a file is uploaded ---
if uploaded_file is not None:
    # Use a try-except block to handle potential errors during file processing
    try:
        # Read the uploaded CSV file into a Pandas DataFrame
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully! A preview of your data is shown below.")
        st.dataframe(df.head()) # Display a preview of the DataFrame

        # Use a spinner to indicate that the report is being generated
        with st.spinner("Generating the profile report... This may take a few moments for larger files."):
            # Generate the ydata-profiling report
            # Using the ProfileReport class directly is the recommended approach.
            # The 'minimal' option is used to speed up generation, especially for large datasets.
            profile = ProfileReport(
                df,
                title=f"Profiling Report for {uploaded_file.name}",
                sort=None,
                html={"style": {"full_width": True}},
                minimal=True
            )

            # Save the report as an HTML string
            profile_html = profile.to_html()

        st.subheader("Data Profile Report")
        # Display the HTML report directly in the Streamlit app
        components.html(profile_html, height=1000, scrolling=True)

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
        st.write("Please ensure that you have uploaded a valid CSV file.")
