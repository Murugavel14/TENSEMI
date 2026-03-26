def main():
   countt=0
   for i in range(0,1000001):
       count=0
       for j in range(1,int(i+1)):
         if(i%j==0):
            count=count+1
       if(count==2):
         sump=0
         temp=i
         while temp>0:
            a=int(temp%10)
            sump=sump+a;
            temp=int(temp/10)
         if(sump==14):
            countt=countt+1
            print(i)
   print(countt)
if __name__ == "__main__":main()