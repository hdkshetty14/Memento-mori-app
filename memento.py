import streamlit as st
import random
import datetime

# Title & quote
st.set_page_config(page_title="Digital Memento Mori", layout="wide")

st.markdown("""
    <style>
        .grid{
            display: grid;
            grid-template-columns: repeat(52, 10px);
            gap: 2px;
            margin-bottom:20px;
        }
        .box{
            width: 10px;
            height: 10px;
            background-color: #eee;
        }
        .lived{
            background-color: #e74c3c;
        }
        .future{
            background-color: #ecf0f1;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🪦Memento Mori - A Reminder Of Your Mortality")
st.markdown("> You could leave life right now. Let that determine what you do, and think. - Marcus Aurelius")
st.write("---")

# Date input
birthdate=st.date_input("📅 Enter your birthdate", min_value=datetime.date(1900,1,1))
today=datetime.date.today()

days_lived=(today-birthdate).days
weeks_lived=days_lived//7
weeks_total= 80*52
weeks_remaining=weeks_total-weeks_lived
st.subheader(f"You have approximately {weeks_remaining:,} weeks left.")


# Grid of Weeks
grid_html= '<div class="grid">'
for week in range(weeks_total):
    if week < weeks_lived:
        grid_html+= '<div class="box lived"></div>'
    else:
        grid_html+= '<div class="box future"></div>'
grid_html += '</div>'
        
st.markdown("### Your life in weeks")
st.markdown(grid_html, unsafe_allow_html=True)

# Quote of the day
quotes=[
    "You could leave life right now. Let that determine what you do, say, and think.",
    "Death is not opposite of life, but a part of it.",
    "It is not that we have a short time to live, but that we waste much of it.",
    "The one who puts the finishing touches on their life each day is never short of time."
]
st.markdown("### ☠️ Daily Reflections")
st.info(f"💭 {random.choice(quotes)}")

# Reflection box
st.markdown("### 📝 How will you use your time today?")
st.text_area("Write your thoughts here (not saved):")