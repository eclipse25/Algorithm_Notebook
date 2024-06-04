import sys

n, m = map(int, sys.stdin.readline().split())
pokemons = {}
for i in range(1, n + 1):
    pokemon = sys.stdin.readline().rstrip()
    pokemons[i] = pokemon
    pokemons[pokemon] = i

for _ in range(m):
    problem = sys.stdin.readline().rstrip()
    if problem.isdigit():
        print(pokemons[int(problem)])
    else:
        print(pokemons[problem])