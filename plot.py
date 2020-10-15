import matplotlib.pyplot as plt
import re
import numpy as np

f = open('url_domain_count.txt', mode='r')
line2 = f.readlines()
url_domain = set()
count = set()
url_domain_count = {}
for line in line2:
    line = line.rstrip()
    if line == '':
        continue
    url, num = line.rsplit(':', 1)
    url = url.rstrip()
    num = num.strip()
    url_domain.add(url)
    count.add(num)
    if url not in url_domain_count:
        url_domain_count[url] = {int(num.replace(',', ''))}
    else:
        url_domain_count[url].add(int(num.replace(',', '')))

# 棒グラフ出力(未完成)
label = []
value = []
i = 0
fig, ax = plt.subplots()
width = 0.75
for k in url_domain_count:
    d_value = int(re.sub("\\D", "", str(url_domain_count[k]).split()[0]))
    if d_value >= 500:
        label.append(k)
        value.append(d_value)
        ax.barh(i, d_value, width)
        i = i + 1
y = np.arange(len(value))
ax.set_yticks(y)
ax.set_yticklabels(label, minor=False)
plt.title('url domain count')
plt.xlabel('domain count')
plt.ylabel('domain')
for t, v in enumerate(value):
    ax.text(v + 3.0, t - 0.25, str(v),fontweight='bold')
plt.savefig("url_domain_count_barh.png", dpi=300, format='png', bbox_inches='tight')
