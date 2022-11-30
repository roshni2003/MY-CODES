from pprint import pprint


a={'data':{
    'jan':{'mon':3,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'feb':{'mon':5,'tues':5,'wed':4,'thurs':7,'fri':2,'sat':3,'sun':7},
    'march':{'mon':7,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'april':{'mon':8,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'may':{'mon':3,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'june':{'mon':2,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'july':{'mon':5,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'aug':{'mon':3,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'sep':{'mon':8,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'oct':{'mon':7,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'nov':{'mon':7,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
    'dec':{'mon':5,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4}}
}
sum = 0 
Mon_l = []
GreateThan_f = []
for i in a :
    for k in a[i].keys():
        for k1 in a[i][k]:
            sum+=a[i][k][k1]
            if k1 == 'mon':
                Mon_l.append(a[i][k][k1])
            elif  a[i][k][k1] > 4:
                GreateThan_f.append(a[i][k][k1])
print("sum of the all value : - ")
print(sum)
print("\n1. Exit all mon values")
for i in Mon_l:
    print('mon :-',i)
print("\ngreater than four : - ")
for i in GreateThan_f:
    print(i)
