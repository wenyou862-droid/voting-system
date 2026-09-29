def cast_vote(requests: list[dict], request_index: int, voter: str, decision: str, reason: str = "") -> list[dict]:
    """Record a vote from a reviewer on a specific request."""
    if request_index < 0 or request_index >= len(requests):
        raise ValueError("Invalid request number.")

    request = requests[request_index]

    if voter not in request["reviewers"]:
        raise ValueError("You are not a reviewer for this request.")
    if voter in request["votes"]:
        raise ValueError("You have already voted on this request.")
    if decision not in ("approve", "reject"):
        raise ValueError("Decision must be 'approve' or 'reject'.")

    request["votes"][voter] = {"decision": decision, "reason": reason}
    return requests