# start , end ---> multiplication-table[start:end]



def multiplication_table (start , end):
    for x in range(start, end+1):

        for y in range(From,to+1):

            print(f"{x} X {y} = {x*y}")

        print('--------------')


start = int(input('Enter Start: '))  # cast
end = int(input('Enter End: '))
From = int(input('From what: '))  
to = int(input('To: '))

multiplication_table (start , end)
