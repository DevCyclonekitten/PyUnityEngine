

def MyFunction():
    print("hello")

def CheckValue(value, function):
    if(value>3):
        function()
    

def RunString(string):
    exec(string)


f = open("runthis.txt")
for line in f.read().split("\n"):
    RunString(line)