package main

import "fmt"

type item struct {
	cost, damage, armor int
}

var weapons = map[string]item{
	"Dagger":     {8, 4, 0},
	"Shortsword": {10, 5, 0},
	"Warhammer":  {25, 6, 0},
	"Longsword":  {40, 7, 0},
	"Greataxe":   {74, 8, 0},
}

var armors = map[string]item{
	"":           {0, 0, 0}, // armor is optional
	"Leather":    {13, 0, 1},
	"Chainmail":  {31, 0, 2},
	"Splintmail": {53, 0, 3},
	"Bandedmail": {75, 0, 4},
	"Platemail":  {102, 0, 5},
}

var rings = map[string]item{
	"":           {0, 0, 0}, // ring is optional
	"Damage +1":  {25, 1, 0},
	"Damage +2":  {50, 2, 0},
	"Damage +3":  {100, 3, 0},
	"Defense +1": {20, 0, 1},
	"Defense +2": {40, 0, 2},
	"Defense +3": {80, 0, 3},
}

type player struct {
	hit, damage, armor int
}

func win(me, boss player) bool {

	isMyTurn := true

	for {

		if isMyTurn {
			damage := me.damage - boss.armor
			if damage < 1 {
				damage = 1
			}
			boss.hit -= damage
		} else {
			damage := boss.damage - me.armor
			if damage < 1 {
				damage = 1
			}
			me.hit -= damage
		}

		if me.hit <= 0 {
			return false
		}

		if boss.hit <= 0 {
			return true
		}

		isMyTurn = !isMyTurn

	}

}

func play(boss player) {

	minCost := 9999999
	maxCost := 0
	for _, weapon := range weapons {
		for _, armor := range armors {
			for ring1Name, ring1 := range rings {
				for ring2Name, ring2 := range rings {

					if ring1Name == ring2Name && ring1Name != "" {
						continue
					}

					totalCost := weapon.cost + armor.cost + ring1.cost + ring2.cost

					me := player{
						100,
						weapon.damage + armor.damage + ring1.damage + ring2.damage,
						weapon.armor + armor.armor + ring1.armor + ring2.armor,
					}

					if win(me, boss) {
						// minimum cost to win
						if totalCost < minCost {
							minCost = totalCost
						}
					} else {
						// maximum cost to still lost
						if totalCost > maxCost {
							maxCost = totalCost
						}
					}
				}
			}
		}
	}

	fmt.Println("Part 1:", minCost)
	fmt.Println("Part 2:", maxCost)

}

func main() {
	// input
	boss := player{100, 8, 2}

	play(boss)
}
