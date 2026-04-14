  🔐 Python Password Manager

A simple command-line password manager built with Python.
It allows users to easily store, retrieve, search, and delete login credentials using a local JSON file.

✨ Features
Add new credentials (site, username, password)
Strong password validation system
Handles duplicate site names (choose to rename or overwrite)
Search credentials by username
Retrieve credentials by site name
Delete saved credentials
Stores all data locally in a JSON file
Includes unit tests using unittest
🧠 How It Works

All login data is stored locally in a JSON file:

login_details.json
Example structure:
{
    "gmail": {
        "username": "user1",
        "password": "Password1!"
    }
}
🚀 Installation & Run
1. Clone the repository
git clone https://gitlab.wethinkco.de/liqotscc-g-025/password_manager.git
cd password_manager
2. Run the program
python3 manager.py
📋 Menu Options

When you run the program, you will see:

1. Add password
2. Get password by site
3. Search by username
4. Delete password
5. Exit
🔐 Password Rules

To keep passwords strong, the system requires:

At least 8 characters
At least one uppercase letter
At least one lowercase letter
At least one number
At least one special character
🧪 Running Tests

You can run unit tests with:

python3 test_manager.py
Tests include:
Adding passwords
Overwriting existing entries
Searching by username
Deleting passwords
🧱 Project Structure
password_manager/
│
├── manager.py              # Main application
├── login_details.json      # Stored credentials
├── test_manager.py         # Unit tests
└── README.md               # Project documentation
⚠️ Security Notice

This project is for educational purposes only.

Passwords are stored in plain text inside a JSON file, which is not secure for real-world use.

For secure password management, consider using tools like:

Bitwarden
1Password

## Author

Liso Qotoyi

A Python learner and developer focused on building practical projects to improve skills in automation, security, and software development.

This project is part of a journey into real-world programming using CLI tools, file handling, and testing.

 GitHub



https://github.com/lisoqotoyi



