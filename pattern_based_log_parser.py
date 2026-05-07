log = "ALERT | 2026-04-29 10:22:01 | USER=admin DST=8.8.8.8 SRC=10.0.0.1"

# Step 1: Split and clean the log
#Split the log at the delimiter
parts=log.split("|")

#Clean the log by trimming the spaces
for p in range(len(parts)):
    parts[p]=parts[p].strip()  

# Step 2: Create empty result dictionary
result = {}

# Step 3: Define known severities
severities = {"ALERT", "WARNING", "INFO", "CRITICAL"}

# Step 4: Identify timestamp, severity, and details section
for p in parts:

    # Timestamp detection
    if ":" in p and "-" in p:
        result["timestamp"] = p

    # Severity detection
    elif p in severities:
        result["severity"] = p

    # Remaining part is details
    else:
        details = p

# Step 5: Create mapping for clean field names
mapping = {
    "SRC": "src_ip",
    "DST": "dst_ip",
    "USER": "user"
}

# Step 6: Split details into fields
fields = details.split()

# Step 7: Parse each field
for field in fields:

    # Split key=value
    key, value = field.split("=")

    # Rename keys using mapping
    clean_key = mapping.get(key, key.lower())

    # Store in dictionary
    result[clean_key] = value

# Step 8: Print final parsed log
print(result)
