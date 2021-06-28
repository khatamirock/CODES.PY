
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

LINES = ['-', ':', '--']  # Line style for plots.



str='''Mr Sherlock Holmes, who was usually very late in the mornings, save
upon those not infrequent occasions when he was up all night, was seated
at the breakfast table. I stood upon the hearth-rug and picked up the
stick which our visito Had left behind him the night before. It was a
fine, thick piec  masdmnasd ADMAS DASJNEWE FS DFWER WERW ERFWFSDRFWRW ER'''

tokens = nltk.word_tokenize(str)

print(tokens)
splt_tok=dict()
splt_tok[1] = ([token.lower() for token in tokens
                                    if token.isalpha()])
len_wrd=[len(wrd) for wrd in splt_tok[1]] ## that is exactly of the first author and upto 300 len()...

# print(len_wrd)

plt.figure(1)

plt.ion()

saa=dict()
saa[1]=nltk.FreqDist(len_wrd)
print(saa)
saa[1].plot(11,
 linestyle='-',
 label='ARTHUR',
 title='ARTHUR')

plt.show()

stp=stopwords.words('english')


stpLs=[wor for wor in splt_tok[1] if wor in stp]

print(stpLs)

nw=dict()
nw[1]=nltk.FreqDist(stpLs)
print(nw)
nw[1].plot(6,linestyle='-', label='ARTHUR',title='STOP_WRDS')


