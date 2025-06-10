from llm_agent import get_ai_suggestion

def suggest_time(start_time, task_type, task_title, profile):
    return get_ai_suggestion(task_title, profile)
