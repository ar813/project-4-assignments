import hashlib  # Import hashlib for hashing

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

db = {
    "arsalan@gmail.com": hash_password("arsalan_123"),
    "rafay@gmail.com": hash_password("rafay_123"),
    "ayan@gmail.com": hash_password("ayan_123"),
    "naeem@gmail.com": hash_password("naeem_123"),
    "farzana@gmail.com": hash_password("farzana_123"),
}

    
email = input("Enter your email: ")
password = input("Enter your password: ")

if email in db:
    if db[email] == hash_password(password):
        print("✅ Login Successful!")
    else:
        print("❌ Incorrect password!")
else:
    print("❌ Email not found!")