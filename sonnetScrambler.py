from random import randint
import json

# Make an array of rhyming couplets by:
# 1. Splitting the document into sonnets
# 2. Splitting each sonnet into lines (by "[p]" character)
# 3. Picking couplets according to strict sonnet structure (which is what Shakespeare used)
# Return the final array of couplets structured as:
# [[rhyme1a,rhyme1b],[rhyme2a, rhyme2b]...[rhyme1078a, rhyme 1078b]]

def make_rhyme_pairs_array(file):
    sonnet_file = open(file, 'r') #file = sonnets.txt or test.txt
    all_sonnets = sonnet_file.read()
    sonnet_file.close()
    sonnet_array = all_sonnets.split("\"\n\"")
    for i in range(len(sonnet_array)):
        sonnet_array[i]=sonnet_array[i].split("[p]")
    rhyme_pairs = []
    for sonnet in range(len(sonnet_array)):
        for line in range(len(sonnet_array[sonnet])):
            if line < 12 and line%4 < 2:
                rhyme_pairs.append([sonnet_array[sonnet][line],sonnet_array[sonnet][line+2]])
            elif line == 12:
                rhyme_pairs.append([sonnet_array[sonnet][line],sonnet_array[sonnet][line+1]])
    return rhyme_pairs

# Pick seven couplets at random and incorporate them into the sonnet structure.
def write_sonnet():
    rhyme_couplets = make_rhyme_pairs_array('sonnets.txt')
    sonnet = ""
    sonnet_rhymes = []
    sonnet_sources = []
    for i in range(7):
        n = randint(0,len(rhyme_couplets))
        sonnet_rhymes.append(rhyme_couplets[n])
        sonnet_sources.append(int(n/7))
    for i in [0, 2, 4]:
        sonnet += sonnet_rhymes[i][0] + sonnet_rhymes[i+1][0] + sonnet_rhymes[i][1] + sonnet_rhymes[i+1][1]
    sonnet += "  " + sonnet_rhymes[6][0] + "  " + sonnet_rhymes[6][1]
    sonnet_sources = list(set(sonnet_sources))
    sources = "\nSonnet lines from"
    for i in range(len(sonnet_sources)):
        if i < len(sonnet_sources)-1:
            sources += " %s," %sonnet_sources[i]
        else:
            sources += " & %s." %sonnet_sources[i]
    f = open('sonnet_output.txt', 'w')
    f.write(sonnet + sources)
    f.close()

write_sonnet()
