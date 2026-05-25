# Linux Authentication Log Parser

log = "Apr 29 10:22:01 server1 sshd[1234]: Failed password for admin from 10.0.0.1 port 22"

# Step 1: Split log into parts
parts = log.split()

# Step 2: Extract timestamp
timestamp = " ".join(parts[0:3])

# Step 3: Extract hostname
hostname = parts[3]

# Step 4: Extract service name
service = parts[4].split("[")[0]

# Step 5: Extract username
user_index = parts.index("for")
user = parts[user_index + 1]

# Step 6: Extract source IP
ip_index = parts.index("from")
src_ip = parts[ip_index + 1]

# Step 7: Extract port number
port_index = parts.index("port")
port = parts[port_index + 1]

# Step 8: Create structured dictionary
result = {}

result["timestamp"] = timestamp
result["hostname"] = hostname
result["service"] = service
result["user"] = user
result["src_ip"] = src_ip
result["port"] = port

# Step 9: Detect action
if "Failed" in log:
    result["action"] = "failed_login"

# Step 10: Print parsed log
print(result)
