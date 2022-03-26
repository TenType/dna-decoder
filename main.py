from data import bases, decoderKey, acids
from inputs import inputs

# Swap pairs
def swap(letter: str):
	value = bases[letter]
	if value == 't':
		return 'u'
	return value

# Split string into array of strings for every 3 letters
def splitThree(str: str):
	n = 3
	arr = [str[i:i+n] for i in range(0, len(str), n)]
	return arr
 
def search(code: str):
	log = []

	# DNA SEQUENCE
	log.append('-'.join(splitThree(code)))

	# RNA SEQUENCE
	swapped = ''
	for i in code:
		swapped += swap(i)

	log.append('-'.join(splitThree(swapped)))

	# HIDDEN MESSAGE
	output = ''
	for i in splitThree(swapped):
		output += decoderKey[i]

	log.append(output)

	# AMINO ACID
	aminoAcids = []
	for i in list(output):
		aminoAcids.append(acids[i])

	log.append('-'.join(aminoAcids))

	print(
		f'''\
DNA Sequence: {log[0]}
RNA Sequence: {log[1]}
Amino Acid: {log[3]}
Hidden Message: {log[2]}
		'''
	)

# Execution
for i, item in enumerate(inputs):
	print(f'=== {i+1} of {len(inputs)} ===')
	search(item)
