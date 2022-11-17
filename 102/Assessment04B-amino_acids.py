#   Grace Luka
#  ​ CSCI 102 – Section B
#   Assessment 04B
#   References: 
#   Time: 60 minutes

print('Input the chemical elements of the amino acid:')
c = int(input('CARBON> '))
h = int(input('HYDROGEN> '))
n = int(input('NITROGEN> '))
o = int(input('OXYGEN> '))
s = int(input('SULFUR> '))

alanine = f'3C--7H--1N--2O--0S'
arginine = f'6C--14H--4N--2O--0S'
asparagine = f'4C--8H--2N--3O--0S'
cysteine = f'3C--7H--1N--2O--1S'
histidine = f'6C--9H--3N--2O--0S'
glutamine = f'5C--10H--2N--3O--0S'


if s != 0:
    print(f'The amino acid for {cysteine} is Cysteine')
    print(f'OUTPUT {cysteine} \nOUTPUT Cysteine')

else:
    if c == 3:
        print(f'The amino acid for {alanine} is Alanine')
        print(f'OUTPUT {alanine} \nOUTPUT Alanine')

    elif c == 6:
        if h == 14:
            print(f'The amino acid for {arginine} is Arginine')
            print(f'OUTPUT {arginine} \nOUTPUT Arginine')
            
        elif h == 9:
            print(f'The amino acid for {histidine} is Histidine')
            print(f'OUTPUT {histidine} \nOUTPUT Histidine')
            
    elif c == 4:
        print(f'The amino acid for {asparagine} is Asparagine')
        print(f'OUTPUT {asparagine} \nOUTPUT Asparagine')
        
    elif c == 5:
        print(f'The amino acid for {glutamine} is Glutamine')
        print(f'OUTPUT {glutamine} \nOUTPUT Glutamine')
