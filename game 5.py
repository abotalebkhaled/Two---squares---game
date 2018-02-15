print(" How To Play !!")
print(" You will entre 2 inputs , these 2 inputs should be next or above each other ")
print(" If you dont want to input in any list q or w , enter 0 in the input ")
q=["1 ","2 ","3 ","4 "]
w=["5 ","6 ","7 ","8 "]
e=["9","10","11","12 "]
t=["13","14","15","16"]
print(q)
print(w)
print(e)
print(t)
p=1
counter=0
i=0
for i in range (8):
        if p==3:
            p=1
        print("Player: ",p)
        p=p+1
        y=int(input("Enter place 1 in q: "))
        k=int(input("Enter place 1 in w: "))
        h=int(input("Enter place 1 in e: "))
        u=int(input("Enter place 1 in t: "))
        if y<=4 and y!=0:
            q.insert(y-1,"x")
            q.pop(y)
        elif k!=0 and k>4 and k<=8:
            w.insert(k-5,"x")
            w.pop(k-4)
        elif h!=0 and h>8 and h<=12:
            e.insert(h-9,"x")
            e.pop(h-8)
        elif u!=0 and u>12 and u<=16:
            t.insert(u-13,"x")
            t.pop(u-12)
        elif y>4:
            print("insert number less than or equal 4")
            y=int(input("Enter place 1 in q: "))
            q.insert(y-1,"x")
            q.pop(y)
        elif 4<=k>8:
            print("insert number bigger than or equal 4 and less than or equal 8")
            k=int(input("Enter place 1 in w: "))
            w.insert(k-5,"x")
            w.pop(k-4)
        elif 8<=h>12:
            print("insert number bigger than or equal 8 and less than or equal 12")
            h=int(input("Enter place 1 in e: "))
            e.insert(h-9,"x")
            e.pop(h-8)
        elif 12<=u>16:
            print("insert number less than or equal 12 and less than or equal 16")
            u=int(input("Enter place 1 in t: "))
            t.insert(u-13,"x")
            t.pop(u-12)
        else:
            print("try again")
        print(q)
        print(w)
        print(e)
        print(t)
        m=int(input("Enter place 2 in q: "))
        j=int(input("Enter place 2 in w: "))
        g=int(input("Emter place 2 in e: "))
        v=int(input("Enter place 2 in t: "))
        if m!=0 and m<=4:
            q.insert(m-1,"x")
            q.pop(m)
        elif j!=0 and j>4 and j<=8 and(j-y==4 or j-k==1 or k-j==1 or h-j==4):
            w.insert(j-5,"x")
            w.pop(j-4)
        elif g!=0 and g>8 and g<=12 and (g-k==4 or g-h==1 or h-g==1 or u-g==4):
            e.insert(g-9,"x")
            e.pop(g-8)
        elif v!=0 and v>12 and v<=16 and (v-h==4 or v-u==1 or u-v==1) :
            t.insert(v-13,"x")
            t.pop(v-12)
        elif m>4:
            print("insert number less than or equal 4 ")
            m=int(input("Enter place 2 in q: "))
            q.insert(m-1,"x")
            q.pop(m)
        elif 4<=j>8:
            print("insert number less than or equal 8 and bigger than 4 , also that number must be under or above the last input ")
            j=int(input("Enter place 2 in w: "))
            if j!=0 and j>4 and j<=8 and(j-y==4 or j-k==1 or k-j==1 or h-j==4):
                w.insert(j-5,"x")
                w.pop(j-4)
        elif 8<=g>12:
            print("insert number less than or equal 12 and bigger than 8, also the number must be under or above the last input ")
            g=int(input("Enter place 2 in e: "))
            if g!=0 and g>8 and g<=12 and (g-k==4 or g-h==1 or h-g==1 or u-g==4):
                e.insert(g-9,"x")
                e.pop(g-8)
        elif 12<=v>16:
            print("insert number less than or equal 16 and bigger than 12 , the number must be under of above the last input ")
            v=int(input("Enter place 2 in t: "))
            if v!=0 and v>12 and v<=16 and (v-h==4 or v-u==1 or u-v==1):
                t.insert(v-13,"x")
                t.pop(v-12)
        else:
            print("Try Again")
        print(q)
        print(w)
        print(e)
        print(t)
        counter=counter+1
        print("Counter=: ",counter)
        if counter==7:
            print("count x in q: ",q.count("x"))
            print("count x in w: ",w.count("x"))
            print("count x in e: ",e.count("x"))
            print("count x in t: ",t.count("x"))
            z=int(input("Enter the last input 1  : "))
            c=int(input("Enter the last input 2  : "))
            if z-c==1 or z-c==4 or c-z==1 or c-z==4:
                print("Draw")
            else:
                print("Player",p-1,"wins")
        if counter==7:
            break;
