from google import search

#b contains list of all columns and rows
b = np.genfromtxt(r'Jobs.csv', delimiter=',', names=True, dtype=None)

l = []

for query in b['JOBS']:
	for url in search(str(query)+' Careers Job Apply', tld='com', lang='en', stop=1):
		l.append(url)
		break;

csv = 'Jobs,Link'+"\n"

for job,link in zip(b['JOBS'], l):
	csv+=str(job)+','+str(link)+'\n'

# choose a filename to save to
print("Choose a filename or press enter to save to `default.csv`:")
try: input = raw_input
except NameError: pass
filename = input().strip()
if filename == '':
	filename = "default.csv"

# save the CSV
try:
    with open(filename, "w+") as outfile:
        outfile.write(csv)
except IOError:
    print("Oops.  Unable to write file to ",filename)
