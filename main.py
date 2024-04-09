# Calculate percentage in Python

def is_what_percent_of(num_a, num_b):
    return (num_a / num_b) * 100


print(is_what_percent_of(25, 75))  # 👉️ 33.33
print(is_what_percent_of(15, 93))  # 👉️ 16.12903..
print(round(is_what_percent_of(15, 93), 2))  # 👉️ 16.13