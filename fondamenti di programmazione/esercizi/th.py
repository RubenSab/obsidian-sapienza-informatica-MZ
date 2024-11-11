l = [1, 2, 4, 5, 6, 'th', 'ruben']
#l = [str(i) for i in l if 'th' not in str(i)]
l = list(filter(lambda x: 'th' not in str(x), l))

print(l)
