#Accepted password for user
Variation 1 in existing code : 
if "Failed" in log:
    result["action"] = "failed_login"

elif "Accepted" in log:
    result["action"] = "successful_login"
