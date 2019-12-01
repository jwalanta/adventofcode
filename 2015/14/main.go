package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type attr struct {
	velocity, duration, rest, totalDistance, durationCounter, restCounter, points int
}

// used for part 1
func totalDistance(time, velocity, duration, rest int) int {

	totalDistance := 0
	durationCounter := duration
	restCounter := 0

	for t := 0; t < time; t++ {
		if durationCounter > 0 {
			totalDistance += velocity
			durationCounter--

			if durationCounter == 0 {
				restCounter = rest
				continue
			}
		}

		if restCounter > 0 {
			restCounter--
			if restCounter == 0 {
				durationCounter = duration
				continue
			}
		}

	}

	return totalDistance

}

// used for part 2
func tick(x *attr) {
	if x.durationCounter > 0 {
		x.totalDistance += x.velocity
		x.durationCounter--

		if x.durationCounter == 0 {
			x.restCounter = x.rest
			return
		}
	}

	if x.restCounter > 0 {
		x.restCounter--
		if x.restCounter == 0 {
			x.durationCounter = x.duration
			return
		}
	}
}

func main() {

	totalSeconds := 2503

	bytes, _ := ioutil.ReadFile("input.txt")
	lines := strings.Split(string(bytes), "\n")

	// part 1
	maxDistance := 0
	for _, line := range lines {
		if line == "" {
			continue
		}
		p := strings.Split(line, " ")

		velocity, _ := strconv.Atoi(p[3])
		duration, _ := strconv.Atoi(p[6])
		rest, _ := strconv.Atoi(p[13])

		d := totalDistance(totalSeconds, velocity, duration, rest)

		if d > maxDistance {
			maxDistance = d
		}

	}

	fmt.Println("part 1:", maxDistance)

	// part 2
	raindeers := make(map[string]*attr)
	for _, line := range lines {
		if line == "" {
			continue
		}
		p := strings.Split(line, " ")

		velocity, _ := strconv.Atoi(p[3])
		duration, _ := strconv.Atoi(p[6])
		rest, _ := strconv.Atoi(p[13])

		raindeers[p[0]] = &attr{velocity, duration, rest, 0, duration, 0, 0}
	}

	// tick for totalSeconds
	for t := 0; t < totalSeconds; t++ {
		// advance all
		max := 0
		for s := range raindeers {
			tick(raindeers[s])
			if raindeers[s].totalDistance > max {
				max = raindeers[s].totalDistance
			}
		}

		// award one point to all the winners
		for s := range raindeers {
			if raindeers[s].totalDistance == max {
				raindeers[s].points++
			}
		}

	}

	maxPoints := 0
	for _, v := range raindeers {
		if v.points > maxPoints {
			maxPoints = v.points
		}
	}

	fmt.Println("part 2:", maxPoints)
}
