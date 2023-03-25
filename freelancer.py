class freelancer:
    def dayrate(self, n):
        return round(n*8)
    def monthrate(self,n,m):
        return round(n*8*22*(1-m))
    def daysinbudget(self,n,m,a):
        return round(n/(8*m*(1-a)))

p=freelancer()
print("The day rate =",p.dayrate(89))
print("The month rate =",p.monthrate(89,0.42))
print("The number of working days =",p.daysinbudget(20000,89,0.2002))