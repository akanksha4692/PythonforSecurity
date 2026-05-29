#Accepted password for user
Variation 1 in existing code : 
if "Failed" in log:
    result["action"] = "failed_login"

elif "Accepted" in log:
    result["action"] = "successful_login"

#Failed password for Invalid user

if "invalid" in parts:
    user_index=parts.index("user")
    user = parts[user_index + 1]
else:
    user_index = parts.index("for")
    user = parts[user_index + 1]
    

