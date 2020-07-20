import string
import sys
sys.setrecursionlimit(10**6)

class work:
    def get_digits(self,No,D):                     #RECIEVING END
        if No==None:
            return None
        No=str(No)
        if D==4:
            No=No.zfill(4)
        elif D==5:
            No=No.zfill(5)
        else:
            No=No.zfill(6)
        k=self.get_value(No,D)
        if k==None:
            return k
        else:
            k=self.zero(k,D)
        return k

    def get_value(self,No,D):            #MAIN FUNCTION RESPONSIBLE FOR CALCULATION
        No = int(No)
        Temp=0
        count=0
        lisT=list(range(0, 102))
        while True:
            if count>=100:
                return None
            if No == Temp:
                break
            elif No<0:
                break
            else:

                Largest =self.get_dsc(No,D)

                Smallest =self.get_asc(No)

                new_No=self.sub(Largest, Smallest)

                new_No=self.zero(new_No,D)

                new_No = int(new_No)
                lisT[count]=No
                seT = set()
                for e in lisT:
                    if e in seT:
                        return e
                    else:
                        seT.add(e)
                Temp = No
                No=new_No
                count=count+1

        new_No=str(new_No)
        return new_No
    def zero(self,No,D):

        No = str(No)
        if D == 4:
            No = No.zfill(4)
        elif D == 5:
            No = No.zfill(5)
        else:
            No = No.zfill(6)
        return No
    def get_asc(self,No):

        smaller = [int(x) for x in str(No)]

        smaller.sort()

        s = [str(i) for i in smaller]
        Val2 = int("".join(s))
        return Val2

    def get_dsc(self,No,D):

        greater = [int(x) for x in str(No)]

        greater.sort(reverse=True)

        s = [str(i) for i in greater]
        Val1 = int("".join(s))
        Val1=self.tailingzero(Val1, D)

        return Val1

    def sub(self,Largest,Smallest):

        new_No=Largest-Smallest

        return new_No

    def tailingzero(self,No, D):

        No=str(No)
        r = D - len(No)
        No = No.ljust(r + len(No), '0')

        No=int(No)

        return No


