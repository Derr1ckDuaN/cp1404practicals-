email_dict = {}

while True:
    email = input("Email: ").strip()

    if not email:
        break

    name_part = email.split('@')[0]
    name_parts = name_part.split('.')
    name = ' '.join(part.title() for part in name_parts)


    confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

    if confirmation not in ('', 'y'):
        name = input("Name: ").strip()

    email_dict[email] = name


for email, name in email_dict.items():
    print(f"{name} ({email})")


