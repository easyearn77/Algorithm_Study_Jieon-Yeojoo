import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemon_dictionary = {}

for i in range(1, n + 1):
    pokemon = input().rstrip()
    pokemon_dictionary[i] = pokemon
    pokemon_dictionary[pokemon] = i

for j in range(m):
    question = input().rstrip()
    if question.isdigit():
        print(pokemon_dictionary[int(question)])
    else:
        print(pokemon_dictionary[question])