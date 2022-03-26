from data import decoderKey, acids
from inputs import inputs

# Swap pairs
def swap(letter):
	if letter == 'g': return 'c'
	if letter == 'c': return 'g'
	if letter == 't': return 'a'
	if letter == 'a': return 'u'
	print(f'Error: {letter} is missing from swap function')

# Split string into array of strings for every 3 letters
def splitThree(str):
	n = 3
	arr = [str[i:i+n] for i in range(0, len(str), n)]
	return arr
 
def search(code):
	# DNA SEQUENCE
	dna = '-'.join(splitThree(code))
	print(f'DNA Sequence: {dna}')

	# RNA SEQUENCE
	swapped = ''
	for i in code:
		swapped += swap(i)

	rna = '-'.join(splitThree(swapped))
	print(f'RNA Sequence: {rna}')

	# HIDDEN MESSAGE
	output = ''
	for i in splitThree(swapped):
		if not decoderKey.get(i): print(f'Error: {i} is missing from map')
		output += decoderKey.get(i)

	print(f'Hidden Message: {output}')

	# AMINO ACID
	aminoAcids = []
	for i in list(output):
		if not acids.get(i): print(f'Error: {i} is missing from acids')
		aminoAcids.append(acids.get(i))

	aminoAcids = '-'.join(aminoAcids)
	print(f'Amino Acid: {aminoAcids}')

# Execution
for i, item in enumerate(inputs):
	print(f'=== {i+1} of {len(inputs)} ===')
	search(item)
	print('\n')
