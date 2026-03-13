def calculate_love_score(name1, name2):
    combined_names = (name1+name2).upper()
    ptrue = "TRUE"
    plove = "LOVE"
    scoretrue = 0
    scorelove = 0
    
    for char in combined_names:
        if char != " ":
            scoretrue += ptrue.count(char)


    for char in combined_names:
        if char != " ":
            scorelove += plove.count(char)
            
    finalscore = (scoretrue*10)+scorelove
    print(finalscore)
    
            
            
    print(combined_names)
calculate_love_score("Angela Yu", "Jack Bauer")