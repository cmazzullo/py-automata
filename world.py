"""
One dimensional automata, a la Wolfram. Just for fun.
"""

import random


def step(world, rule):
    new_world = []
    for i in range(len(world)):
        new_world.append(rule(world[i], neighbors(world, i)))
    return new_world


def neighbors(world, index):
    "Edges are set to 0 for now"
    left = world[index - 1] if index > 0 else 0
    right = world[index + 1] if index < len(world) - 1 else 0
    return left + right


def stringify(world):
    return ''.join('X' if x else '.' for x in world)


def random_world(n):
    return random.choices([0, 1], k=n)


def make_rule(rule_string):
    def cell_rule(cell, neighbors):
        if cell == 0:
            if neighbors == 0:
                return int(rule_string[0])
            if neighbors == 1:
                return int(rule_string[1])
            if neighbors == 2:
                return int(rule_string[2])
        elif cell == 1:
            if neighbors == 0:
                return int(rule_string[3])
            if neighbors == 1:
                return int(rule_string[4])
            if neighbors == 2:
                return int(rule_string[5])
    return cell_rule


# Tests

def assertListEqual(l1, l2):
    for e1, e2 in zip(l1, l2):
        assert e1 == e2


assert neighbors([1, 0, 1], 2) == neighbors([1, 0, 1], 0) == 0
assert neighbors([1, 0, 1], 1) == 2

rule_string = '001110'
new_rule = make_rule(rule_string)
assert new_rule(0, 0) == 0
assert new_rule(0, 1) == 0
assert new_rule(0, 2) == 1
assert new_rule(1, 0) == 1
assert new_rule(1, 1) == 1
assert new_rule(1, 2) == 0

rule_string = '111000'
new_rule = make_rule(rule_string)
assert new_rule(0, 0) == 1
assert new_rule(0, 1) == 1
assert new_rule(0, 2) == 1
assert new_rule(1, 0) == 0
assert new_rule(1, 1) == 0
assert new_rule(1, 2) == 0

assertListEqual(step([1, 0, 1], make_rule('001110')), [1, 1, 1])

assert stringify([0, 1, 1]) == '.XX'


if __name__ == '__main__':
    "Run a whole little simulation with all the rules"
    generations = 100
    world_size = 100
    all_rules = ['{:06b}'.format(i) for i in range(2**6)]
    for i, rule_string in enumerate(all_rules):
        print(f'Rule {i}: {rule_string}')
        rule = make_rule(rule_string)
        world = random_world(world_size)
        for g in range(generations):
            print(stringify(world))
            world = step(world, rule)
