    
servers = [
    {"name": "web-server-01", "status": "ONLINE", "memory_usage": 45},
    {"name": "database-master", "status": "ONLINE", "memory_usage": 92},
    {"name": "redis-cache", "status": "OFFLINE", "memory_usage": 0},
    {"name": "auth-api", "status": "ONLINE", "memory_usage": 78},
    {"name": "backup-runner", "status": "ONLINE", "memory_usage": 88},
]

def check_servers():
    alert_count = 0  # 1. Initialize counter inside the function

    for server in servers:
        # Extract variables from current server dictionary for clean f-strings
        name = server["name"]
        status = server["status"].upper()
        memory = server["memory_usage"]

        # 2. Check conditions with matching indentation
        if status == "OFFLINE":
            print(f"[CRITICAL] {name} is DOWN!")
            alert_count += 1
        elif memory > 80:
            print(f"[WARNING]  {name} High Memory: {memory}%")
            alert_count += 1
        else:
            print(f"[HEALTHY]  {name} is running normally.")

    # 3. Print summary after the loop finishes
    print(f"\nTotal servers that need attention: {alert_count}")

# 4. Call the function
check_servers()