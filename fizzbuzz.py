d = x = [None,None,'fizz',None,'buzz','fizz',None,None,'fizz','buzz',None,'fizz',None,None,'fizzbuzz']
fizzbuzz = ((x[(i-1) % 15] or i) for i in range(1,100))

# newline seperated

if __name__=="__main__":
    for i in fizzbuzz:
        print i
