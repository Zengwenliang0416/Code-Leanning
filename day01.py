from bs4 import BeautifulSoup


def getRes(n):
  a = []
  sumN =0
  for i in range(n):
    sumN += 2**(i)
    a.append((2**(i)))
  return "{}/{}".format(sumN,a[n-1])
print(getRes(20))
sums=0
for i in range(20):
  sums+=2**i
print('{}/{}'.format(sums,2**19))


