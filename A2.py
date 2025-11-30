#check the frequency

dict={
    "Welcome":10,"to":3,"my":6,"class":10
}
print("Dictionary: "+str(dict))
x=int(input("Enter the number to check the frequency: "))
res=0
for key in dict:
    if dict[key]==x:
        res= res + 1

print("The frequency of ",x,":",str(res))
