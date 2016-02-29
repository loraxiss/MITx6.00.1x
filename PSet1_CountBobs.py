bob_count = 0
search_start = 0
bob_index = 0
while (bob_index != -1):
    bob_index = s.find('bob',search_start)
    if bob_index != -1:
        bob_count +=1
        search_start = bob_index+1
        
print('Number of times bob occurs is: ' + str(bob_count))
