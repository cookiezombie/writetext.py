import feedparser

a = feedparser.parse('https://feeds.npr.org/1001/rss.xml')
b = f"{a.entries[0].title + '. ' + a.entries[0].summary}"
c = f"{a.entries[1].title + '. ' + a.entries[1].summary}"
d = f"{a.entries[2].title + '. ' + a.entries[2].summary}"
e = f"{a.entries[3].title + '. ' + a.entries[3].summary}"
ef = f"{a.entries[4].title + '. ' + a.entries[4].summary}"
g = f"{a.entries[5].title + '. ' + a.entries[5].summary}"
h = f"{a.entries[6].title + '. ' + a.entries[6].summary}"
i = f"{a.entries[7].title + '. ' + a.entries[7].summary}"
j = f"{a.entries[8].title + '. ' + a.entries[8].summary}"
k = f"{a.entries[9].title + '. ' + a.entries[9].summary}"
l = f"{a.entries[10].title + '. ' + a.entries[10].summary}"
m = f"{a.entries[11].title + '. ' + a.entries[11].summary}"
n = f"{a.entries[12].title + '. ' + a.entries[12].summary}"
o = f"{a.entries[13].title + '. ' + a.entries[13].summary}"
p = f"{a.entries[14].title + '. ' + a.entries[14].summary}"
q = feedparser.parse('https://feeds.arstechnica.com/arstechnica/index')
r = f"{q.entries[0].title + '. ' + q.entries[0].summary}"
s = f"{q.entries[1].title + '. ' + q.entries[1].summary}"
t = f"{q.entries[2].title + '. ' + q.entries[2].summary}"
u = f"{q.entries[3].title + '. ' + q.entries[3].summary}"
v = f"{q.entries[4].title + '. ' + q.entries[4].summary}"
w = f"{q.entries[5].title + '. ' + q.entries[5].summary}"
x = f"{q.entries[6].title + '. ' + q.entries[6].summary}"
y = f"{q.entries[7].title + '. ' + q.entries[7].summary}"
z = f"{q.entries[8].title + '. ' + q.entries[8].summary}"
ab = f"{q.entries[9].title + '. ' + q.entries[9].summary}"
ac = f"{q.entries[10].title + '. ' + q.entries[10].summary}"
ad = f"{q.entries[11].title + '. ' + q.entries[11].summary}"
ae = f"{q.entries[12].title + '. ' + q.entries[12].summary}"
af = f"{q.entries[13].title + '. ' + q.entries[13].summary}"
ag = f"{q.entries[14].title + '. ' + q.entries[14].summary}"
ah = feedparser.parse('https://www.wgrz.com/feeds/syndication/rss/news/local')
ai = f"{ah.entries[0].title + '. ' + ah.entries[0].summary}"
aj = f"{ah.entries[1].title + '. ' + ah.entries[1].summary}"
ak = f"{ah.entries[2].title + '. ' + ah.entries[2].summary}"
al = f"{ah.entries[3].title + '. ' + ah.entries[3].summary}"
am = f"{ah.entries[4].title + '. ' + ah.entries[4].summary}"
an = f"{ah.entries[5].title + '. ' + ah.entries[5].summary}"
ao = f"{ah.entries[6].title + '. ' + ah.entries[6].summary}"
ap = f"{ah.entries[7].title + '. ' + ah.entries[7].summary}"
aq = f"{ah.entries[8].title + '. ' + ah.entries[8].summary}"
ar = f"{ah.entries[9].title + '. ' + ah.entries[9].summary}"

news =open("writetext.txt", "w")
newsl = [b,c,d,e,ef,g,h,i,j,k,l,m,n,o,p,r,s,t,u,v,w,x,y,z,ab,ac,ad,ae,af,ag,ai,aj,ak,al,am,an,ao,ap,aq,ar]
for item in newsl:
	news.writelines(item + '\n')
