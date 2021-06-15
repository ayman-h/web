import random
import turtle

pokeMovesFile = open('pokemon_moves.csv') # open pokemon_moves.csv
next(pokeMovesFile) # skip first line 

allMoves = {}
for line in pokeMovesFile: # Iterate through each line
    currLine = line.rstrip().split(',')
    allMoves[currLine[0]] = {
        "type": currLine[1], 
        "damage": int(currLine[2]), 
        "accuracy": int(currLine[3])
    }

allPokemonFile = open('pokemon_names.csv') # open pokemon_names.csv
next(allPokemonFile)

allPokemon = {}
for line in allPokemonFile: 
    currLine = line.rstrip().split(',')
    allPokemon[currLine[0]] = {
        "type": currLine[1], 
        "move_1": currLine[2], 
        "move_2": currLine[3], 
        "move_3": currLine[4], 
        "move_4": currLine[5]
    }

def attack(attackingPokmon, foePokemon, foePokemonHP, isPlayer): # attack function (works for both player and foe)
    attackingPokmonMoves = []
    for i in range(1, 5): 
        attackingPokmonMoves.append(allPokemon[attackingPokmon]["move_" + str(i)])

    chooseMovePrompt = "What will " + attackingPokmon + " do?\n"
    for move in attackingPokmonMoves: 
        chooseMovePrompt += "\t- " + move + "\n"  

    if isPlayer: 
        choosenMove = input(chooseMovePrompt)      
        if choosenMove not in attackingPokmonMoves: 
            print(attackingPokmon + " does not know this move, choose again!")
            choosenMove = input(chooseMovePrompt)  
        print(attackingPokmon + " used " + choosenMove + "!")
    else: 
        choosenMove = random.choice(attackingPokmonMoves)
        print("Foe " + attackingPokmon + " used " + choosenMove + "!")

    if random.randrange(101) > allMoves[choosenMove]["accuracy"]: 
        print(attackingPokmon + "'s attack missed!") 
        return foePokemonHP
    # damage multiplyer according to move type and victim pokemon type
    if (allMoves[choosenMove]["type"] == "Fire") and (allPokemon[foePokemon]["type"] == "Grass"): 
        print("It was super effective!") 
        foePokemonHP -= allMoves[choosenMove]["damage"] * 1.1
    elif (allMoves[choosenMove]["type"] == "Electric") and (allPokemon[foePokemon]["type"] == "Water"): 
        print("It was super effective!")  
        foePokemonHP -= allMoves[choosenMove]["damage"] * 1.1
    elif (allMoves[choosenMove]["type"] == "Water") and (allPokemon[foePokemon]["type"] == "Fire"): 
        print("It was super effective!")  
        foePokemonHP -= allMoves[choosenMove]["damage"] * 1.1
    elif (allMoves[choosenMove]["type"] == "Grass") and (allPokemon[foePokemon]["type"] == "Rock"): 
        print("It was super effective!")  
        foePokemonHP -= allMoves[choosenMove]["damage"] * 1.1
    elif (allMoves[choosenMove]["type"] == "Rock") and (allPokemon[foePokemon]["type"] == "Electric"): 
        print("It was super effective!")  
        foePokemonHP -= allMoves[choosenMove]["damage"] * 1.1
    else: 
        foePokemonHP -= allMoves[choosenMove]["damage"] 

    return round(foePokemonHP)

def main():
    continueGame = True    
    while continueGame: 

        # Announce which enemy pokemon we have run into 
        foePokemon = random.choice(list(allPokemon.keys()))
        print("Wild " + foePokemon + " appeared")

        # Choose pokemon 
        choosePokemonPrompt = "Which Pokémon will you bring out? Select from: \n"
        for name in allPokemon.keys(): 
            choosePokemonPrompt += "\t- " + name + "\n" 

        playerPokemon = input(choosePokemonPrompt)
        
        # Check if pokemon selected is available
        while playerPokemon not in allPokemon.keys(): 
            print("The Pokemon you have selected is not available, choose again!")
            playerPokemon = input(choosePokemonPrompt)

        # Announce selected pokemon
        print("You have selected " + playerPokemon + "!")

        foeHP = playerHP = 60 
        playerTurn = True 
        # HP tracker
        while (foeHP > 0) and (playerHP > 0): 
            if playerTurn: 
                foeHP = attack(playerPokemon, foePokemon, foeHP, playerTurn) 
                playerTurn = False

                if foeHP > 0: 
                    print("The wild " + foePokemon + " has " + str(foeHP) + " HP remaining!")
            else:  
                playerHP = attack(foePokemon, playerPokemon, playerHP, playerTurn)
                playerTurn = True 

                if playerHP > 0: 
                    print(playerPokemon + " has " + str(playerHP) + " HP remaining!")

        # Enemy pokemon has fainted 
        if foeHP <= 0: 
            print("The wild " + foePokemon + " has fainted!")
            tr = turtle.Turtle()
            wn = turtle.Screen()
            wn.addshape('gif images/' + playerPokemon + '.gif')
            tr.shape('gif images/' + playerPokemon + '.gif')
        else: # Current pokemon has fainted 
            print("Your " + playerPokemon + " has fainted!")  
            tr = turtle.Turtle()
            wn = turtle.Screen()
            wn.addshape('gif images/' + foePokemon + '.gif')
            tr.shape('gif images/' + foePokemon + '.gif')
        # Prompt user if they want to continue the game
        continueGameAnswer = input("\nDo you want to continue the game?\n \t- Yes\n \t- No\n")

        if continueGameAnswer == 'Yes': 
            continueGame = True 
            wn.reset()
            wn.clear() # resets turte window
        else: 
            continueGame = False

if __name__ == "__main__":
    main()

