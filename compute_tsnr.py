import sys
import os
from nipype.algorithms.confounds import TSNR

subjects_en = ["subj57","subj58","subj59","subj61","subj62","subj63","subj64","subj65","subj67",
"subj68","subj69","subj70","subj72","subj73","subj74","subj75","subj76","subj77","subj78",
"subj79","subj81","subj82","subj83","subj84","subj86","subj87","subj88","subj89","subj91",
"subj92","subj93","subj94","subj95","subj96","subj97","subj98","subj99","subj100","subj101",
"subj103","subj104","subj105","subj106","subj108","subj109","subj110","subj113","subj114",
"subj115"]

subjects_cn = ["subj1","subj2","subj3","subj4","subj5","subj6","subj7","subj8","subj9","subj10",
"subj11","subj13","subj14","subj15","subj16","subj17","subj18","subj19","subj20","subj21",
"subj22","subj23","subj24","subj25","subj26","subj27","subj28","subj29","subj30","subj31",
"subj32","subj33","subj34","subj36","subj37"]

subjects_fr = ["subj1","subj2","subj3","subj4","subj5","subj6","subj7","subj8","subj9","subj10",
"subj11","subj12","subj13","subj14","subj15","subj16","subj17","subj18","subj19","subj20",
"subj22","subj23","subj24","subj25","subj26","subj29","subj30"]

lang = sys.argv[1]
subj_id = int(sys.argv[2])

if lang == "en":
	subjects = subjects_en
elif lang == "cn":
	subjects = subjects_cn
elif lang == "fr":
	subjects = subjects_fr

subj = subjects[subj_id-1]	

tsnr = TSNR()

os.chdir("/scratch/jl10240/lpp/Data/lpp_%s/%s/func/" %(lang,subj))
if not os.path.exists("tsnr"):
	os.makedirs("tsnr")
for i in range(1,10):
	f = "section%d.nii.gz" %i if lang != "fr" else "section%d.nii" %i
	tsnr.inputs.in_file = f
	tsnr.inputs.tsnr_file = "tsnr/section%d_tsnr.nii.gz" %i
	tsnr.inputs.mean_file = "tsnr/section%d_mean.nii.gz" %i
	tsnr.inputs.stddev_file = "tsnr/section%d_stddev.nii.gz" %i
	tsnr.inputs.detrended_file = "tsnr/section%d_detrended.nii.gz" %i
	tsnr.inputs.regress_poly = 4
	tsnr.run()

os.chdir("/scratch/jl10240/lpp/Data/lpp_%s_raw/%s/func/tsnr" %(lang,subj)) 
for i in range(1,10):
	f = "run%d_echo2_align.nii.gz" %i
	tsnr.inputs.in_file = f
	tsnr.inputs.tsnr_file = "run%d_echo2_align_tsnr.nii.gz" %i
	tsnr.inputs.mean_file = "run%d_echo2_align_mean.nii.gz" %i
	tsnr.inputs.stddev_file = "run%d_echo2_align_stddev.nii.gz" %i
	tsnr.inputs.detrended_file = "run%d_echo2_align_detrended.nii.gz" %i
	tsnr.inputs.regress_poly = 4
	tsnr.run()