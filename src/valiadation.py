def validate_title(title):
    return len(title) > 0

def validate_description(descripcion):
    return len(descripcion) > 0

def validate_priority(priority):
    return priority in ["high", "mid", "low"]