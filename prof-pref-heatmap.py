from IPython import get_ipython
import pandas as p
from matplotlib import pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('pylab', 'inline')

data = p.read_csv('./speeddating.csv', encoding='ISO-8859-1')
print("sup")
data['zipcode'].unique()[0:5]
data['zipcode'] = data['zipcode'].apply(lambda v: str(v).replace(',', '')).apply(lambda v: v.zfill(5))

# Create set to contain pairs of participants where participant with iid
# has 'match' == 1 and participant with pid has 'dec_o' == 1 in the same row.
mut_matches = set()

# Dictionary to store field codes for iids and pids
field_codes = {}

# Dictionary for looking up the name associated with a field codes
fields = {
	1: "Law",
	2: "Math",
	3: "Social Science, Psychology",
	4: "Medical Science, Pharmaceuticals, Bio-tech",
	5: "Engineering",
	6: "English, Creative Writing, Journalism",
	7: "History, Religion, Philosophy",
	8: "Business, Economics, Finance",
	9: "Education, Academia",
	10: "Biological Sciences, Chemistry, Physics",
	11: "Social Work",
	12: "Undergrad, Undecided",
	13: "Political Science, International Affairs",
	14: "Film",
	15: "Fine Arts, Arts Administration",
	16: "Languages",
	17: "Architecture",
	18: "Other"
}

#print([x, y, z in data[['iid', 'pid', 'match']] if data['match'] == 1 and data['dec_o'] == 1])
for index, row in data.iterrows():
	if (row['match'] == 1 and row['dec_o'] == 1) and ('iid' in row and 'pid' in row and 'field_cd' in row):

		# Cast ids as ints
		row['iid'] = int(row['iid'])
		row['pid'] = int(row['pid'])

		# Sort tuples before adding them to the set. This is to ensure that a tuple
		# (a, b) and a tuple (b, a) are treated as equivalent.
		if row['iid'] < row['pid']:
			mut_matches.add((row['iid'], row['pid']))
		else:
			mut_matches.add((row['pid'], row['iid']))

		# Store field code if it is not already stored
		if row['iid'] not in field_codes:
			field_codes[row['iid']] = row['field_cd']
		if row['pid'] not in field_codes:
			field_codes[row['pid']] = row['field_cd']


xid, yid, xfield, yfield = []

# Populate lists to create a new dataframe
for row in mut_matches:
	xid.append(row[0])
	yid.append(row[1])
	xfield.append(fields[row[0]])
	xfield.append(fields[row[1]])

plot_data = pd.DataFrame({'xid': xid, 'yid': yid, 'xfield': xfield, 'yfield': yfield})
plot_data.plot(kind='bar', stacked=True)

#temp = [x for x in
print("after")

# Create heatmap showing number of matches between each combination of professions
#hm = sns.heatmap()
