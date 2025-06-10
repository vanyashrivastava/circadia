def get_user_profile():
    print("\n💬 Welcome to Circadia – Built on the science of timing. Powered by you.")
    print("Optimize your daily rhythm with AI-powered insights.\n")

    print("📘 Let's discover your chronotype to personalize your timing suggestions.\n")

    print("🛏️ 1. What best describes your natural sleep pattern?")
    sleep = input(
        "Options:\n"
        "1. Early bird - I wake up naturally before 7 AM and feel most alert in the morning\n"
        "2. Night owl - I prefer to stay up late and wake up later in the day\n"
        "3. Somewhere in between - I adapt to different schedules fairly easily\n"
        "Enter 1, 2, or 3: "
    )

    print("\n⚡ 2. When do you typically feel most energetic and focused?")
    focus = input(
        "Options:\n"
        "1. Morning (6 AM - 12 PM)\n"
        "2. Afternoon (12 PM - 6 PM)\n"
        "3. Evening (6 PM - 12 AM)\n"
        "4. It varies day to day\n"
        "Enter 1, 2, 3, or 4: "
    )

    print("\n🎨 3. When do you feel most creative and innovative?")
    creativity = input(
        "Options:\n"
        "1. Early morning (6-9 AM)\n"
        "2. Mid-morning (9 AM-12 PM)\n"
        "3. Afternoon (1-5 PM)\n"
        "4. Evening (6-10 PM)\n"
        "Enter 1, 2, 3, or 4: "
    )

    print("\n☕ 4. How much caffeine do you typically consume?")
    caffeine = input(
        "Options:\n"
        "1. None - I avoid caffeine\n"
        "2. Light - 1-2 cups of coffee/tea per day\n"
        "3. Moderate - 3-4 cups per day\n"
        "4. Heavy - 5+ cups per day\n"
        "Enter 1, 2, 3, or 4: "
    )

    print("\n🧠 5. When do you make your best decisions?")
    decision = input(
        "Options:\n"
        "1. Morning - when my mind is fresh\n"
        "2. After lunch - when I've had time to think\n"
        "3. Evening - after reflecting on the day\n"
        "4. Under pressure - regardless of time\n"
        "Enter 1, 2, 3, or 4: "
    )

    # Map answers to labels
    sleep_map = {"1": "Early bird", "2": "Night owl", "3": "Somewhere in between"}
    focus_map = {"1": "Morning", "2": "Afternoon", "3": "Evening", "4": "Variable"}
    creativity_map = {"1": "Early morning", "2": "Mid-morning", "3": "Afternoon", "4": "Evening"}
    caffeine_map = {"1": "None", "2": "Light", "3": "Moderate", "4": "Heavy"}
    decision_map = {"1": "Morning", "2": "Afternoon", "3": "Evening", "4": "Under pressure"}

    def infer_chronotype(sleep, focus):
        if sleep == "Early bird" and focus == "Morning":
            return "Lark"
        elif sleep == "Night owl" and focus in ["Afternoon", "Evening"]:
            return "Owl"
        else:
            return "Third Bird"

    profile = {
        "chronotype": infer_chronotype(sleep_map[sleep], focus_map[focus]),
        "sleep_pattern": sleep_map[sleep],
        "energy_peak": focus_map[focus],
        "creativity_window": creativity_map[creativity],
        "caffeine_intake": caffeine_map[caffeine],
        "decision_time": decision_map[decision],
    }

    print("\n✅ Profile created! Here’s your rhythm summary:")
    for key, value in profile.items():
        print(f"• {key.replace('_', ' ').capitalize()}: {value}")

    return profile

# If running directly:
if __name__ == "__main__":
    user_profile = get_user_profile()
