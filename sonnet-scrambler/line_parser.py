from pprint import pprint
from matplotlib import pyplot
import math

def line_parser(file):
    f = open(file)
    all_lines = f.read()
    f.close()
    return all_lines

def line_length_distribution(file):
    all_lines = line_parser(file)
    # Clean up data
    all_lines = all_lines.replace("\n","")
    all_lines = all_lines.replace("-","")
    all_lines = all_lines.replace(";","")
    all_lines = all_lines.replace("[p]"," ")
    all_lines = all_lines.lower()
    all_lines = all_lines.split("\"")
    all_lines = filter(None, all_lines)
    line_array = []
    for i in range(len(all_lines)):
        n_start = 0
        sub_array = []
        for n in range(len(all_lines[i])):
            if all_lines[i][n] == " ":
                sub_array.append(all_lines[i][n_start:n])
                n_start = n+1
            elif all_lines[i][n] in ".?!:,":
                sub_array.append(all_lines[i][n_start:n])
                sub_array.append(all_lines[i][n])
                n_start = n+2
        for word in sub_array:
            if word in [""," "]:
                sub_array.remove(word)
        line_array.append(sub_array)
    # Find each
    # line_length_dist = {}
    # for i in range(len(all_lines)):
    #     all_lines[i] = all_lines[i].split()
    #     if len(all_lines[i]) in line_length_dist:
    #         line_length_dist[len(all_lines[i])] += 1
    #     else:
    #         line_length_dist[len(all_lines[i])] = 1
    # line_length_dist = [(k,v) for k,v in line_length_dist.items()]
    # line_length_dist_norm = [(t[0],float(t[1])/len(all_lines)) for t in line_length_dist]
    # log_dist = [(t[0],math.log(t[1])) for t in line_length_dist_norm]
    # pyplot.scatter(*zip(*log_dist))
    # pyplot.title('Line length distribution for comedies')
    # pyplot.xlabel('Line length (words)')
    # pyplot.ylabel('log(probability)')
    # pyplot.show()
    return line_array

pprint(line_length_distribution('source_texts/tragedy_lines.csv'))
