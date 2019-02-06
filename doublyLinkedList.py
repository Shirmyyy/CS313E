class poly(object):
    def __init__(self,coeff,expo,next=None):
        self.coeff=coeff
        self.expo=expo
        self.next=next

class poly_list(object):
    def __init__(self):
        self.first=None
    def insert(self,expo,coeff):
        new_link=poly(coeff,expo)
        current=self.first
        if current is None:
            self.first=new_link
            return
        while current.next!=None:
            current=current.next
        current.next=new_link


    def plus(self):
        current=self.first
        li=poly_list()
        coeff1=0
        if self.first==None:
            return 0
        current_expo=0
        while current!=None:
            if current.expo>current_expo:
                current_expo=current.expo
            current=current.next
        print(current_expo)

        current_expo_min=self.first.expo
        while current!=None:
            if current.expo_min<current_expo:
                current_expo_min=current.expo
            current=current.next


        while current_expo>=current_expo_min:
            while current!=None:
                if current.expo==current_expo:
                    coeff1+=current.coeff
                current=current.next
            print(coeff1)
            li.insert(current_expo,coeff1)
            current_expo-=1
        return li

    def __str__(self):
        current=self.first
        strng=''
        while current!=None:
            strng+=str(current.coeff)+'  '+str(current.expo)+'\n'
            current=current.next

        return strng
def main():
    lst=poly_list()
    lst.insert(2,3)
    lst.insert(3,2)
    print(lst)

    print(lst.plus())
main()
