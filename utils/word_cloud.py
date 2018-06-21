import numpy as np 
import pandas as pd 
import matplotlib as mpl  
import matplotlib.pyplot as plt 


from subprocess import check_output 
from wordcloud import WordCloud, STOPWORDS

mpl.rcParams['font.size'] = 12
mpl.rcParams['savefig.dpi'] = 100
mpl.rcParams['figure.subplot.bottom'] = .1

stopwords = set(STOPWORDS)
data = open("input.txt").read()

WordCloud = WordCloud(
	background_color = 'white',
	stopwords  = stopwords,
	max_words = 200,
	max_font_size = 40,
	random_state = 42,
	).generate(str[data])

print(wordcloud)
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
fig.savefig("Figures/word_cloud.png", dpi = 900)