def main():
    count=0
    for  i in range(1000,10000):
      n=str(i)
      dec=1
      for j in range(0,len(n)-1):
        if(n[j]>n[j+1]):
            dec=0
            break
      if dec==1:  
        count=count+1
        print(i,"non decreasing num")
    print("total",count)
if __name__ == "__main__":main()