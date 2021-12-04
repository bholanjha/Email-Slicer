email = input("Enter Your Email: ").strip()
username = email[:email.index('@')]
print(username)
domain = email[email.index('@') + 1:]
print(domain)
