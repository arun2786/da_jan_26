title = "nAtUrE"

print(type(title))
print(title)
# nature
print(title.lower())
# NATURE
print(title.upper())


# print(f"-7: {title[-7]}") # error
print(f"-6: {title[-6]}")
print(f"Last char: {title[-1]}")
print(f"First char: {title[0]}")
print(f"Second char: {title[1]}")
print(f"Third char: {title[2]}")
print(f"Fourth char: {title[3]}")



print(f"Total char: {len(title)}")
print(f"Last char: {title[len(title)-1]}")
# print(f"Next to Last char: {title[6]}")

print(f"First 3 chars: {title[:3]}")

# Nature
# print(title.capitalize())

print(title[0].upper() + title[1:].lower())
