from __future__ import annotations
from part1 import count, HIGH, LOW, Conjunction, FlipFlop, do_pulses, pulse_buffer, FLIP_FLOP
import math

modules: dict[str, FlipFlop] = {}
pulse_buffer: list[tuple[str, bool]] = []

target = 'rx'
loop_counts: dict[str, int] = {}
loops = []


def parse(path: str):
    broadcaster: str
    cons = {}
    with open(path) as f:
        for line in f.readlines():
            module, output = line.strip().split(" -> ")
            results = output.split(', ')

            if module == "broadcaster":
                broadcaster = results
                continue
            
            module_type = module[0]
            name = module[1:]

            if module_type == FLIP_FLOP:
                modules[name] = FlipFlop(name, results)
            else:
                modules[name] = Conjunction(name, results)
    
    for node_name in modules:
        node = modules[node_name]
        for out_name in node.outputs:
            out = modules.get(out_name)
            if out == None: continue
            if type(out) != Conjunction: continue
            out: Conjunction
            out.inputs[node_name] = LOW
    
    return broadcaster


def find_inputs():
    con: Conjunction
    for key in modules:
        node = modules[key]
        #print(node.outputs)
        if target in node.outputs:
            con = node
            #print(target, node, con)
            break
    for input in con.inputs:
        loops.append(input)


def do_pulses(broadcast_list: list[str]):
    global pulse_buffer
    solutions = []
    count(LOW)
    pulse_buffer = [('broadcaster', name, LOW) for name in broadcast_list]
    while pulse_buffer != []:
        s = check_for_solution()
        if s != []: solutions += s

        sender, name, pulse = pulse_buffer.pop(0)
        count(pulse)
        node = modules.get(name)
        if node == None: continue
        node.pulse(sender, pulse, pulse_buffer)
    return solutions


def check_for_solution():
    out = []
    for critical in loops:
        node = modules[critical]
        if node.state == HIGH:
            loops.remove(critical)
            out.append(critical)
    return out


def main():
    broadcast_list = parse("input.txt")
    find_inputs()
    i = 0
    multiples = []
    while True:
        i += 1
        s = do_pulses(broadcast_list)
        if s != []:
            for x in s:
                multiples.append(i)
                print(x, i)
            
        if len(loops) == 0:
            break
    print(multiples)
    print(math.lcm(*multiples))
    
    



if __name__ == "__main__":
    main()