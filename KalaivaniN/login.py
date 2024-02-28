dict={'kalai':2510,'siva':2212,'ramya':4065}
print("LOGIN PAGE")
print("user name : ")
name=input()
print("Password : ")
password=int(input())
uname=list(dict.keys())
pswd=list(dict.values())
succes=0
for i in range(0,3):
    if uname[i]==name and pswd[i]==password:
        print("Login Succesfully")
        succes=1
if succes==0:
    print("wrong")

    
    


