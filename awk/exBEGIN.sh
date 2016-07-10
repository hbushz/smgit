#! /bin/awk -f

BEGIN {
x=3/9
x+=5
x=int(x)
message="Hello, world!"
arr[1]="Trim"
arr["a"]=12
arr[3]=13
print x, arr["a"],arr[1],arr[2],arr[3]
print "Hello, World!"
}
