import sys, re

f = open(sys.argv[1]+'.txt', 'r')

s = [re.sub(r'[^a-z0-9\s\n]','',line.lower()) for line in f]
s = ' '.join(s)

s = s.split()
s = [a for a in s if len(a)>=4]

print(' '.join(s))

f_out = open(sys.argv[1]+'_clean.txt', 'w')
f_out.write(' '.join(s))
f_out.close()
