

# # 1. Define custom exception class
# class InvalidAPIKeyError(Exception):
#     pass

# def validate_api_key(key):
#     # Rule 1: Check prefix
#     if not key.startswith("sk-"):
#         raise InvalidAPIKeyError(f"The key '{key}' is invalid; it must start with 'sk-'.")
    
#     # Rule 2: Check length
#     if len(key) < 12:
#         raise InvalidAPIKeyError(f"The key length must be at least 12 characters.")

#     print(f"API Key '{key}' is valid!")

# # 2. Execution and error handling
# try:
#     validate_api_key("invalid_key_name")
# except InvalidAPIKeyError as error:
#     print(f"Validation Failed: {error}")


#########################################################

# port = int(input("Enter target port: "))
# print (f"Target port is:{port}")

# if port != 80 and port != 443:
#     print("Access Denied: Unapproved Port")
# else:
#     print("Access Granted")

################################

# statuses = ["running", "stopped", "stopped", "running"]

# for status in statuses:
#     if status == "stopped":
#         statuses.remove(status)
# print(statuses)

# 

# pod_count = 0

# def provision_node():
#    global pod_count
#    pod_count +=1
# print(f"Node provisioned. Total: {pod_count}")

# provision_node()

pod_count = 0

def provision_node():
    global pod_count  # Explicitly tell Python: "Use the pod_count from outside"
    pod_count += 1
    print(f"Node provisioned. Total: {pod_count}")

provision_node()
# Output: Node provisioned. Total: 1