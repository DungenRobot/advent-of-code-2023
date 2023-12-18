

mirror_map = []


def generate_map(path: str):
    with open(path) as f:
        for line in f.readlines():
            mirror_map.append([char for char in line.strip()])


cache = {}

def get_cache_key(pos: tuple[int, int], dir: str):
    return "(%s, %s) %s" % (*pos, dir)


def get_energy_value(pos: tuple[int, int], dir: str):
    key = get_cache_key(pos, dir)
    result = cache.get(key)
    if result != None:
        return result
    
    

    pass



def main():
    generate_map("test.txt")
    


if __name__ == "__main__":
    main()
