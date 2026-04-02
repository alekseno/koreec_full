import secrets

def generate_task():
    return f"\'task_{secrets.token_bytes(16).hex()}\'"

def test_ff_task():
    res = generate_task()
    print(res)