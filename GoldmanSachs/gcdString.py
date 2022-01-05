class gcdStr():
    def gcdOfStrings(self, str1: str, str2: str):
        length1 = len(str1)
        length2 = len(str2)
        length = min(length1,length2)
        prefix = ""
        temp = ""
        print(length)
        for i in range(length):
            temp += str1[i]
            print(temp)
            if length1%len(temp) == 0 and length2%len(temp) == 0:
                if temp*(length1//len(temp)) == str1 and temp*(length2//len(temp)) == str2:
                    prefix = temp
        return prefix


if __name__=='__main__':
    str1=input("enter the first string ")
    str2=input("enter the 2 string ")
    sol=gcdStr()
  
    print(sol.gcdOfStrings(str1,str2))

    