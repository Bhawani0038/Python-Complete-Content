# 28. Event Registration Function

def register_event(name, event_type, **details):
    record = {
        "name": name,
        "event_type": event_type,
    }
    record.update(details)
    return record


print(register_event("Seminar", "Workshop", venue="Hall A", seats=40))
