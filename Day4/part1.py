
def main():

    total = 0

    with open("input.txt") as f:
        for line in f.readlines():
            line = line.split(': ')[1] #removes the first part of the line
            line = line.replace("  ", " ").strip() #removes double spaces and newline

            winning, scratch = line.split(" | ")
            winning = winning.split(" ")
            scratch = scratch.split(" ")

            power = -1

            for num in scratch:
                if num in winning:
                    power += 1
            
            if power != -1: 
                total += pow(2, power)
    
    print(total)


if __name__ == "__main__":
    main()
