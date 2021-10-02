import os
import numpy as np

subjects_en = ["subj57","subj58","subj59","subj61","subj62","subj63","subj64","subj65","subj67",
"subj68","subj69","subj70","subj72","subj73","subj74","subj75","subj76","subj77","subj78",
"subj79","subj81","subj82","subj83","subj84","subj86","subj87","subj88","subj89","subj91",
"subj92","subj93","subj94","subj95","subj96","subj97","subj98","subj99","subj100","subj101",
"subj103","subj104","subj105","subj106","subj108","subj109","subj110","subj113","subj114","subj115"]

subjects_cn = ["subj1","subj2","subj3","subj4","subj5","subj6","subj7","subj8","subj9","subj10",
"subj11","subj13","subj14","subj15","subj16","subj17","subj18","subj19","subj20","subj21",
"subj22","subj23","subj24","subj25","subj26","subj27","subj28","subj29","subj30","subj31",
"subj32","subj33","subj34","subj36","subj37"]

subjects_fr = ["subj1","subj2","subj3","subj4","subj5","subj6","subj7","subj8","subj9","subj10",
"subj11","subj12","subj13","subj14","subj15","subj16","subj17","subj18","subj19","subj20",
"subj22","subj23","subj24","subj25","subj26","subj28","subj29","subj30"]

lang = "fr"

if lang == "en":
	subjects = subjects_en
elif lang == "cn":
	subjects = subjects_cn
elif lang == "fr":
	subjects = subjects_fr

os.chdir("/scratch/jl10240/lpp/Data/lpp_%s_raw" %(lang))	   

fd_mean = []
fd_percent = []
for subj in subjects:
	motion = np.genfromtxt("%s/func/motion/%s_%s_motion.csv" %(subj,lang,subj), delimiter=" ")
	fd = np.sum(abs(motion[1:,:3]-motion[:-1,:3]), axis=1) + 50 * np.pi/180 * np.sum(abs(motion[1:,3:]-motion[:-1,3:]), axis=1)
	fd_mean.append(fd.mean())
	fd_percent.append(len(np.where(fd>0.2)[0])/len(fd))

np.save("/scratch/jl10240/lpp/Analysis/data_quality/fd/%s_fd_mean" %lang, fd_mean)
np.save("/scratch/jl10240/lpp/Analysis/data_quality/fd/%s_fd_percent" %lang, fd_percent)

