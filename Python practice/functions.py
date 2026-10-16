def print_cluster_status():
    print("Cluster health: OK All nodes active.")
print_cluster_status()
print_cluster_status()
###########################################################################
def format_log(service_name,status_code):
  print(f"SERVICE:{service_name} Status returned: {status_code}")
format_log("auth_api",200)
format_log("database",500)
############################################################################
def calculate_storage_cost(gigabytes,rate_per_gb):
   int= gigabytes*rate_per_gb
   return int
calculate_storage_cost(500, 0.08)
monthly_bill= calculate_storage_cost;
print("Monthly bill is: $" + str(monthly_bill))
##############################################################################
def calculate_storage_cost(gigabytes, rate_per_gb):
    total_cost = gigabytes * rate_per_gb
    return total_cost

# Call the function with arguments and store its returned value in monthly_bill
monthly_bill = calculate_storage_cost(500, 0.08)

print("Monthly bill is: $" + str(monthly_bill))
#############################################################################
def is_high_latency (latency_ms):
   if(latency_ms>100):
      return True
   else:
      return False
print((is_high_latency(120)))
print((is_high_latency(45)))

###########################################

def validate_resource_tag(tag_name):
   if len(tag_name)<3 or len(tag_name)>10:
    return "INVALID:length error"
   if tag_name[:4]:
    return "INVALID: Missing env- prefix"
   return "VALID:"+ tag_name
validate_resource_tag("prod")
validate_resource_tag("env-production-database")
validate_resource_tag("env-dev")

def validate_resource_tag(tag_name):
    # 1. Length check: strictly less than 3 or strictly greater than 10
    if len(tag_name) < 3 or len(tag_name) > 10:
        return "INVALID: Length error"
    
    # 2. Prefix check: first 4 characters must be "env-"
    if tag_name[:4] != "env-":
        return "INVALID: Missing env- prefix"
    
    # 3. Passed all checks
    return "VALID: " + tag_name

# Testing with quoted string arguments wrapped in print()
print(validate_resource_tag("prod"))
print(validate_resource_tag("env-production-database"))
print(validate_resource_tag("env-dev"))

