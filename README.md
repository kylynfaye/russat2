# Russian Satellite Activity Analysis & Anomaly Detection - inspired by Kurtenbach et al. (2025)

## Project Summary
Kurtenbach et al. (2025) applied deep learning techniques for anomaly detection and sequential pattern mining to analyze activity of Russian owned resident space objects (RSO) prior to the Ukraine invasion. This research assesses potential indicators or warnings of aggressive military behavior through statistical analysis of RSO pattern of life/pattern of behavior (PoL/PoB) using publicly available Keplerian elements.

The analysis in `russat2`, includes a replication of their analysis, using a simplified codebase to achieve the same effects. It is the intention of this project to make the work of Kurtenbach more easily reproducible, as their Github was, well, described as "ugly" by Kurtenbach himself via LinkedIn.
- RSO activity monitoring during active combat periods using two-line element (TLE) data post-invasion
- Categorization of space objects by mission set and purpose for enhanced explainability
- Development of generalized profiles for space activity preceding military actions


## 1. How to Run

Open the notebook `main.ipynb` and run through each step you would like to. Pay attention to lines that are commented out with long lines of ###; these will recreate datasets already saved here in the project directory. You will need some data already produced via this notebook if you choose not to re-run the data queries from Space-Track or model training. See 'Data' section for instructions on how to download.

### a. Package Requirements/Environment

If you have conda, run the following in your terminal
`conda env create -f environment.yml`
then run
`conda activate russat2`
to activate the environment with the proper packages.

If you do not have conda, you can pip install `requirements.txt` (which was created via pip freeze of the conda environment), but I cannot guarantee this will run without a hitch.

### b. Data
- `spacetrack_tle_df_merged.parquet`: all TLEs for use in analysis. Acquire at [LINK](https://drive.google.com/drive/folders/1rg60Yy-tRXeviVdjGKVRTMuE8KGDP6w6?usp=sharing). You can also make this dataset yourself in main.ipynb using the chunked TLEs in tles/ folder at that link.
- `MODEL_rfc_persat.pkl`: Model fitted to the training data (all TLEs before 2021-08-23), able to call predict() on this. Acquire at link above.
- `filtered_df.csv`: If you do not want to reproduce the TLEs/column modifications, load in this csv to run the analysis. Acquire at [LINK](https://drive.google.com/file/d/1dvQG1IZNQS94GXFxBxy9-MN4lVNUq1xx/view?usp=sharing)
- `spacetrackcreds.txt`: Need to make a file with this name, formatted spacetrackuser,spacetrackpw. Visit [Space-Track.org](https://space-track.org) to make your account.

### c. Using the Original Author's Data Files (`/Kurtenbach_files`)
- `CIS_satcat.pkl`: SpaceTrack satellite catalog data for CIS-owned objects (~25K objects including debris)
-- You can use this, or you can run the first four cells. To use the `CIS_satcat.pkl` dataset instead of pulling your own from Space-Track, add the following lines of code:
```
#### Load the CIS_satcat.pkl dataset
satcat_path = 'dataout_HPC/CIS_satcat.pkl'

with open(satcat_path, 'rb') as f:
    satcat = pickle.load(f)

#### Convert the satcat data into a DataFrame for easy manipulation
satcat_df = pd.DataFrame(satcat)
```

## 2. Data Sources
- TLEs: Public Keplerian elements from Space-Track
- NASA mission classifications: from paper (Kurtenbach et al. 2025)
- Analysis period: Pre-Ukraine invasion through active combat period

## 3. Contributors
- Original Authors:
  - David Kurtenbach, Kansas State University
  - Megan Manly, Kansas State University
  - Zach Metzinger, Kansas State University
- `russat2` Author:
  - Kylyn Smith, Yale University