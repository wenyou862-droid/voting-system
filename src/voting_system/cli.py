from .requests import add_request
from .storage import load_requests, load_users, save_requests, save_users
from .users import add_user, login
from .utils import get_non_negative_float, get_positive_int
from .votes import cast_vote


def main():
    users = load_users()
    requests_list = load_requests()
    current_user = None

    while True:
        print("\n" + "-" * 30)
        if current_user:
            print(f"Logged in as: {current_user}")
        else:
            print("Not logged in")
        print("1. Create user")
        print("2. List users")
        print("3. Login")
        print("4. Create request")
        print("5. List requests")
        print("6. Vote on request")
        print("7. Exit")
        print( "-" * 30)
        choice = input("Please enter your choice: ")

        if choice == "1":
            name = input("User name: ")
            password = input("Password: ")
            try:
                users = add_user(users, name, password)
                save_users(users)
                print(f"Created user: {name.strip()}")
            except ValueError as error:
                print(error)
            input("\nPress Enter to return to menu...")
        elif choice == "2":
            if users:
                names = ", ".join(u["username"] for u in users)
            else:
                names = "None yet"
            print("Users:", names)
            input("\nPress Enter to return to menu...")
        elif choice == "3":
            name = input("Username: ").strip()
            password = input("Password: ").strip()
            if login(users, name, password):
                current_user = name
                print(f"Logged in as {current_user}")
            else:
                print("Wrong username or password.")
            input("\nPress Enter to return to menu...")
        elif choice == "4":
            if current_user is None:
                print("Please login first.")
            else:
                cancelled = False
                while True:
                    reviewer_input = input("Reviewers (comma separated usernames): ")
                    reviewers = [r.strip() for r in reviewer_input.split(",")]

                    existing_usernames = [u["username"] for u in users]
                    invalid = [r for r in reviewers if r not in existing_usernames]
                    if invalid:
                        print(f"These users don't exist yet: {', '.join(invalid)}")
                        retry = input("Type 'r' to re-enter reviewers, or 'm' to return to menu: ").strip().lower()
                        if retry == "m":
                            cancelled = True
                            break
                        else:
                            continue

                    if current_user in reviewers:
                        print("You cannot be your own reviewer. Try again.")
                        continue

                    break

                if not cancelled:
                    item = input("What do you want to buy? ")
                    quantity = get_positive_int("Quantity: ")
                    price = get_non_negative_float("Price: ")
                    reason = input("Reason: ")
                    try:
                        requests_list = add_request(
                            requests_list, users, current_user, reviewers, item, quantity, price, reason)
                        save_requests(requests_list)
                        print("Request created!")
                    except ValueError as error:
                        print(error)
            input("\nPress Enter to return to menu...")
        elif choice == "5":
            if not requests_list:
                print("No requests yet.")
            else:
                for i, req in enumerate(requests_list, start=1):
                    approvers = [name for name, v in req["votes"].items() if v["decision"] == "approve"]
                    rejecters = [(name, v["reason"]) for name, v in req["votes"].items() if v["decision"] == "reject"]
                    pending = [r for r in req["reviewers"] if r not in req["votes"]]

                    print(f"{i}. {req['item']} x{req['quantity']} - ${req['price']} "
                          f"(by {req['created_by']})")
                    print(f"   Approvals ({len(approvers)}): {', '.join(approvers) if approvers else 'None'}")
                    if rejecters:
                        print(f"   Rejections ({len(rejecters)}):")
                        for name, reason in rejecters:
                            print(f"     - {name}: {reason}")
                    else:
                        print("   Rejections (0): None")
                    print(f"   Pending: {', '.join(pending) if pending else 'None'}")
            input("\nPress Enter to return to menu...")
        elif choice == "6":
            if current_user is None:
                print("Please login first.")
            elif not requests_list:
                print("No requests to vote on.")
            else:
                for i, req in enumerate(requests_list, start=1):
                    print(f"{i}. {req['item']} x{req['quantity']} - ${req['price']} "
                          f"(by {req['created_by']})")
                    print(f"   Reviewers: {', '.join(req['reviewers'])}")
                try:
                    choice_num = int(input("Which request number? "))
                    decision = input("approve or reject? ").strip().lower()
                    reason = ""
                    if decision == "reject":
                        reason = input("Reason for rejection: ").strip()
                    requests_list = cast_vote(requests_list, choice_num - 1, current_user, decision, reason)
                    save_requests(requests_list)
                    print("Vote recorded!")
                except ValueError as error:
                    print(error)
            input("\nPress Enter to return to menu...")
        elif choice == "7":
            break
        else:
            print("Please choose 1, 2, 3，4，5，6 or 7.")