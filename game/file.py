str="linux is my life \n how about you \n fuck"
my_file=open('my_file.txt','w')
my_file.write(str)
my_file.close()

my_file=open('my_file.txt','a')
str2='end'
my_file.write(str2)
my_file.close()

my_file=open('my_file.txt','r')
str3=my_file.read()
print(str3)
my_file.close()

my_file=open('my_file.txt','r')
str4=my_file.readline()
print(str4)
my_file.close()

my_file=open('my_file.txt','r')
str5=my_file.readlines()
print(str5)
my_file.close()