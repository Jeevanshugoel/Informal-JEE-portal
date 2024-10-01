import matplotlib.pyplot as plt
l1=[]
l2=[]
for i in range (3):
    x=int(input("enter x"))
    y=int(input("enter y"))

    l1.append(x)
    l2.append(y)
print(l1,l2)
plt.plot(l1,l2,"green")
plt.xlabel("Year ")
plt.ylabel("no. of Registrations")
plt.title("YEARLY DATA")
plt.show()
