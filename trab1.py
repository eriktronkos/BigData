import matplotlib.pyplot as plt
import numpy as np

data = []

arq = open("character-deaths.csv")
arq = arq.read()
lines = arq.split("\r")

for line in lines[1:]:
	data.append(line.split(','))

maleBooks = {}
femaleBooks = {}
for person in data:
	if person[3] != "":
		key = int(person[3])
		if int(person[6]) == 0:
			if key in femaleBooks.keys():
				femaleBooks[key] += 1.0
			else:
				femaleBooks[key] = 1.0
		else:
			if key in maleBooks.keys():
				maleBooks[key] += 1.0
			else:
				maleBooks[key] = 1.0

print maleBooks
print femaleBooks

N = 5

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots(2, sharex=True)
rects1 = ax[0].bar(ind, maleBooks.values(), width, color='r')

rects2 = ax[0].bar(ind + width, femaleBooks.values(), width, color='y')

# add some text for labels, title and axes ticks
ax[0].set_ylabel('Deaths')
ax[0].set_title('Deaths by gender')
ax[0].set_xticks(ind + width)
ax[0].set_xticklabels(('Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5'))

ax[0].legend((rects1[0], rects2[0]), ('Men', 'Women'))


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax[0].text(rect.get_x() + rect.get_width()/2., height - 10,
                '%d' % int(height),
                ha='center', va='bottom')
autolabel(rects1)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax[0].text(rect.get_x() + rect.get_width()/2., 1.05* height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects2)


percMale = {}
percFemale = {}

for book in maleBooks.keys():
	percMale[book] = maleBooks[book]*1.0 / (maleBooks[book] + femaleBooks[book])
	percMale[book] *= 100.0
	percFemale[book] = 100 - percMale[book]

print percMale
print percFemale

N = 5

rects1 = ax[1].bar(ind, percMale.values(), width, color='r')

rects2 = ax[1].bar(ind + width, percFemale.values(), width, color='y')

# add some text for labels, title and axes ticks
ax[1].set_ylabel('% of Deaths')
ax[1].set_title('% of Deaths by gender')
ax[1].set_xticks(ind + width)
ax[1].set_xticklabels(('Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5'))



def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax[1].text(rect.get_x() + rect.get_width()/2., height - 10,
                '%1.1f' % float(height),
                ha='center', va='bottom')
autolabel(rects1)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax[1].text(rect.get_x() + rect.get_width()/2., 1.05* height,
                '%1.1f' % height,
                ha='center', va='bottom')

autolabel(rects2)

plt.show()
