import numpy as np
from collections import Counter

def trucksim(n, d):
    return np.random.choice(d.keys(), n, p = d.values())

def get_percentages(input_list):
    d = {}
    for i in input_list:
        d[i] = input_list[i] / float(len(input_list))



d = {"a": .2, "b": .3, "c": .5}
print trucksim(10, d)


keyname = {"<10", "10-15", "15-20", "20-25", "25-30", "30-35", "35-37", "37+"}

def truck1CI(keyname, simlist, n, alpha):

    sample_pct = []
    sim_len = len(simlist)
    c = Counter(simlist)
    d = {}

    for i in c:
        d[i] = c[i]/float(sim_len)

    for i in range(n):
        sample_pct.append(len([each for each in trucksim(sim_len, d) if each==keyname])/(sim_len*1.0))

    mean = np.mean(sample_pct)
    lower_bound = np.percentile(sample_pct, (alpha/2)*100)
    upper_bound = np.percentile(sample_pct, (alpha/2)*100)
    standard_deviation = np.std(sample_pct)

    return mean, lower_bound, upper_bound, standard_deviation


simlist = (['< 10'] * 452) + (['10-15'] * 1212) + (['15-20'] * 625) + (['20-25'] * 653) \
   + (['25-30'] * 713) + (['30-35'] * 858) + (['35-37'] * 368) + (['37+'] * 108)

print truck1CI('30-35', simlist, 100, 0.1)

d = {'< 10': .08, '10-15': .27, '15-20': .1, '20-25': .11, '25-30': .15, '30-35': .2,
    '35-37': .07, '37+': .02}

simlist = []
for key in d:
   simlist = simlist + ([key] * int(4989 * d[key]))


