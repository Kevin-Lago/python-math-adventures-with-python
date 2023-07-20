import random

target = "I never go back on my word, because that is my Ninja way."
characters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.',?!"


def makeList() -> list:
    charList = []

    for i in range(len(target)):
        charList.append(random.choice(characters))
    return charList


def score(myList):
    matches = 0

    for i in range(len(target)):
        if myList[i] == target[i]:
            matches += 1

    return matches


def mutate(myList):
    newList = list(myList)
    new_letter = random.choice(characters)
    index = random.randint(0, len(target) - 1)
    newList[index] = new_letter
    return newList


if __name__ == '__main__':
    random.seed()
    bestList = makeList()
    bestScore = score(bestList)

    guesses = 0

    while True:
        guess = mutate(bestList)
        guessScore = score(guess)
        guesses += 1

        if guessScore <= bestScore:
            continue

        print(''.join(guess), guessScore, guesses)
        if guessScore == len(target):
            break

        bestList = list(guess)
        bestScore = guessScore
    print(len(target))
    print(makeList())
