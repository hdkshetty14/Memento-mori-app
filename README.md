# 🪦 Digital Memento Mori

> A minimalist, interactive reminder that your time is limited — built for digital minds.

This is a simple yet powerful web app inspired by the ancient Stoic practice of **Memento Mori** ("remember that you must die"). The app visualizes the weeks of your life based on your age and displays a daily quote to nudge reflection and mindful living.

---

## ⚙️ What It Does

- Accepts your **current age**
- Generates a **life calendar grid** (~4,160 weeks, assuming 80-year lifespan)
  - 🟥 for weeks lived
  - ⬜ for weeks remaining
- Displays a random **Memento Mori quote** on every load
- Provides a **text area for daily reflection** (not stored yet)

---

## 🔨 Tech Stack

- [Streamlit](https://streamlit.io/) – Rapid Python-based UI framework
- Python 3.10+
- No database or backend (for now)

---

## 🚧 Current Status: V1

We’re working on the **first version (V1)** — a minimal, clean prototype to bring the idea to life.  
Here’s what’s planned next:

- 📅 **Add precise birthdate input** → calculate weeks more accurately
- 🎨 **Improve the visual grid** → using HTML/CSS or canvas
- 💾 **Option to save reflections** (via Google Sheets, Firebase, etc.)
- 🌍 **Deploy publicly via Streamlit Cloud**
- 🔔 Notifications or reminders
- 🧠 AI-based life reflection prompts (experimental)

---

## 🚀 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/memento-mori.git
   cd memento-mori
