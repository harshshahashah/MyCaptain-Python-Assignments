# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

for n in range(1,6):
    i = 1
    while(n-i > 0):
        print(" ", end = " ")
        i = i + 1
    j = 1
    while(j <= 6-n):
        print(" * ", end = " ")
        j = j + 1
    
    while(n-i > 0):
        print(" ", end  = " ")
    i = i + 1
    print()

for n in range(2,6):
    i = 0
    while(i < 5-n):
        print(" ", end = " ")
        i = i + 1
    j = 1
    while(j <= n):
        print(" * ", end = " ")
        j = j + 1
    while(i < 5-n):
        print(" ", end = " ")
        i = i + 1
    print()
    
