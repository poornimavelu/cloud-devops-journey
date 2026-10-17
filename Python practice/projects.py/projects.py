
#Server Health & Alert Filter

# 1. The input data: List of dictionaries
servers = [
    {"name": "web-01", "cpu": 82, "ram": 65, "online": True},
    {"name": "db-01",  "cpu": 96, "ram": 88, "online": True},
    {"name": "auth-01", "cpu": 15, "ram": 40, "online": False},
    {"name": "api-01", "cpu": 45, "ram": 50, "online": True},
    {"name": "worker-01", "cpu": 91, "ram": 30, "online": True},
]

# 2. Storage for our findings
offline_nodes = []
overloaded_nodes = []

# 3. Process each server using a for loop and conditions
for node in servers:
    # Check if offline
    if not node["online"]:
        offline_nodes.append(node["name"])
        continue  # skip checking CPU if it's already dead

    # Check for critical thresholds (Defensive check)
    if node["cpu"] >= 90 or node["ram"] >= 85:
        overloaded_nodes.append({
            "name": node["name"],
            "cpu": node["cpu"],
            "ram": node["ram"]
        })

# 4. Print the final operational report
print("=== CLUSTER HEALTH REPORT ===")
print(f"Total nodes scanned: {len(servers)}")

print(f"\n[!] Offline Nodes ({len(offline_nodes)}):")
for name in offline_nodes:
    print(f"  - {name}")

print(f"\n[*] Critical Resource Warnings ({len(overloaded_nodes)}):")
for node in overloaded_nodes:
    print(f"  - {node['name']} -> CPU: {node['cpu']}%, RAM: {node['ram']}%")