

# 1. Define custom exception class
class InvalidAPIKeyError(Exception):
    pass

def validate_api_key(key):
    # Rule 1: Check prefix
    if not key.startswith("sk-"):
        raise InvalidAPIKeyError(f"The key '{key}' is invalid; it must start with 'sk-'.")
    
    # Rule 2: Check length
    if len(key) < 12:
        raise InvalidAPIKeyError(f"The key length must be at least 12 characters.")

    print(f"API Key '{key}' is valid!")

# 2. Execution and error handling
try:
    validate_api_key("invalid_key_name")
except InvalidAPIKeyError as error:
    print(f"Validation Failed: {error}")
