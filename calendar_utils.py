from auth import get_calendar_service
from datetime import datetime

def fetch_events():
    service = get_calendar_service()
    now = datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime'
    ).execute()

    return events_result.get('items', [])

def classify_event(title):
    title = title.lower()
    if any(keyword in title for keyword in ["review", "plan", "analyze", "report", "budget"]):
        return "analytic"
    elif any(keyword in title for keyword in ["email", "call", "sync", "meeting", "check-in"]):
        return "admin"
    elif any(keyword in title for keyword in ["brainstorm", "write", "idea", "pitch", "design"]):
        return "creative"
    else:
        return "admin"
