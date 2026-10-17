# 
###################################

# raw_ips = ["10.0.0.1", "192.168.1.1", "10.0.0.1", "172.16.0.1", "192.168.1.1"]

# How would you write a loop to populate a list clean_ips containing only unique values in the order they were first seen: 
# ['10.0.0.1', '192.168.1.1', '172.16.0.1']? 
# Write the Python code.

# for raw in raw_ips:
#  raw_ips={"10.0.0.1", "192.168.1.1", "10.0.0.1", "172.16.0.1", "192.168.1.1"}
#  print("cleared ips are :",raw_ips)
###########################################

#DICTIONARY
# allocated_ram = 4 

# server_memory = {
#     "web": 8,
#     "api": 16,
#     "database": 64
# }


# for key in server_memory:
#     server_memory.get("Cache")
# else:
#     print (f"Allocated RAM: {allocated_ram}GB") 



system_status = {
    "CPU": "Normal",
    "Disk": "Warning",
    "Memory": "Critical"
}

for key,values in system_status.items():
 print(f"Component: {key} | Status :{values}")

