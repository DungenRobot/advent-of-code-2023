
def main():

    values = []
    modified = []

    f = open("input.txt")

    values = [int(i) for i in f.readline().removeprefix("seeds:").strip().split(' ')]
    seeds = []
    seeds_unchanged = []
    seeds_out = []
    
    start = -1
    for v in values:
        if start == -1:
            start = v
        else:
            seeds.append([start, v])
            start = -1

    f.readline()

    for line in f.readlines():
        line = line.strip()
        if line == "":
            continue
        if line.endswith(":"):
            seeds += seeds_out
            seeds_out = []
            print(seeds)
            print(line)
            continue

        destination, source, length = line.split(' ')
        destination, source, length = int(destination), int(source), int(length)
        end = (source + length)

        for seed_start, seed_length in seeds:
            seed_end = seed_start + seed_length

            #range is entirely within the bounds
            if (source <= seed_start) and (seed_end < end):
                seed_start += destination - source

                seeds_out.append([seed_start, seed_length])

            #range is around bounds (must remove middle)
            elif (seed_start < source) and (end < seed_end):
                section_start = [seed_start, source - seed_start]
                section_middle = [destination, length]
                section_end = [end, seed_end - end]

                seeds_unchanged.append(section_start)
                seeds_out.append(section_middle)
                seeds_unchanged.append(section_end)

            #only the start of the range is in bounds
            elif (source <= seed_start < end):
                section_start = [seed_start, end - seed_start]
                section_end = [end, seed_end - end]
                section_start[0] += destination - source

                seeds_out.append(section_start)
                seeds_unchanged.append(section_end)
            
            #only the end of the range is in bounds
            elif (source <= seed_end < end):
                print("original:", [seed_start, seed_length])
                section_start = [seed_start, source - seed_start]
                section_end = [source, seed_end - source]
                section_end[0] += destination - source

                print(section_start, section_end)
                seeds_unchanged.append(section_start)
                seeds_out.append(section_end)

            #range is entirely outside of the bounds
            else:
                seeds_unchanged.append([seed_start, seed_length])
            
            print(seeds_out)

        seeds = seeds_unchanged
        seeds_unchanged = []

    print(seeds)
    print(min(seeds)[0])


if __name__ == "__main__":
    main()