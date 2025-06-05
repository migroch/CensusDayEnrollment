import pandas as pd
import glob

rename_dic = {'CountyName':'COUNTY', 'DistrictName':'DISTRICT', 'SchoolName':'SCHOOL', 'TOTAL_ENR':'TOTAL_ENR', 
              'GR_KN':'KDGN', 'GR_01':'GR_1', 'GR_02':'GR_2', 'GR_03':'GR_3', 'GR_04':'GR_4',
              'GR_05':'GR_5', 'GR_06':'GR_6', 'GR_07':'GR_7', 'GR_08':'GR_8', 'GR_09':'GR_9'}

# Concatenate all enrollment files into a single DataFrame
dfs = []
for file in glob.glob("data/enrollment_*.txt"):
    df = pd.read_csv(file, sep="\t", header=None)
    df['FileName'] = file.split('/')[-1] 
    dfs.append(df)

for file in glob.glob("data/cdenroll_*.txt"):
    df = pd.read_csv(file, sep="\t", header=None)
    df['FileName'] = file.split('/')[-1]
    df.rename(columns=rename_dic, inplace=True) 
    dfs.append(df)

enrollment = pd.concat(dfs, ignore_index=True)
    

