package main

import (
	"fmt"
	"math/rand"
)

type Boss struct {
	hit, damage int
}

type Wizard struct {
	hit, mana, armor                           int
	shieldEffect, poisonEffect, rechargeEffect int
	totalMana                                  int
}

type Spell struct {
	name string
	mana int
}

func (boss *Boss) doDamage(n int) {
	boss.hit -= n
}

func (wizard *Wizard) doDamage(n int) {
	totalDamage := n - wizard.armor

	if totalDamage < 0 {
		totalDamage = 1
	}
	wizard.hit -= totalDamage
}

func (boss *Boss) isDead() bool {
	return boss.hit <= 0
}

func (wizard *Wizard) isDead() bool {
	// minimum mana required to purchase spell = 53
	return wizard.hit <= 0 || wizard.mana < 53
}

func (wizard *Wizard) castSpell(spell Spell, boss *Boss) {

	if spell.name == "MagicMissile" {
		boss.doDamage(4)
	}

	if spell.name == "Drain" {
		boss.doDamage(2)
		wizard.hit += 2
	}

	if spell.name == "Shield" {
		wizard.armor += 7
		wizard.shieldEffect = 6
	}

	if spell.name == "Poison" {
		wizard.poisonEffect = 6
		// nothing else to do here, damage done will be during tickTock
	}

	if spell.name == "Recharge" {
		wizard.rechargeEffect = 5
		// nothing to do here. mana increase will be during tickTock
	}

	wizard.totalMana += spell.mana
	wizard.mana -= spell.mana
}

func (wizard *Wizard) canCast(spell Spell) bool {
	if spell.mana > wizard.mana {
		return false
	}

	// spell cant be applied if it's already in effect
	if spell.name == "Shield" && wizard.shieldEffect > 0 {
		return false
	}

	if spell.name == "Poison" && wizard.poisonEffect > 0 {
		return false
	}

	if spell.name == "Recharge" && wizard.rechargeEffect > 0 {
		return false
	}

	// ok for everything else
	return true
}

func (wizard *Wizard) tickTock(boss *Boss) {

	if wizard.shieldEffect > 0 {
		wizard.shieldEffect--
	} else {
		wizard.armor = 0
	}

	if wizard.poisonEffect > 0 {
		boss.doDamage(3)
		wizard.poisonEffect--
	}

	if wizard.rechargeEffect > 0 {
		wizard.mana += 101
		wizard.rechargeEffect--
	}

}

var spells = []Spell{
	Spell{"MagicMissile", 53},
	Spell{"Drain", 73},
	Spell{"Shield", 113},
	Spell{"Poison", 173},
	Spell{"Recharge", 229},
}

var minMana = 9999999
var part2 = false // part 2 has 1 hit points in each turn

func play(boss Boss, player Wizard) {

	for {

		// player turn

		if part2 {
			player.doDamage(1)
			if player.isDead() {
				break
			}
		}

		player.tickTock(&boss)

		// pick a spell in random that works
		n := 0
		for {
			n = rand.Intn(len(spells))
			if player.canCast(spells[n]) {
				break
			}
		}

		player.castSpell(spells[n], &boss)

		player.tickTock(&boss)

		if boss.isDead() {
			if player.totalMana < minMana {
				minMana = player.totalMana
				break
			}
		}

		// boss turn
		player.doDamage(boss.damage)

		if player.isDead() {
			break
		}

	}
}

func main() {

	// Input:
	// Hit Points: 71
	// Damage: 10

	// PART 1

	// there are too many combinations to check all (similar to day 19)
	// so do random runs enough times to get the answer
	for i := 0; i < 1000000; i++ {

		boss := Boss{71, 10}
		player := Wizard{hit: 50, mana: 500}

		play(boss, player)

	}

	fmt.Println("Part 1:", minMana)

	// PART 2

	minMana = 999999999
	part2 = true // activate part 2
	for i := 0; i < 1000000; i++ {

		boss := Boss{71, 10}
		player := Wizard{hit: 50, mana: 500}

		play(boss, player)

	}

	fmt.Println("Part 2:", minMana)

}
