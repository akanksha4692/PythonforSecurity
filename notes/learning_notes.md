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

# Linux Authentication Log Parser

A beginner cybersecurity automation project written in Python to parse Linux authentication logs and convert them into structured dictionary data.

This project focuses on:
- syslog parsing
- field extraction
- keyword-based parsing
- pattern matching
- cybersecurity automation fundamentals

---

# Current Capabilities

The parser can currently:

- Extract timestamp
- Extract hostname
- Extract service name
- Extract username
- Extract source IP
- Extract port
- Detect failed login activity

---

# Parsing Approach

The parser uses:

## 1. String Splitting

Used:
- `split()`

Purpose:
- break raw logs into searchable parts

---

## 2. List Slicing

Used to extract:
- timestamp components

Example concept:
- first three values form timestamp

---

## 3. Keyword-Based Extraction

The parser identifies fields dynamically using keywords instead of fixed positions.

Examples:
- after `for` → username
- after `from` → source IP
- after `port` → port number

Purpose:
- make parsing more flexible

---

## 4. Pattern Matching

Used to identify actions such as:
- failed login attempts

Purpose:
- basic detection logic
