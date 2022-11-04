from operator import truediv
import pandas
import random

df = pandas.read_csv('vocabulary.csv', error_bad_lines=False)
print('\n\n')

#length of the table to ask questions later:
amountOfLines = df.shape[0]
#list of languages
languages = (df.keys())

#Get a random word and ask for the translation in a given language


score = 0
mistakes = 0

while score < 20:
    correct = False
    sameWordMistake = 0
    randomLanguage = random.randint(0,len(languages)-1)
    randomWord = random.randint(0,amountOfLines-1)

    question = (df[languages[randomLanguage]][randomWord])

    answerLanguage = random.randint(0,len(languages)-1)

    print(f'{question} -> {languages[answerLanguage]}?')
    rightAnswer = (df[languages[answerLanguage]][randomWord])
    while correct == False:
        answer = input(': ')
        if answer == rightAnswer:
            score += 1
            print(f'score: {score}')
            correct = True
        else:
            mistakes += 1
            sameWordMistake += 1
        if sameWordMistake == 5:
            correct = True
            print(rightAnswer)

print(mistakes)






def main():
    return 1


main()