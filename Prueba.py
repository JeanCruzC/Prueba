import streamlit as st
from datetime import datetime

def main():
    st.title("Hora Actual")
    current_time = datetime.now().strftime("%H:%M:%S")
    st.write("La hora actual es:", current_time)

if __name__ == "__main__":
    main()