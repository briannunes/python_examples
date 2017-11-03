#!/usr/bin/python

fo = open("/etc/passwd", "r")
print ("<accounts>\n")

count=0
for line in fo:
        count+=1
        new=line.rstrip()
        cols=new.split(":", 6)
        print ("    <user name=\"" + cols[0] + "\">")
        print ("        <username>" + cols[0] + "</username>")
        print ("        <password>" + cols[1] + "</password>")
        print ("        <uid>" + cols[2] + "</uid>")
        print ("        <gid>" + cols[3] + "</gid>")
        print ("        <dir>" + cols[4] + "</dir>")
        print ("        <shell>" + cols[5] + "</shell>")
fo.close()

print ("    <TotalAccounts total=\""),count,("\">")
print ("</accounts>")
