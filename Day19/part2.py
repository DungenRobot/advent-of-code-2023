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
                return

            name, rest = line.split('{')
            rules = rest[:-2].split(',')
            last = rules.pop()
            rule_list = [rule.split(':') for rule in rules]
            rule_list.append(last)

            workflows[name] = rule_list


def dict_to_xmas(d: dict[str, list[int]]):
    return[ d['x'], d['m'], d['a'], d['s'], ]


def count_dict(d: dict[str, list[int]]):
    #print(d)
    total = 1
    for i in [ (d[key][1] - d[key][0] + 1) for key in d]:
        total *= i
    return total


def find_valid_combos(xmas: list[list[int, int]], flow_name: str):
    combinations = 0

    workflow = workflows[flow_name].copy()
    last = workflow.pop()
    x, m, a, s = xmas

    values = {
        'x' : x,
        'm' : m,
        'a' : a,
        's' : s,
    }

    for rule in workflow:
        condition, result = rule

        num_to_result = [] #the number of values that lead to the result
        num_to_pass = [] #the number of values that lead to continuing to the next statement

        if '<' in condition:
            trait, check = condition.split('<')
            lower, upper = values[trait]
            check = int(check)

            if (lower < check <= upper):
                num_to_result = [lower, check - 1]
                num_to_pass = [check, upper]
            elif (check > upper):
                num_to_result = [lower, upper]
            else:
                num_to_pass = [lower, upper]
        else: #'>' in condition
            trait, check = condition.split('>')
            lower, upper = values[trait]
            check = int(check)
            
            if (lower < check <= upper):
                num_to_result = [check + 1, upper]
                num_to_pass = [lower, check]
            elif (check > upper):
                num_to_pass = [lower, upper]
            else:
                num_to_result = [lower, upper]


        if num_to_result == []: continue
        
        values[trait] = num_to_result
        xmas_result = dict_to_xmas(values)
        xmas_result_dict = values.copy()

        values[trait] = num_to_pass

        match result:
            case 'R': continue
            case 'A': combinations += count_dict(xmas_result_dict)
            case _:
                if num_to_pass == []: return combinations
                combinations += find_valid_combos(xmas_result, result)

    if num_to_pass == []: return combinations
    match last:
        case 'R': return combinations
        case 'A': return combinations + count_dict(values)
        case _: return combinations + find_valid_combos(dict_to_xmas(values), last)


def main():
    parse_input("input.txt")

    xmas = [[1, 4_000] for _ in range(4)]

    print(find_valid_combos(xmas, 'in'))
    

if __name__ == "__main__":
    main()