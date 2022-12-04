import functools

user = {"username": "jose", "access_level": "guest"}
# user = {"username": "jose", "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permitions for {user['username']}."
    
    return secure_function

@make_secure
def get_admin_password():
    return "1234"
# equals to
# get_admin_password = make_secure(get_admin_password)
# by using @make_sure

print(get_admin_password())

print(get_admin_password.__name__)
# will get "secure_function" if didn't use @functools.wraps(func)

