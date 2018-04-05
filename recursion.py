'''
Anuj Kumar Chaudhary <me@anujkch.com>
# a reach to singularity or golden ratio
# another example for reaching golden ratio is to make fibonacci
# our brain is much more reactive to singular things and prefer singular things
# a person looks more attractive when they wear glasses,
# it makes our face more looks singular so is attractive,
# more we are towards golden ratio better we look,
# so when you wear a brand they make designs to make you more singular
# recursion helps you to reach singularity

### In this demo we are calculating the demo of number 5 which is very common
### to know about factorial, please google, this it is very basic mathematical problem
### for a quick intro
### e.g. if we want a factorial of number 5 then it can be achieved by
### 5*4*3*2*1 which is 120. It can be written as 5!,
### 5! = 120
'''
# recursive demo by simple
def repydemo(num):

    #terminal statement
    if num < 2:
        return 1;

    # print num ## uncomment this for debugging purpose
    result = num*repydemo(num-1)
    return result;

print ("Recursive results {0}".format(repydemo(5)))

#iterative demo
result = 1
for num in range(1,6):
    # print num ## uncomment this for debugging purpose
    result = result*num

print ("Iterative results {0}".format(result))
