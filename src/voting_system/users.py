def add_user(users: list[dict], name: str, password: str) -> list[dict]:
    """Add a new user if the name is not already taken."""
    name = name.strip()

    if not name:
        raise ValueError("Name cannot be empty.")
    if not password:
        raise ValueError("Password cannot be empty.")
    if any(u["username"] == name for u in users):
        raise ValueError("This user already exists.")

    return users + [{"username": name, "password": password}]


def login(users: list[dict], name: str, password: str) -> bool:
    """Check if the username and password match an existing user."""
    return any(u["username"] == name and u["password"] == password for u in users)