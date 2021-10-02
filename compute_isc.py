import sys
import os
import nibabel as nib
import numpy as np
from scipy.stats import pearsonr

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
"subj22","subj23","subj24","subj25","subj26","subj27","subj28","subj29","subj30"]

lang = sys.argv[1]
subj_id = int(sys.argv[2])

if lang == "en":
	subjects = subjects_en
elif lang == "cn":
	subjects = subjects_cn
elif lang == "fr":
	subjects = subjects_fr

mask = nib.load("lpp_%s%d_groupmask_thrs80.nii" %(lang,len(subjects))).get_fdata()   	
mask = mask.flatten()

subj = subjects[subj_id-1]
subjects.remove(subj)

os.chdir("/scratch/jl10240/lpp/Data/lpp_%s" %(lang))
    
correlations = []
for i in range(1,10):
	subj_data = nib.load("%s/func/section%d.nii" %(subj,i)).get_fdata()
	scan_num = subj_data.shape[3]
	subj_data = subj_data.reshape(-1,scan_num)
	group_mean = np.zeros_like(subj_data)
	for iother, other in enumerate(subjects):
		other_data = nib.load("%s/func/section%d.nii" %(other,i)).get_fdata()
		other_data = other_data.reshape(-1,scan_num)
		group_mean = (group_mean * iother + other_data)/(iother+1)
	corr = np.zeros_like(mask)
	for j in range(len(subj_data)):
		print(i,j)
		if mask[j]>0 and subj_data[j,:].any()>0 and group_mean[j,:].any()>0:
			corr[j] = pearsonr(subj_data[j,:], group_mean[j,:])[0]
	correlations.append(corr)

correlations = np.array(correlations)
correlations_mean = np.mean(correlations, axis=0)

np.save("/scratch/jl10240/lpp/Analysis/data_quality/isc/%s_subj%d_isc" %(lang,subj_id), correlations)
np.save("/scratch/jl10240/lpp/Analysis/data_quality/isc/%s_subj%d_isc_mean" %(lang,subj_id), correlations_mean)
