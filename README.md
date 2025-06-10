# 🕒 Circadia: Built on the Science of Timing

**Make what you do count more by doing it at the right time.**

---

## 📖 What is Circadia?

Circadia is a terminal-based productivity tool inspired by Daniel H. Pink's book *When: The Scientific Secrets of Perfect Timing*. It uses insights from **chronobiology** — the study of natural physiological rhythms — to help you schedule your day around your **biological peak performance windows**.

Powered by **generative AI**, Circadia analyzes your Google Calendar and suggests better timing for your tasks based on your **chronotype**:

🕊 **Lark** – Early riser
🦉 **Owl** – Night thinker
☕ **Third Bird** – Somewhere in between

---

## 🧠 How It Works

1. **Chronotype Quiz**: Answer 5 short questions to determine your internal rhythm profile.
2. **Google Calendar Scan**: Circadia fetches your upcoming events using the Google Calendar API.
3. **AI Suggestions**: GPT-4 analyzes each task and suggests optimal time windows using research from *When*.

---

## ⚙️ Current Features

✅ Terminal-based chronotype onboarding
✅ AI-powered timing recommendations
✅ Google Calendar integration (via OAuth)
✅ Justified suggestions using *When*-backed logic

> ❗ Note: Circadia currently runs **only in the terminal**. The AI backend and logic are fully coded in Python. The frontend UI is currently **mocked via Lovable** (see below).

---

## 🎨 UI Design 

The visual UI for Circadia was designed using [Lovable](https://whenbot-timing-ai.lovable.app/).
This prototype is **not connected to the backend yet**, but shows how Circadia could feel as a full product.

👉 [Live UI Preview](https://whenbot-timing-ai.lovable.app/)

---

## 🛠️ Installation & Setup

1. Clone the repo
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Add your `credentials.json` for Google Calendar OAuth
4. Run the app:

   ```bash
   python circadia.py
   ```

---

## 🤔 Would You Use It?

This is an early prototype, but I'm building it out based on your feedback.
**Would this help you schedule smarter?** Let me know!
