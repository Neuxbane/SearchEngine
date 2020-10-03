def WordsList(text):
	Words = text.replace('\n','. ').split(' ')
	n = []
	for x in Words:
		if not x in n:
			n.append(x.replace('.','').replace('(','').replace(')','').replace('/',''))
	Words = n
	del n
	return Words
def WordsCorrection(Words,inp):
	Result = []
	for argument in inp.split(' '):
		score = []
		for a in Words:
			Score = 0
			for b in a:
				if b.lower() in argument.lower():
					Score += 1
				else:
					Score -= 5
			score.append(Score)
		BestScore = 0
		for x in score:
			if x>BestScore:
				BestScore = x
		Result.append(Words[score.index(BestScore)])
	return ' '.join(Result)
def listsentences(path):
	try:
		Data = open(path,'r').read()
	except Exception as e:
		open(path,'a')
		Data = 'No Data'
	a = []
	b = ''
	ie = True
	for x in range(len(Data)-(Data[-1] == ".")):
		if Data[x] == '[':
			ie = False
		if ie:
			b += Data[x]
		if Data[x] == ']':
			ie = True
		if "." == Data[x]:
			if (Data[x+2] == Data[x+2].upper() or Data[x+1] == Data[x+1].upper()) and (not Data[x+2] in '1234567890' or not Data[x+1] in '1234567890'):
				a.append(b[(b[0] == ' '):].replace('\n',' ').replace('  ',' '))
				b = ''
	a.append(b[(b[0] == ' '):].replace('\n',' ').replace('  ',' '))
	return a
def searchresult(arg,data):
	a = data
	n = []
	for c in a:
		score = 0
		text = []
		for x in c.split(' '):
			if (x.lower() in [u.lower() for u in arg.split(' ')]) and not x.lower() in text:
				score += 5
			else:
				score -= 3
			text.append(x.lower())
		if arg.lower().replace(' ','') in c.lower().replace(' ',''):
			score += 20
		n.append(score/(len(c)+0.1))
	best = -999
	num = 0
	for x in range(len(n)):
		if n[x] > best:
			best = n[x]
			num = x
	text = []
	b = 1
	while 100>len('\n\n'.join(a[num:num+b])):
		b += 1
	for x in '\n\n'.join(a[num:num+b]).split(' '):
		if True in [x.lower() in u.lower() or u.lower() in x.lower() for u in arg.split(' ')]:
			text.append(f"*{x}")
		else:
			text.append(x)
	return ' '.join(text)
while 1:
	inp=input(">")
	print()
	correction = WordsCorrection(WordsList(open('a.txt','r').read()),inp)
	#if inp.lower() != correction.lower():
		#print()
		#print('Did you mean:',correction)
		#print()
	print('Jawab:\n',searchresult(inp,listsentences("a.txt")))