from csv import reader
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pandas as pd
plt.style.use('ggplot')

with open('newSites.csv', 'r') as f:
    data = list(reader(f))

print(data[0])
# show headers

print(data[1])
# show first row

fb_likes = [i[7] for i in data[1::]]

fb_likes = []
for i in data[1::]:
    f = i[7]
    f = int(f)
    fb_likes.append(f)


#creating a facebook likes list

type = []
for i in data[1::]:
    f = i[3]
    type.append(f)
# creating a type list

df = pd.DataFrame({'type': type, 'fb_likes': fb_likes})
print(len(df))

means = df.groupby('type').agg({'fb_likes': 'mean'})

print(len(means))

print(means)

# plt.plot(range(len(fb_likes)), fb_likes)
# plt.ylabel('Number of Facebook likes')
# plt.show()
#
# plt.hist(fb_likes, 50, normed=1, facecolor='green', alpha=0.75)
# plt.xlabel('Number of Facebook likes')
# plt.show()


# df.plot('type', 'mean', kind='bar', color='r')




