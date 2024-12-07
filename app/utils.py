import re

def validate_field(value, field_type):
    if field_type == "email":
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", value))
    elif field_type == "phone":
        return bool(re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value))
    elif field_type == "date":
        return bool(
            re.match(r"^\d{2}\.\d{2}\.\d{4}$", value) or
            re.match(r"^\d{4}-\d{2}-\d{2}$", value)
        )
    elif field_type == "text":
        return True
    return False

def determine_field_type(value):
    if validate_field(value, "date"):
        return "date"
    elif validate_field(value, "phone"):
        return "phone"
    elif validate_field(value, "email"):
        return "email"
    return "text"
