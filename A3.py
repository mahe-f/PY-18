#get the country code
code={
    "India":"0091",
    "USA":"001",
    "Pakistan":"+92",
    "Germany": "+49",
    "Australia": "+61",
    "UK":"+44",
    "Japan":"0081"
}
print("Country code finder")
country=input("Enter country name: ")
print("Country code is: ",code.get(country,"Not found"))