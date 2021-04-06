if __name__ == '__main__':
    s = input()
    alnm = 'False'
    alp = 'False'
    dig = 'False'
    low = 'False'
    upp = 'False'
    for i in s:
        if i.isalnum():
            alnm = 'True'
        if i.isalpha():
            alp = 'True'
        if i.isdigit():
            dig = 'True'
        if i.islower():
            low = 'True'
        if i.isupper():
            upp = 'True'
print(alnm + '\n'+ alp + '\n'+dig + '\n'+ low+ '\n'+upp)
