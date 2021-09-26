# Completed: December 2020

# Goal: Use semantic similarity to find synonyms given a list of options.
# Semantic similarity refers to how often two words appear in similar contexts.
# We can get a good sense of two words' similarity from examining a large database of sentences,
# like a book. Two novel's, Swann's Way and War and Peace, are in placed in this folder.
# A list of test problems is found in problemSet.txt

import math
import pprint

def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    parameter: vec, a dictionary
    '''
    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    '''
    Returns the dot product between vec1 and vec2
    '''
    dot = 0
    for key in vec1:
        if vec2.get(key, None) != None:
            dot += vec1[key] * vec2[key]
    sum_squares1 = 0
    for key in vec1:
        sum_squares1 += vec1[key] ** 2
    sum_squares2 = 0
    for key in vec2:
        sum_squares2 += vec2[key] ** 2

    return dot / math.sqrt(sum_squares1 * sum_squares2)

def build_semantic_descriptors(sentences):
    dict = {}
    for sentence in sentences:
        for word in sentence:
            dict[word] = {}

    for sentence in sentences:
        for word in dict: # every distinct word in dict
            if word in sentence: # if this word isn't in the sentence, don't add anything to its dictionary
                for other_words in dict.fromkeys(sentence):
                    if other_words != word and other_words not in dict[word]:
                        dict[word][other_words] = 1
                    elif other_words != word and other_words in dict[word]:
                        dict[word][other_words] += 1

    return dict

def build_semantic_descriptors_from_files(filenames):
    f = ""
    for file in filenames:
        f += open(file, "r", encoding="latin1").read()
        f += " "
    f = f.lower()

    for char in [",", ":", ";"]:
        f = f.replace(char, "")
    f = f.replace("--"," ").replace("-"," ").replace("\n", " ")
    list_of_sent = f.replace("!", ".").replace("?", ".").split(". ")
    if f[-1][-1] in [",",".",":"]:
        f[-1] = f[-1][:-1]
    words_of_sent = []

    for i in range(len(list_of_sent)):
        words_of_sent.append(list(filter(None,list_of_sent[i].split(" "))))

    return build_semantic_descriptors(words_of_sent)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    # looks at the other words that appear in the context and compares frequency
    largest = -1
    closest_choice = choices[0]
    d = semantic_descriptors
    for i in range(len(choices)):
        if word in d.keys() and choices[i] in d.keys():
            if similarity_fn(d[word], d[choices[i]]) > largest:
                largest = similarity_fn(d[word], d[choices[i]])
                closest_choice = choices[i]
    return closest_choice

def run_similarity_test(testFile, semantic_descriptors, similarity_fn):
    '''
    Returns a score of accuracy prediction out of 100.
    Each line of the test file testFile has format: <Word in Question> <Correct Answer> <Option 1> <Option 2>
    Where <Correct Answer> is the synonym of <Word in Question>, and it matches one of the options

    The score is calculated based on the algorithm's prediction accuracy, as a percentage.
    '''
    f = open(testFile, "r", encoding="latin1").read().split("\n")
    number_correct = 0
    total_number = 0
    while '' in f:
        f.remove('')
    for line in f:
        line = line.split(" ") #each line is a list of format "question", "option", "option", "option"
        word = line[0]
        correct = line[1]
        choices = line[2:]
        total_number += 1
        if most_similar_word(word, choices, semantic_descriptors, similarity_fn) == correct:
            number_correct += 1
    if total_number != 0:
        return 100*number_correct/total_number
    else:
        return 0

if __name__ == "__main__":
    # some tests
    cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6})
    (cosine_similarity({"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1, "unattractive": 1}, {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1}))
    L = [["i", "am", "a", "sick", "man"],
        ["i", "am", "a", "spiteful", "man"]]
    case = (build_semantic_descriptors(L))
    pprint.pprint(case)
    pprint.pprint(build_semantic_descriptors([["i", "am", "a", "sick", "man"],["i", "believe", "my", "liver", "is", "diseased"],["i", "am", "a", "spiteful", "man"],["i", "am", "an", "unattractive", "man"]]))
    
    # Large books will take a while to compute
    g = build_semantic_descriptors_from_files(["C:\\Users\\qingy\\OneDrive\\Documents\\Year_1\\Sem_1\\ESC180 - Computer\\Codes\\Projects\\Projects_GitHub\\Python-Projects\\Synonyms\\SwannsWay.txt"])
    test = "C:\\Users\\qingy\\OneDrive\\Documents\\Year_1\\Sem_1\\ESC180 - Computer\\Codes\\Projects\\Projects_GitHub\\Python-Projects\\Synonyms\\problemSet.txt"
    
    print(f"Accuracy: {run_similarity_test(test, case, cosine_similarity)}%")

[["i", "am", "a", "sick", "man"],
["i", "am", "a", "spiteful", "man"],
["i", "am", "an", "unattractive", "man"],
["i", "believe", "my", "liver", "is", "diseased"],
["however", "i", "know", "nothing", "at", "all", "about", "my",
"disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]