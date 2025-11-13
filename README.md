# Russian Satellite Activity Analysis & Anomaly Detection - Version 2

## Project Summary
We apply deep learning techniques for anomaly detection and sequential pattern mining to analyze activity of Russian owned resident space objects (RSO) prior to the Ukraine invasion. This research assesses potential indicators or warnings of aggressive military behavior through statistical analysis of RSO pattern of life/pattern of behavior (PoL/PoB) using publicly available Keplerian elements.

Our analysis includes:
- RSO activity monitoring during active combat periods using two-line element (TLE) data post-invasion
- Categorization of space objects by mission set and purpose for enhanced explainability
- Development of generalized profiles for space activity preceding military actions

## How to Run

Open the notebook `main.ipynb` and run through each step you would like to. Pay attention to lines that are commented out with long lines of ###; these will recreate datasets already saved here in the project directory.

## Package Requirements/Environment

If you have conda, run the following in your terminal
`conda env create -f environment.yml`
then run
`conda activate russat2`
to activate the environment with the proper packages.

If you do not have conda, you can pip install requirements.txt (which was created via pip freeze of the conda environment), but I cannot guarantee this will run without a hitch.

## Repository Structure

### Original Author's Data Files (`/Kurtenbach_files`)
- `CIS_satcat.pkl`: SpaceTrack satellite catalog data for CIS-owned objects (~25K objects including debris)
-- You can use this, or you can run the first four cells. To use the `CIS_satcat.pkl` dataset instead of pulling your own from Space-Track, add the following lines of code within the """ to the beginning of the first cell in Step 3:
"""
# Load the CIS_satcat.pkl dataset
satcat_path = 'dataout_HPC/CIS_satcat.pkl'

with open(satcat_path, 'rb') as f:
    satcat = pickle.load(f)

# Convert the satcat data into a DataFrame for easy manipulation
satcat_df = pd.DataFrame(satcat)
"""
### Model(s)
- `MODEL_rfc_persat.pkl`: Combined data including:
  - TLE data
  - Satellite catalogue/characteristics information
  - NASA mission type classification data
  - Fitted model to the training data (TLEs before 2021-08-23), able to call predict()

### Misc.
- `filtered_df.csv`: If you do not want to reproduce the TLEs/column modifications, load in this csv to run the analysis
- `parse_tle.py`: Helpful function for parsing the TLE strings downloaded from Space-Track
- `spacetrackcreds.txt`: Need to make a file with this name, formatted spacetrackuser,spacetrackpw,udluser,udlpw

## Data Sources
- TLEs: Public Keplerian elements from Space-Track
- NASA mission classifications: from paper (Kurtenbach et al. 2025)
- Analysis period: Pre-Ukraine invasion through active combat period

## Contributors
- David Kurtenbach, Kansas State University
- Megan Manly, Kansas State University
- Zach Metzinger, Kansas State University
- Kylyn Smith, Yale University