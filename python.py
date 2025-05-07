import streamlit as st
import random

# Title & quote
st.set_page_config(page_title="Digital Memento Mori", layout="wide")
st.title("🪦Memento Mori - A Reminder Of Your Mortality")
st.markdown("> You could leave life right now. Let that determine what you do, and think.* - Marcus Aurelius")
st.write("---")

# Age input
age=st.number_input("Enter your age:", min_value=1, max_value=100, value=22)
life_expectancy= 80
weeks_total= life_expectancy*52
week_lived= age*52

# Grid of Weeks
grid=""
for week in range(weeks_total):
    if week < week_lived:
        grid+= "🟥"
    else:
        grid+="⬜"
    if (week+1) % 52== 0:
        grid+= "\n"
st.markdown("### Your life in weeks")
st.text(grid)

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