substring = input().split(", ")
more_words = input()
match = []
match = [item for item in substring if item in more_words and item not in match]

print(match, end="")

