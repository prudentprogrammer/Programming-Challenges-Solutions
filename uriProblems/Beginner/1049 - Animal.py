# Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1049

species = ['vertebrado', 'invertebrado']
type_animals = [['ave', 'mamifero'], ['inseto', 'anelideo']]
food = [['carnivoro', 'onivoro'], ['onivoro', 'herbivoro'], ['hematofago', 'herbivoro'], ['hematofago', 'onivoro']]
result = ['aguia', 'pomba', 'homem', 'vaca', 'pulga', 'lagarta', 'sanguessuga', 'minhoca']

counter = 0
mapping = {}
for ind1, specie in enumerate(species):
  for ind2, animal_type in enumerate(type_animals[ind1]):
    for ind3, food_type in enumerate(food[2 * ind1 + ind2]):
      mapping['{},{},{}'.format(specie, animal_type, food_type)] = result[counter]
      counter += 1

print(mapping['{},{},{}'.format(input(), input(), input())])