containers = [
    {"name": "frontend-ui", "state": "running", "disk_percent": 40},
    {"name": "auth-service", "state": "stopped", "disk_percent": 15},
    {"name": "postgres-db", "state": "running", "disk_percent": 95},
    {"name": "payment-api", "state": "running", "disk_percent": 82},
    {"name": "cache-node", "state": "running", "disk_percent": 50},
]

def inspect_containers():
    issue_count =0


    for container in containers:
        name = container["name"]
        state=container["state"]
        disk_percent=container["disk_percent"]

        if container["state"].lower()=="stopped":
          print (f"[STOPPED]{name} is not running!")
          issue_count +=1
        elif container["disk_percent"] >= 85:
          print (f"[DISK WARNING]{name} disk is full: {disk_percent}%")
          issue_count +=1
        else:
         print (f"[READY]{name} is healthy and ready")

    print ("The number of containers that need attention is:",issue_count)

inspect_containers()
