workflows: dict[str, list[tuple[str, str]]] = {
    # "in" : [("a>3333", R), ...],
    # ...
}

parts: list[list[int]] = []

def parse_input(path: str):
    with open(path) as f:
        while True:
            line = f.readline()
            if line == '\n':
                break

            name, rest = line.split('{')
            rules = rest[:-2].split(',')
            last = rules.pop()
            rule_list = [rule.split(':') for rule in rules]
            rule_list.append(last)

            workflows[name] = rule_list
        for line in f.readlines():
            xmas = line.strip('{}\n').split(',')
            values = [int(pair.split('=')[1]) for pair in xmas]
            parts.append(values)


def is_reject(part: list[int]):
    x, m, a, s = part
    workflow = 'in'

    while True:
        rules = workflows[workflow]
        for rule in rules:
            if type(rule) == str:
                if rule == 'R': return True
                if rule == 'A': return False
                else: 
                    workflow = rule
                    break

            condi, result = rule
            if eval(condi):
                if result == 'R': return True
                if result == 'A': return False
                else: 
                    workflow = result
                    break
            

def main():
    parse_input("input.txt")

    total = 0

    for part in parts:
        if is_reject(part): continue
        value = sum(part)
        #print(value)
        total += value
    print(total)
    

if __name__ == "__main__":
    main()