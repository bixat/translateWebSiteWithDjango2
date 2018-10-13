from mydb import intodb
ar = open('arabe.txt', encoding='utf8')
for w in ar:
    q = w.find(',')
    if q == -1:
        q += 1
    print('eng:{}, ar:{}'.format(w[:q], w[q + 1:len(w)]))
    intodb(w[:q], w[q + 1:len(w)])

