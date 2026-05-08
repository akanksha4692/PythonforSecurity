# Processing Multiple Events

In cybersecurity automation, each log row represents one security event.

The parser converts:
- one CSV row → one dictionary
- multiple rows → list of dictionaries

- The standard cybersecurity pipeline
Raw logs
   ↓
Parse each event
   ↓
Convert to dictionary
   ↓
Store in list
   ↓
Run detections
   ↓
Generate alerts

Raw Logs
→ Parse rows
→ Convert to dictionaries
→ Store in list
→ Run detections

This approach is commonly used in:
- SIEM pipelines
- threat detection systems
- SOAR automation workflows

The project stores parsed events using:
- list of dictionaries

This structure makes it easier to:
- filter events
- detect suspicious activity
- count failed logins
- correlate events
