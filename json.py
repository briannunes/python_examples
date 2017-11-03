!/usr/bin/python

fo = open("/etc/passwd", "r")
print ("{\"Accounts\": {\n")

count=0
for line in fo:
        count+=1
        new=line.rstrip()
        cols=new.split(":", 6)
        print ("    \"User\": {");
        print ("        \"username\": \"" + cols[0] + "\",")
        print ("        \"password\": \"" + cols[1] + "\",")
        print ("        \"uid\": " + cols[2] + ",")
        print ("        \"gid\": " + cols[3] + ",")
        print ("        \"dir\": \"" + cols[4] + "\",")
        print ("        \"shell\": \"" + cols[5] + "\",")
        print ("      },")
fo.close()

print ("    \"TotalAccounts\":"), count
print "}}"
