with open('day3.input') as fp: print (sum( [ (1 if l[(3*i) % (len(l)-1) ] == '#' else 0) for i,l in enumerate(fp)] ))
