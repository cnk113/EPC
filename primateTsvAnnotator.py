with open('filteredAnnotated.vcf') as infile:
    sig = {}
    for line in infile:
        if line[0] != '#':
            line = line.rstrip()
            attr = line.split()
            c = "chr"+attr[0]
            sig[attr[2]] = (c,attr[1],attr[3],attr[4])

with open('PrimateAI_scores_v0.2.tsv') as infile:
    scores = {}
    for line in infile:
        if line[0] != '#':
            line = line.rstrip()
            attr = line.split()
            scores[(attr[0],attr[1],attr[2],attr[3])] = attr[10]

with open('filteredSpliceTsv.txt') as tsv:
    for line in tsv:
        if line[0] != '#':
            line = line.rstrip()
            attr = line.split()
            prim = scores.get(sig.get(attr[0]))
            if prim != None:
                attr.append(prim)
            print('\t'.join(attr))
        else:
            line = line.rstrip()
            attr = line.split()
            attr.append('primateDL_score')
            print('\t'.join(attr))