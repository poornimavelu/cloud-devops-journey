



class InvalidBucketNameError(Exception):
    pass


def valid_bucket_name(name):
    # Rule 1: Length check (3 to 63 characters)
    if len(name) < 3 or len(name) > 63:
        raise InvalidBucketNameError("Bucket name must be between 3 and 63 characters long.")
    
    # Rule 2: Casing check (no uppercase letters allowed)
    if any(char.isupper() for char in name):
        raise InvalidBucketNameError("Bucket name cannot contain uppercase letters.")
    
    # Rule 3: Formatting check (cannot start or end with a hyphen)
    if name.startswith('-') or name.endswith('-'):
        raise InvalidBucketNameError("Bucket name cannot start or end with a hyphen.")

    print(f"Bucket name '{name}' is valid!")

# Test with an invalid bucket name ("MyBucket" has uppercase letters)
try:
    valid_bucket_name("MyBucket")
except InvalidBucketNameError as err:
    print(f"Validation Failed: {err}")




################

class InvalidAPIKeyError(Exception):
    pass

def validate_api_key(key):
    if key.doesntstartswith("sk-"):
        print(f"the name {key} is invalid it must start with sk-")
        if len(key)<12:
            print("the length should be greater than 12")
            raise InvalidBucketNameError

try :
    validate_api_key("invalid_key_name")
except InvalidAPIKeyError as error:
    print (f"{key} is a invalid name please try again ")


#############################

class InvalidAPIKeyError(Exception):
    pass

def validate_api_key(key):
    if not key.startswith("sk-"):
        print(f"the name {key} is invalid it must start with sk-")
        if len(key)<12:
            print("the length should be greater than 12")
            raise InvalidBucketNameError

try :
    validate_api_key("sk-123poornima")
except InvalidAPIKeyError as error:
    print (f"{key} is a invalid name please try again ") 

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



    