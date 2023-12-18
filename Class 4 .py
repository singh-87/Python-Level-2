"""#n1=[1,2,3,4,5] n2=[4,5,6,7,8] add each item from n1 with each item of n2 so the output=[5,7,9,11,13]
n1=[1,2,3,4,5]
n2=[4,5,6,7,8]
output = list(map(lambda a,b: a+b,n1,n2))
print(output)"""
#Convert from string to integer using .split(without condition)
"""n1=["1","2","3","4","5"]
user = input("Enter your numbers separated by comma:").split(",")
print(user)
output = [ int(i) for i in user]
print(output)"""
#With condition
"""names=["karan", "karvin" , "poovin", "saran", "tharun" , "saranya" , "angela" ,  "sanjith"]
output = [ i for i in names if i[-1]=='n' and len(i)==5]
print(output)
"""
"""a=[1,2,3,4,5,6,7,8,9,10,11,12]
output = [i for i in a if i>10]
filtera = list(filter(lambda a: a>10,a))
print(output)
print(filtera)
numbers= [6,10,15,19,25,29,31,40,50]
output = [i for i in numbers if i%5==0]
filtera = list(filter(lambda a: a%5==0,numbers))
print(filtera)
print(output)
n = ['1','2','3','4','5']
output = [int(i) for i in n]
output2 = [i**2 for i in output]
print(output)
print(output2)
students=["a.partha","b.parv","c.sarath","d.sanjay","e.lim"]
output = [i.title() for i in students]
print(output)
names=['Karan.A', 'Karvin.B', 'Poovin.C', 'Saran.D', 'Tharun.E']
output = [i[0:-2] for i in names]
print(output)"""

Names=["sanjay","Rahul","Karan","Wasim","Ramesh","Ajay","Sartaj","Priya"]
weight=[50,50,80,76,60,44,50,70]
height=[1.5,1.0,1.7,1.4,1.1,1.5,1.8,1.7]
output = list(map(lambda a,b: round(a/b**2,2) ,weight,height))
print(output)
BMI= {}
for i in range(0,8):
    BMI[Names[i]]= output[i]
print(BMI)
"""sport = {'hockey':12,'cricket':11}
sport['hockey']=13
for i in sport:
    print(sport[i])
print(sport.values())
print(sport)"""
sport = {'hockey':12,'cricket':11}
sport['football']=10
print(sport)