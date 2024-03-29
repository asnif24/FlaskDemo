user = {"username": "jose", "access_level": "guest"}
# user = {"username": "jose", "access_level": "admin"}

def get_admin_password():
    return "1234"

# def secure_function(func):
#     if user["access_level"] == "admin":
#         return func        
# get_admin_password = secure_function(get_admin_password)

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permitions for {user['username']}."
    
    return secure_function
get_admin_password = make_secure(get_admin_password)

print(get_admin_password())