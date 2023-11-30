def total_marks(math,english,kiswahili,science,sos):
    total=(math+english+kiswahili+science+sos)
    return total
maths=float(input("enter your math score: "))
eng=float(input("enter your english score: "))
kiswa=float(input("enter your kiswahili score: "))
scie=float(input("enter your science score: "))
social=float(input("enter your social score: "))
score=total_marks(maths,eng,kiswa,scie,social)

def avarage_marks(math,english,kiswahili,science,sos):
    avarages=(math+english+kiswahili+science+sos)/5
    return avarages
avarage=avarage_marks(maths,eng,kiswa,scie,social)
print(avarage)

def total_grade(avarage):
   if(avarage>70):
     score="A"
   elif(avarage>60)and(avarage<79):
     score="B"
   elif(avarage>49)and(avarage<59):
     score="c"
   elif(avarage>40)and(avarage<49):
     score="d" 
   else:
      score="e"
   return(score)
grades=total_grade(avarage)
print(grades)