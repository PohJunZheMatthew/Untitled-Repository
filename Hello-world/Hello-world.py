#Here are some ways to say hello world in python
#defult print() function
print("Hello world")
#Use system standard output
import sys
sys.stdout.write("Hello world")
#Write it into a file
with open("Hello-world.txt","w+") as file:
  file.write("Hello world")
