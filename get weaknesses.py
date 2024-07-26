from os import system


def get_matchups(*types, get_coverage=False, inverse=False):
    type_matchups = {
        "Normal": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                   "Fighting": 2, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1,
                   "Rock": 1, "Ghost": 0, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},

        "Fire": {"Normal": 1, "Fire": 0.5, "Water": 2, "Electric": 1, "Grass": 0.5, "Ice": 0.5,
                 "Fighting": 1, "Poison": 1, "Ground": 2, "Flying": 1, "Psychic": 1, "Bug": 0.5,
                 "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 0.5, "Fairy": 0.5},

        "Water": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Electric": 2, "Grass": 2, "Ice": 0.5,
                  "Fighting": 1, "Poison": 1, "Ground": 2, "Flying": 1, "Psychic": 1, "Bug": 1,
                  "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 0.5, "Fairy": 1},

        "Electric": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 0.5, "Grass": 1, "Ice": 1,
                     "Fighting": 1, "Poison": 1, "Ground": 2, "Flying": 0.5, "Psychic": 1, "Bug": 1,
                     "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 0.5, "Fairy": 1},

        "Grass": {"Normal": 1, "Fire": 2, "Water": 0.5, "Electric": 0.5, "Grass": 0.5, "Ice": 2,
                  "Fighting": 1, "Poison": 2, "Ground": 0.5, "Flying": 2, "Psychic": 1, "Bug": 2,
                  "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},

        "Ice": {"Normal": 1, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 0.5,
                "Fighting": 2, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1,
                "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 2, "Fairy": 1},

        "Fighting": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                     "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 2, "Psychic": 2, "Bug": 0.5,
                     "Rock": 0.5, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 2},

        "Poison": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                   "Fighting": 0.5, "Poison": 0.5, "Ground": 2, "Flying": 1, "Psychic": 2, "Bug": 0.5,
                   "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 0.5},

        "Ground": {"Normal": 1, "Fire": 1, "Water": 2, "Electric": 0, "Grass": 2, "Ice": 2,
                   "Fighting": 1, "Poison": 0.5, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1,
                   "Rock": 0.5, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},

        "Flying": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 2, "Grass": 0.5, "Ice": 2,
                   "Fighting": 0.5, "Poison": 1, "Ground": 0, "Flying": 1, "Psychic": 1, "Bug": 1,
                   "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},

        "Psychic": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                    "Fighting": 0.5, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 0.5, "Bug": 2,
                    "Rock": 1, "Ghost": 2, "Dragon": 1, "Dark": 2, "Steel": 1, "Fairy": 1},

        "Bug": {"Normal": 1, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 0.5, "Ice": 1,
                "Fighting": 0.5, "Poison": 1, "Ground": 0.5, "Flying": 2, "Psychic": 1, "Bug": 1,
                "Rock": 2, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},

        "Rock": {"Normal": 0.5, "Fire": 0.5, "Water": 2, "Electric": 1, "Grass": 2, "Ice": 1,
                 "Fighting": 2, "Poison": 0.5, "Ground": 2, "Flying": 0.5, "Psychic": 1, "Bug": 1,
                 "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1},

        "Ghost": {"Normal": 0, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                  "Fighting": 0, "Poison": 0.5, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 0.5,
                  "Rock": 1, "Ghost": 2, "Dragon": 1, "Dark": 2, "Steel": 1, "Fairy": 1},

        "Dragon": {"Normal": 1, "Fire": 0.5, "Water": 0.5, "Electric": 0.5, "Grass": 0.5, "Ice": 2,
                   "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1,
                   "Rock": 1, "Ghost": 1, "Dragon": 2, "Dark": 1, "Steel": 1, "Fairy": 2},

        "Dark": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                 "Fighting": 2, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 0, "Bug": 2,
                 "Rock": 1, "Ghost": 0.5, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 2},

        "Steel": {"Normal": 0.5, "Fire": 2, "Water": 1, "Electric": 1, "Grass": 0.5, "Ice": 0.5,
                  "Fighting": 2, "Poison": 0, "Ground": 2, "Flying": 0.5, "Psychic": 0.5, "Bug": 0.5,
                  "Rock": 0.5, "Ghost": 1, "Dragon": 0.5, "Dark": 1, "Steel": 0.5, "Fairy": 0.5},

        "Fairy": {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                  "Fighting": 0.5, "Poison": 2, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 0.5,
                  "Rock": 1, "Ghost": 1, "Dragon": 0, "Dark": 0.5, "Steel": 2, "Fairy": 1}
    }

    matchups = {"Normal": 1, "Fire": 1, "Water": 1, "Electric": 1, "Grass": 1, "Ice": 1,
                "Fighting": 1, "Poison": 1, "Ground": 1, "Flying": 1, "Psychic": 1, "Bug": 1,
                "Rock": 1, "Ghost": 1, "Dragon": 1, "Dark": 1, "Steel": 1, "Fairy": 1}

    for t in types:
        for x in type_matchups:
            if get_coverage:
                if matchups[x] == 1:
                    if inverse:
                        matchups[x] /= type_matchups[x][t]
                    else:
                        matchups[x] *= type_matchups[x][t]
            else:
                if inverse:
                    matchups[x] /= type_matchups[t][x]
                else:
                    matchups[x] *= type_matchups[t][x]

    return matchups


while True:
    types = input("What types do you want to find the weaknesses of?\nPlease separate them by spaces\n").capitalize().split(" ")
    matchups = get_matchups(*types)
    [print(f"{t}: {matchups[t]}") for t in matchups]
    input()
    system("cls")
