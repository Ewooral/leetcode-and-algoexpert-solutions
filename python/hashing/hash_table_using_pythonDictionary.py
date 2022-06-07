voted = {}
def check_voter(name):
 if voted.get(name):
    print( "kick them out!")
 else:
    voted[name] = "Voted!"
    print( "let them vote!")
    print(voted)

check_voter("Elijah")
check_voter("Elijah")
check_voter("Kukua")