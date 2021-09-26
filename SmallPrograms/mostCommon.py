# Completed: Dec 2020
# This program uses a urllib request to settle some debates between which more word choices are more common, based on the number of internet searches.
# For example, "fifth anniversary" is more commonly used than "five-year anniversary".

import urllib.request

def num_of_searches(term):
    temp = term
    # format term to have spaces replaced by "+"
    term = term.replace(" ", "+")

    url = f"https://ca.search.yahoo.com/search?p={term}&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8"
    f = urllib.request.urlopen(url)
    page = f.read().decode("utf-8")

    f.close()
    words = page.replace(">", " ").split()
    for i in range(len(words)-1):
        if words[i+1] == "results</span":
            print(f"The term {temp} has been searched {words[i-1]} times!")
            return words[i-1]

def choose_variant(variants):

    cur_max = [variants[0], int(num_of_searches(variants[0]).replace(",", ""))]
    for i in range(len(variants)):
        if int(num_of_searches(variants[i]).replace(",", "")) > cur_max[1]:
            cur_max[0], cur_max[1] = variants[i], int(num_of_searches(variants[i]).replace(",", ""))

    return cur_max[0]

if __name__ == "__main__":
    options = ["top ranked school uoft", "top ranked school waterloo"]
    print(f"{choose_variant(options)} is the more popular option!")
    print(choose_variant(["five-year anniversary", "fifth anniversary"]))