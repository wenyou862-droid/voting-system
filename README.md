# Voting System

## 1. Brief Introduction

Voting_system is a command-line tool that allows one user to create a purchase request and invite several reviewers to vote on it, helping them make a decision together.

## 2. Details

### Problem Solved

Voting_system helps users make decisions when they want to buy a certain item. This tool can be shared by people living together, so they can gather everyone's opinion before a purchase. It can also help someone who is unsure whether to buy a product, by collecting opinions from friends.

### How to Use It

Different people share and use the same computer, logging in separately to create requests or vote.

## 3. Functions

1. **Create user** — Create a new user with a username and password
2. **List users** — See the names of existing users
3. **Login** — Users must log in before creating a request or voting
4. **Create request** — Create a new request, including: reviewers (voters), item to buy, quantity, price, and reason
5. **List requests** — Check whether a request has been created, and view all existing requests
6. **Vote on request** — Reviewers can share their opinion: approve or reject
7. **Exit** — End the program

## 4. Installation and Run
```
uv pip install -e .
uv run -m voting_system
```
## Example

Once running, you'll see a menu like this:

1. Create user
2. List users
3. Login
4. Create request
5. List requests
6. Vote on request
7. Exit<br>
Please enter your choice:

## 5. Project Structure
```
src/voting_system/
├── users.py     - User management
├── requests.py  - Request creation and validation
├── votes.py     - Voting logic
├── storage.py   - Persistent storage for users and requests
├── utils.py     - Input validation
└── cli.py       - Command-line interface
```
## 6. Limits and Future Work

- Passwords are currently stored in plain text, without encryption; they are used only to distinguish user identity for this demo.
- The system currently runs on a single machine; multiple users must take turns on the same device.
- Future versions could support multi-device collaboration, for example by sharing request files between devices.