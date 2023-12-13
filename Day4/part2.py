
def main():

    total = 0

    with open("input.txt") as f:
        
        #list representing the number of copies we've won of the upcoming scratch cards
        num_copies = [1]

        for line in f.readlines():
            line = line.split(': ')[1] #removes the first part of the line
            line = line.replace("  ", " ").strip() #removes double spaces and newline

            winning, scratch = line.split(" | ")
            winning = winning.split(" ")
            scratch = scratch.split(" ")

            copies_won = 0

            for num in scratch:
                if num in winning:
                    copies_won += 1
            
            #if there aren't enough values to index into: add some zeros
            upcoming_length = len(num_copies) - 1
            if upcoming_length < copies_won:
                num_copies += [1 for x in range(copies_won - upcoming_length)]
            
            for i in range(copies_won):
                num_copies[i + 1] += num_copies[0]
            
            print(num_copies)
            total += num_copies.pop(0)
        
        total += sum(num_copies)
    
    print(total)



if __name__ == "__main__":
    main()