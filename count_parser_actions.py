import os
import numpy as np

DIR = "/Users/jl10240/Dropbox/Study/Cornell/Dissertation/Analysis/model/"
os.chdir(DIR)

lang = "fr"
with open("%s/preprocess/lpp_%s_tree.csv" %(lang,lang)) as f: 
    snts = [i.split(") ") for i in f.read().splitlines()]

# top-down count
td = []
for i in snts:
	for j in i:
		td.append(j.count("("))
np.savetxt("%s/preprocess/lpp_%s_td.csv" %(lang,lang), td, fmt="%d")

# bottom-up count
with open("%s/preprocess/lpp_%s_tree.csv" %(lang,lang)) as f: 
    snts = [i.split(" ") for i in f.read().splitlines()]
bu = []
for i in snts:
	for j in i:
		if ")" in j:
			bu.append(j.count(")"))
np.savetxt("%s/preprocess/lpp_%s_bu.csv" %(lang,lang), bu, fmt="%d")

# left-corner count
lc = []
for i in snts:
	for j in i:
		br1 = j.count("(")
		br2 = j.count(")")+1
		if br1 != br2:
			lc.append(min(br1,br2)+1)
		else:
			lc.append(br1)
np.savetxt("%s/preprocess/lpp_%s_lc.csv" %(lang,lang), lc, fmt="%d")
