def area(b,h):
    return b*h/2
#a=area(9,3)
b=area(6,5)
print(b)

def consec(sec):
    h=sec//3600
    min=(sec-h*3600)//60
    sec=sec-h*3600-min*60
    return h,min,sec
h,min,sec=consec(6000)
print(h,min,sec)
def luckno(name):
    no=len(name)*9
    print(no)
luckno("ken")
luckno("aaron")


def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))