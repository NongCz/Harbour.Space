s = input()

alice_wins = s.count('A')
bob_wins = s.count('B')

if alice_wins > bob_wins:
    print("ALICE")
elif bob_wins > alice_wins:
    print("BOB")
else:
    print("DRAW")
