from __future__ import annotations

modules: dict[str, FlipFlop] = {}
pulse_buffer: list[tuple[str, bool]] = []
HIGH = True
LOW = False
FLIP_FLOP = '%'
num_high = 0
num_low = 0


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
    

def count(pulse: bool):
    global num_high
    global num_low
    if pulse:
        num_high += 1
    else:
        num_low += 1


class FlipFlop:
    def __init__(self, name, outputs):
        self.name = name
        self.state: bool = LOW
        self.outputs: list[str] = outputs
    def pulse(self, _, s: bool, pb):
        if s == LOW:
            self.state = not self.state
            pb += [(self.name, node_name, self.state) for node_name in self.outputs]
    def __repr__(self):
        return str(self.outputs)

class Conjunction:
    def __init__(self, name, outputs):
        self.name = name
        self.inputs: dict[str, bool] = {}
        self.outputs: list[str] = outputs
        self.state: bool = LOW
    def pulse(self, name: str, pulse: bool, pb: list):
        self.inputs[name] = pulse
        for node_name in self.inputs:
            state = self.inputs[node_name]
            #if any are low
            if state == LOW:
                self.state = HIGH
                pb += [(self.name, out_name, HIGH) for out_name in self.outputs]
                return
        #if all HIGH pulses
        self.state = LOW
        pb += [(self.name, out_name, LOW) for out_name in self.outputs]
    def __repr__(self):
        return str(self.inputs) + " | " + str(self.outputs)


def do_pulses(broadcast_list: list[str]):
    global pulse_buffer

    print("broadcaster", LOW)
    count(LOW)

    pulse_buffer = [('broadcaster', name, LOW) for name in broadcast_list]

    while pulse_buffer != []:
        sender, name, pulse = pulse_buffer.pop(0)
        node = modules.get(name)
        if node == None: continue
        node.pulse(sender, pulse, pulse_buffer)


def main():
    broadcast_list = parse("input.txt")
    for _ in range(1000):
        do_pulses(broadcast_list)
    print(num_high, num_low)
    print(num_high * num_low)



if __name__ == "__main__":
    main()
