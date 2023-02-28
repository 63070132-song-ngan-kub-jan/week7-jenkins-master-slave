with open('./name.txt', encoding='utf-8') as name_file:
    name = name_file.read().strip()

with open('./age.txt', encoding='utf-8') as age_file:
    age = age_file.read().strip()

greeting = "Hello, " + name + "!"

if age:
    greeting += " You are " + age + " years old."

print(greeting)

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("name", help="the name to greet")
# parser.add_argument("--age", help="the age of the person being greeted", type=int)
# args = parser.parse_args()

# greeting = "Hello, " + args.name + "!"
# if args.age:
#     greeting += " You are " + str(args.age) + " years old."

# print(greeting)
