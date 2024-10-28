def is_palindrome(looking_str: str, index: int = 0) -> bool:

    # Base case: if we’ve reached the middle, it’s a palindrome
    if index >= len(looking_str) // 2:
        return True

    # Check if characters from both ends match
    if looking_str[index] != looking_str[-(index + 1)]:
        return False

    # Recursive call to check the next pair of characters
    return is_palindrome(looking_str, index + 1)
