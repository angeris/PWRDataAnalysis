import numpy as np
from sklearn.decomposition import PCA

CE_file = open('CE_clean.txt', 'r')
SB_file = open('SB_clean.txt', 'r')
BH_file = open('BH_clean.txt', 'r')
TE_file = open('TE_clean.txt', 'r')

dictionary = {}

CE_str = CE_file.readline()
SB_str = SB_file.readline()
BH_str = BH_file.readline()
TE_str = TE_file.readline()

unique_words = set()

for i in (CE_str+' '+SB_str+' '+BH_str+' '+TE_str).split():
    unique_words.add(i)

t = 0

rev_dictionary = {}

for i in unique_words:
    dictionary[i] = t
    rev_dictionary[t] = i
    t+=1

CE_vec = np.zeros(len(dictionary))
SB_vec = np.zeros(len(dictionary))
BH_vec = np.zeros(len(dictionary))
TE_vec = np.zeros(len(dictionary))

for i in CE_str.split():
    CE_vec[dictionary[i]] += 1

for i in SB_str.split():
    SB_vec[dictionary[i]] += 1

for i in BH_str.split():
    BH_vec[dictionary[i]] += 1

for i in TE_str.split():
    TE_vec[dictionary[i]] += 1

# normalize all vectors
M = np.array([CE_vec, SB_vec, BH_vec, TE_vec]).T

M /= np.sum(M, 0)

pca = PCA(n_components=4)
pca.fit(M)

print(pca.explained_variance_ratio_)

M = pca.fit_transform(M)

s = M[:,0]
top = sorted(s)[-10]

for i in range(len(M[:,0])):
    if M[i,0] > top:
        print(rev_dictionary[i])

print('---------')

s = M[:,-1]
top = sorted(s)[-10]

for i in range(len(M[:,0])):
    if M[i,-1] > top:
        print(rev_dictionary[i])
