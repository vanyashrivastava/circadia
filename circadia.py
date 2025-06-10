from calendar_utils import fetch_events, classify_event
from suggestions import suggest_time
from datetime import datetime
from questionnaire import get_user_profile

def run_circadia():
    print("📋 Welcome to Circadia: Built on the science of timing.\n")

    # Step 1: Get user's rhythm profile
    profile = get_user_profile()

    # Step 2: Fetch calendar events
    print("⏳ Fetching your upcoming calendar events...\n")
    events = fetch_events()

    if not events:
        print("✅ No upcoming events found.")
        return

    # Step 3: Classify and evaluate each event
    for event in events:
        title = event.get("summary", "Untitled Event")
        start = event["start"].get("dateTime") or event["start"].get("date")

        try:
            start_dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
            start_time_str = start_dt.strftime("%H:%M")
        except Exception:
            start_time_str = "Unknown"

        task_type = classify_event(title)
        suggestion_data = suggest_time(start_time_str, task_type, title, profile)

        suggested_time = suggestion_data.get("suggested_time", "Unknown")
        justification = suggestion_data.get("justification", "")

        print(f"📌 Event: {title}")
        print(f"   • Type: {task_type}")
        print(f"   • Scheduled: {start_time_str}")
        if suggested_time.lower() == start_time_str:
            print("   • Suggested: ✔ Optimal\n")
        else:
            print(f"   • Suggested: {suggested_time}")
            print(f"     ⤷ {justification}\n")

if __name__ == "__main__":
    run_circadia()
