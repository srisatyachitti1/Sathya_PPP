def count_up_to(limit):
    count = 0
    while count < limit:
        yield count
        count += 2
        # 0 2 4

# Using the generator
for number in count_up_to(5):
    # number in [0,2,4]
    print(number)