# Scripts for the data paper "Le Petit Prince: A multilingual fMRI corpus using ecological stimuli".

1. **compute_fd.py:** 
- Compute the tsnr for the raw and preprocessed fMRI data.

2. **compute_tsnr.py:** 
- Compute the temporal signal-to-noise ratio (tSNR) for the raw and preprocessed fMRI data.

3. **compute_isc.py:**     
- Compute inter-subject correlation (ISC) for each voxel's timeseries across subjects in each language group.

4. **get_f0_intensity.m:**    
- Get the f0 and root-mean-square (RMS) intensity for every 10 ms of the audios using the Matlab toolbox Voicebox.

5. **get_word_frequency.py:**    
- Get word frequency using the Google Books (Version 20120701) unigram frequency counts.

6. **get_word_embeddings.py:**    
- Extract GloVe and BERT embeddings using SpaCy.

7. **parse_syntax.sh:**    
- Get part-of-speech tagging, constituent tree structure and dependency relations for every sentence using the Stanford parser. 

8. **count_parser_actions.py:**    
- Syntactic node counts for each word in the audiobooks based on bottom-up, top-down and left-corner parsing strategies as applied to the Stanford-derived constituency trees described above.
