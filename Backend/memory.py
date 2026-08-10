from collections import defaultdict

MAX_HISTORY = 10

conversation_histories = defaultdict(list)


def add_message(session_id, role, content):

    history = conversation_histories[session_id]

    history.append({
        "role": role,
        "content": content
    })

    if len(history) > MAX_HISTORY * 2:
        history.pop(0)


def get_history(session_id):

    return conversation_histories[session_id]


def clear_history(session_id):

    conversation_histories[session_id] = []