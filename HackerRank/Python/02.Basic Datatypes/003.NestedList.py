'''
Question : Given the names and grades for each student in a class of N students, store them in a nested list and 
           print the name(s) of any student(s) having the second lowest grade.
           Note: If there are multiple students with the second lowest grade, order their names alphabetically and 
           print each name on a new line.
           
Link : https://www.hackerrank.com/challenges/nested-list/problem           
'''

marksheet=[]
scorelist=[]
if __name__ == '__main__':
        for i in range(int(input())):
                name = input()
                score = float(input())
                marksheet+=[[name,score]]
                scorelist+=[score]
        b=sorted(list(set(scorelist)))[1] 

        for a,c in sorted(marksheet):
             if c==b:
                    print(a)
