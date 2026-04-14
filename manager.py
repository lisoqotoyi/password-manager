import json

FILE = "login_details.json"

# =========================
# File Handling
# =========================
def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# =========================
# Handle Duplicate Sites
# =========================
def handle_existing_site(data, site):
    while site in data:
        print("\n==== Site Manager ====")
        print(f"'{site}' already exists.")
        print("1. Change site name")
        print("2. Overwrite existing password")

        choice = input("Choose an option: ")

        if choice == "1":
            site = input("Enter a new site name: ")
        elif choice == "2":
            print("Overwriting existing password...")
            return site
        else:
            print("Invalid choice. Try again.")

    return site

# =========================
# Add Password
# =========================
def add_password(data):
    site = input("Site: ")
    site = handle_existing_site(data, site)

    username = input("Username: ")

    while True:
        password = input("Password: ")

        if len(password) < 8:
            print("Password must be at least 8 characters long")
            continue

        if not any(c.isupper() for c in password):
            print("Password must contain at least one uppercase letter")
            continue

        if not any(c.islower() for c in password):
            print("Password must contain at least one lowercase letter")
            continue

        if not any(c.isdigit() for c in password):
            print("Password must contain at least one number")
            continue

        if not any(not c.isalnum() for c in password):
            print("Password must contain at least one special character")
            continue

        break

    data[site] = {
        "username": username,
        "password": password
    }

    print("Saved!")

# =========================
# Get Password by Site
# =========================
def get_password(data):
    site = input("Enter site: ")

    if site in data:
        print("\n==== Saved Password ====")
        print(f"Site: {site}")
        print(f"Username: {data[site]['username']}")
        print(f"Password: {data[site]['password']}")
    else:
        print("Not found.")

# =========================
# Search by Username
# =========================
def search_by_username(data):
    search_user = input("Enter username to search: ")

    found = False
    print("\n==== Search Results ====")

    for site, details in data.items():
        if search_user.lower() in details["username"].lower():
            print(f"\nSite: {site}")
            print(f"Username: {details['username']}")
            print(f"Password: {details['password']}")
            found = True

    if not found:
        print("No accounts found with that username.")

# =========================
# Delete Password
# =========================
def delete_password(data):
    site = input("Enter site to delete: ")

    if site in data:
        print(f"\nFound entry for '{site}'")
        confirm = input("Are you sure you want to delete it? (y/n): ").lower()

        if confirm == "y":
            del data[site]
            print("Deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Site not found.")

# =========================
# Main Menu
# =========================
def main():
    data = load_data()

    while True:
        print("\n==== Password Manager ====")
        print("1. Add password")
        print("2. Get password by site")
        print("3. Search by username")
        print("4. Delete password")
        print("5. Exit")

        choice = input("Choice: ")

        if choice == "1":
            add_password(data)
            save_data(data)

        elif choice == "2":
            get_password(data)

        elif choice == "3":
            search_by_username(data)

        elif choice == "4":
            delete_password(data)
            save_data(data)

        elif choice == "5":
            save_data(data)
            print("Goodbye!")
            break

        else:
            print("Invalid option")

# =========================
# Run Program
# =========================
if __name__ == "__main__":
    main()