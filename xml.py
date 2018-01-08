import os

inpt = 'D:\\xml'
otpt = inpt + '\\out'

if not os.path.exists(otpt):
    os.makedirs(otpt)

for file in os.listdir(inpt):
    filename, file_extension = os.path.splitext(file)
    if file_extension == '.xml':
        with open(os.path.join(inpt, file), 'r') as cf:  # current file
            with open(os.path.join(otpt, file), 'w') as nf:  # new file
                linia = cf.readline().split()
                if linia[0] == "<PERMISSIVEWINDOW" and 'name' in linia[1]:
                    linia.pop(1)
                    nowa = ' '.join(linia)
                    nf.write(nowa + '\n')
                    for linia in cf:
                        nf.write(linia)
