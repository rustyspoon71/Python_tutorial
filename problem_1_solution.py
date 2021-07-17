# Tell me who was at party_1 but not at party_2. Then create a new set containing
# the people who didnt go to party 2 and the people who didn't go to party_1. Then
# output the set to know who wasn't at both parties. 

party_1 = {"Annie","Richie","Rosie","Becca","Ryland","Scott"}
party_2 = {"Annie","Richie","Rosie","Becca","Samantha","Mom","Dad"}

# Put your code here you may use any type of operations.

# Get people who only went to one party
party_2_missing = party_1.difference(party_2)
party_1_missing = party_2.difference(party_1)

print("Missing from party_2: ",party_2_missing)
print(" ")
print("Missing from party_1: ",party_1_missing)
print("  ")


# Join the two set to create a new one.
didnt_attend_both_parties = party_1_missing.union(party_2_missing)

print("Cumulative list of people who only attended one party: ",didnt_attend_both_parties)