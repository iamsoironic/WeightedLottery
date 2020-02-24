import random
import math

dictionary1 = {
  "winning": 1,
  "losing": 10
}

dictionary2 = {
  "red": 1,
  "green": 2,
  "blue": 3
} 



def weighted_lottery(weights):
    odds = list(weights.values())
    result = list(weights.keys())
    weighted_random = []
    x = 0
    for _ in weights:
        weighted_random += [result[x]] * odds[x]
        x += 1
    return random.choice(weighted_random)

print(weighted_lottery(dictionary1))
