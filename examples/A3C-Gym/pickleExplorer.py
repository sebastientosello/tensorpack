import pickle

with open('demofile.pickle', 'rb') as handle:
	while True:
		try:
			b = pickle.load(handle)
			print(len(b))
		except EOFError:
			break
