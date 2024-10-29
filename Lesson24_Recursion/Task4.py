def reverse(input_str: str) -> str:
    if len(input_str) <= 1:
        return input_str

    return reverse(input_str[1:]) + input_str[0]


print(reverse("hello"))  # Output: "olleh"
print(reverse("o"))  # Output: "o"
print(reverse(""))  # Output: ""
