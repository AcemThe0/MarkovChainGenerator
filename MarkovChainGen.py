from random import randint


def choose(list):
    return list[randint(0, len(list)-1)]


def markovChainGenText(length, data):
    output = []
    choice_list = []
    current_word = choose(data)
    output.append(current_word)
    i = 0

    while i < length:

        for word in range(0, len(data), 1):

            if data[word] == current_word:

                try:
                    choice_list.append(data[word+1])
                except:
                    choice_list.append(choose(data))
                    
        output.append(choose(choice_list))

        choice_list = []
        current_word = output[-1]
        i+=1
    print(' '.join(output))

try:
    with open("dataset.txt", "r") as data_file:
        dataset = data_file.read().replace("\n", " ")#.lower()
except:
    dataset = "0 1 0 1"

try:
    markovChainGenText(int(input("Sentence length: ")), dataset.split())
except:
    pass
