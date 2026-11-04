# Time-table-Generation

A Streamlit app for planning exam seating. You upload three CSV files - faculty, room capacities and student roll numbers by branch - and the app assigns students to rooms based on capacity (alternating between branches), allocates invigilators to rooms in turn, and lets you download the timetable, a room summary and the seating arrangement as CSV files.

## Tech stack

- Python, Streamlit
- pandas, XlsxWriter

## Input files

- `Faculty.csv` - a `Faculty` column with invigilator names
- `RoomCapacity.csv` - `Room No` and `Capacity` columns
- `Students.csv` - one column per branch, each listing roll numbers

## How to run

```bash
pip install -r requirements.txt
streamlit run new_app.py
```
