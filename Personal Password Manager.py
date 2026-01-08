User_Names=[]
User_Platform={}
Account_Type=set()

UserName=input("Enter User Name:")
Platform=input("Enter User Platform:")
Type=input("Enter Account Type (Personal/Work):")

User_Names.append(UserName)
PlatformAndAccount=(Platform,Type)
User_Platform[UserName]=Platform
Account_Type.add(Type)

print("\n    |User Account Data|       ")
print("User Name (List):",User_Names)
print("Platform And Account Type (Tuple):",PlatformAndAccount )
print("Username To Platform (Dictionary):",User_Platform)
print("Account Type (Set):",Account_Type)
print("       Thankyou      ")