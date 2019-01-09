#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Solution for https://adventofcode.com/2018/day/24
#

import re


class Group:
    def __init__(self, group_type, group_number, units, hit, weak, immune,
                 attack_damage, attack_type, initiative):
        self.group_type = group_type
        self.group_number = group_number
        self.units = int(units)
        self.hit = int(hit)
        self.weak = weak
        self.immune = immune
        self.attack_damage = int(attack_damage)
        self.attack_type = attack_type
        self.initiative = int(initiative)

        # updated during the simulation
        self.target = None

    def effective_power(self):
        return self.units * self.attack_damage

    def damage_to(self, group):
        if self.attack_type in group.immune:
            return 0
        elif self.attack_type in group.weak:
            return self.effective_power() * 2
        else:
            return self.effective_power()

    def attack_target(self):
        if self.target == None:
            return 0

        total = int(self.damage_to(self.target) / self.target.hit)
        if total > self.target.units:
            total = self.target.units

        # print self.group_type, "group", self.group_number, "attacks defending group", self.target.group_number, ", killing", total, "units"
        self.target.units -= total

        return total

    def print_self(self):
        print self.group_type, self.group_number, self.units


# array to hold instances of class Group
original_groups = []

# read input
f = open("day24-input.txt")
lines = f.read().split("\n")

group_type = ""  # current group type
group_count = {  # group numbering
    "Immune System": 1,
    "Infection": 1
}
for l in lines:
    if l.strip() == "":
        continue

    if ":" in l:
        group_type = l[:-1]
    else:
        p = re.findall(
            "(.*) units each with (.*) hit points (.*)with an attack that does (.*) (.*) damage at initiative (.*)",
            l)[0]

        weak_immune = p[2].replace("(", "").replace(")", "").split(";")

        weak = []
        immune = []
        for s in weak_immune:
            if "weak" in s:
                weak = s.replace("weak to ", "").strip().split(", ")
            elif "immune" in s:
                immune = s.replace("immune to ", "").strip().split(", ")

        original_groups.append(
            Group(group_type, group_count[group_type], p[0], p[1], weak,
                  immune, p[3], p[4], p[5]))
        group_count[group_type] += 1

boost = 0
while True:

    boost += 1

    # print "boost =",boost

    # create new groups with boosted immune
    groups = []
    for g in original_groups:
        boosted = boost if g.group_type == "Immune System" else 0

        groups.append(
            Group(g.group_type, g.group_number, g.units, g.hit, g.weak,
                  g.immune, g.attack_damage + boosted, g.attack_type,
                  g.initiative))

    # run simulation
    while True:
        # target selection

        # sort group by effective power, and initiative
        groups = sorted(
            groups,
            key=lambda g: (g.effective_power(), g.initiative),
            reverse=True)

        choice = set()

        # for each group, choose a target
        for g in groups:

            # possible targets (opposite group, not chosen already, and that can be damaged)
            targets = [
                t for t in groups if t.group_type != g.group_type and (
                    t.group_type,
                    t.group_number) not in choice and g.damage_to(t) > 0
            ]

            # sort by possible damage, then by effective power, finally by initiative
            targets = sorted(
                targets,
                key=
                lambda t: (g.damage_to(t), t.effective_power(), t.initiative),
                reverse=True)

            if len(targets) > 0:
                t = targets[0]
                choice.add((t.group_type, t.group_number))
                g.target = t
            else:
                g.target = None

        # attack order by initiative
        groups = sorted(groups, key=lambda g: g.initiative, reverse=True)

        # attack targets
        total_kills = 0
        for g in groups:
            total_kills += g.attack_target()

        # if there are no kills, then it's going in a loop. break this simulation
        if total_kills == 0:
            break

        groups = [g for g in groups if g.units > 0]

        # for g in groups:
        #     g.print_self()

        total_infection = len([g for g in groups if g.group_type == "Infection"])
        total_immune = len([g for g in groups if g.group_type == "Immune System"])
        if total_immune == 0 or total_infection == 0:
            break

    if total_kills != 0 and total_immune != 0:
        print sum([g.units for g in groups])
        break
