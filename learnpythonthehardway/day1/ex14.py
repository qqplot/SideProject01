from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I am a {script} script.")
print("I have some # QUESTION. ")
print(f"{user_name}, Do you like me?")
like = input(prompt)

print(f"{user_name}, Where do you live now?")
live = input(prompt)

print("What kind of computer you have?")
computer = input(prompt)

print(f"""
Good, the answer of Do you like me is {like}.
you live in {live}. I don't know where it is.
And you have a {computer} computer. Awesome! 
""")
