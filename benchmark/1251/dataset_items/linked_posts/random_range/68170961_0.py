import random
def randomizer(): 
            chosen_number=[]
            count=0
            user_input = int(input("Enter number for how many rows to randomly select: "))
            numlist=[]
            #length = whatever the highest number you want to choose from
            while 1<=user_input<=length:
                count=count+1
                if count>user_input:
                    break
                else:
                    chosen_number = random.randint(0, length)
                    if line_number in numlist:
                        count=count-1
                        continue
                    if chosen_number not in numlist:
                        numlist.append(chosen_number)
                        #do what you want here
