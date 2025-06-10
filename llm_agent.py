from openai import OpenAI
import json

client = OpenAI(api_key="OPENAI_API_KEY")

# === Circadian Science Summary from "When" ===
CIRCADIAN_KNOWLEDGE = """
KEY INSIGHTS FROM *WHEN* BY DANIEL H. PINK:

1. Daily Energy Rhythm (Larks & Third Birds): Peak (8AM–12PM) → Trough (1–4PM) → Rebound (4–8PM)
   - Use peak for analytical tasks (deep work, decision making).
   - Use trough for administrative or menial work (email, data entry).
   - Use rebound for creative or social tasks (brainstorming, outreach).

2. Night Owls: Their productive rhythm is reversed — Rebound → Trough → Peak.

3. Breaks:
   - Take short, frequent breaks, especially during troughs.
   - Movement, nature, and social contact help reset energy and attention.
   - “Caffeine nap” (coffee + 20 min nap) is highly restorative if timed right.

4. Starts, Middles, Ends:
   - Leverage “fresh start” dates (Mondays, birthdays) for motivation.
   - Use midpoint awareness to re-ignite momentum.
   - Endings shape memory — end strong for lasting impact.

5. Chronotypes have biological and genetic underpinnings; they influence decision quality, creativity, and energy levels.

6. Language and future planning: People who connect present with future selves tend to make wiser decisions and stick to long-term goals.

Based on these, Circadia should match task types to ideal time windows using:
- Task category (analytical, creative, admin)
- Chronotype (Lark, Owl, Third Bird)
- Questionnaire results
"""

def get_ai_suggestion(task, user_profile):
    profile_text = f"""
The user's rhythm profile:
- Chronotype: {user_profile['chronotype']}
- Sleep pattern: {user_profile['sleep_pattern']}
- Energy peak: {user_profile['energy_peak']}
- Creativity window: {user_profile['creativity_window']}
- Caffeine intake: {user_profile['caffeine_intake']}
- Decision-making strength: {user_profile['decision_time']}
"""

    prompt = f"""
You are Circadia, an AI productivity coach trained on *When: The Scientific Secrets of Perfect Timing* by Daniel Pink.

Your job is to evaluate the **ideal time window** to perform a task, using:
- The peak–trough–rebound model
- Chronotype and rhythm info from the questionnaire
- Task type (admin, creative, analytical)
- Scheduled time (if any) — if it’s already optimal, say so

Output ONLY a valid JSON object like:
{{
  "suggested_time": "HH:MM–HH:MM",
  "justification": "Evidence-based reasoning about why this is the best time based on the user's rhythm and the science from When."
}}

Task/Event: "{task}"

{profile_text}

RESEARCH KNOWLEDGE:
{CIRCADIAN_KNOWLEDGE}
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Circadia, a timing AI that strictly outputs structured JSON responses."},
            {"role": "user", "content": prompt}
        ]
    )

    text_response = response.choices[0].message.content.strip()

    try:
        parsed = json.loads(text_response)
        return parsed
    except json.JSONDecodeError:
        return {
            "suggested_time": "Unknown",
            "justification": f"⚠ Could not parse response: {text_response}"
        }
