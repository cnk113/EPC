

with open('filtered.vcf') as infile:
    splice = {}   
    sig = {}
    for line in infile:
        if line[0] != '#':
            line = line.rstrip()
            attr = line.split()
            inf = attr[7].split(';')
            splice[attr[2]] = inf[-1].split('=')[-1]
            for i in inf:
                if i[:6] == 'CLNSIG':
                    sig[attr[2]] = i.split('=')[-1]
with open('annotatedVep.txt') as tsv:
    for line in tsv:
        if line[0] != '#':
            line = line.rstrip()
            attr = line.split()
            spl = splice.get(attr[0]).split('|')
            attr.extend(spl[2:6])
            attr.append(sig.get(attr[0]))
            print('\t'.join(attr))
        else:
            line = line.rstrip()
            attr = line.split()
            attr.append('spliceai_DS_AG')
            attr.append('spliceai_DS_AL')
            attr.append('spliceai_DS_DG')
            attr.append('spliceai_DS_DL')
            attr.append('CLINSIG')
            print('\t'.join(attr))
