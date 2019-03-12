with open('clinvar_20170905.vcf') as infile:
    sig = {}
    for line in infile:
        if line[0] != '#':
            line = line.rstrip()
            attr = line.split()
            sig[attr[2]] = True

with open('clinvar_20190211.vcf') as tsv:
    for line in tsv:
        if line[0] != '#':
            line = line.rstrip()
            attr = line.split()
            if sig.get(attr[2]) == True :
                print(line.rstrip())
        else:
            print(line.rstrip())
