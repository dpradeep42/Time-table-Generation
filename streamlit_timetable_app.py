import streamlit as st
import pandas as pd
from timetable_generator import generate_timetable

# Streamlit App Layout
def main():
    st.title("Exam Timetable Generator")

    # Upload CSV Files
    st.sidebar.header("Upload Data")
    courses_file = st.sidebar.file_uploader("Upload Courses CSV", type="csv")
    students_file = st.sidebar.file_uploader("Upload Students CSV", type="csv")
    teachers_file = st.sidebar.file_uploader("Upload Teachers CSV", type="csv")

    if courses_file and students_file and teachers_file:
        # Load data
        courses = pd.read_csv(courses_file)
        students = pd.read_csv(students_file)
        teachers = pd.read_csv(teachers_file)

        st.write("### Uploaded Data")
        st.write("**Courses**")
        st.dataframe(courses)
        st.write("**Students**")
        st.dataframe(students)
        st.write("**Teachers**")
        st.dataframe(teachers)

        # Generate Timetable Button
        if st.button("Generate Timetable"):
            timetable = generate_timetable()

            # Display timetable in a formatted way
            st.write("### Generated Timetable")
            # Assuming timetable is returned as a DataFrame
            if isinstance(timetable, pd.DataFrame):
                st.dataframe(timetable)
            else:
                st.write(timetable)
    else:
        st.warning("Please upload all required files.")

if __name__ == "__main__":
    main()
