guitar = "Gibson L-5 CES"
price = 16036

formatting_string = f"1922 {guitar} for about ${price:,}!"
print(formatting_string)

for i in range(11):
    result = 2 ** i
    print(f"2 ^ {i} is {result:>5}")