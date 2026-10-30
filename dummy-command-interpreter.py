Tokens = []
state = True

def parser(command):
    command = command.lstrip()
    if "add" in command:    
        Tokens = command.split(" ")
        Tokens.pop(0)
        Tokens = [int(x) for x in Tokens if x != " "]
        return sum(Tokens)

    if "subtract" in command:
        Tokens = command.split(" ")
        Tokens.pop(0)
        Tokens = [int(x) for x in Tokens]
        return Tokens[0]-sum(Tokens[1:])    
while state != False:
    command = input(">>> ")
    print(parser(command))
