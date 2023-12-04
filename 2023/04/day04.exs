defmodule Day04 do
  def total_matches(line) do
    %{"mine" => mine_str, "winning" => winning_str} =
      Regex.named_captures(~r/Card.*: (?<winning>.*) \| (?<mine>.*)/, line)

    mine = String.split(mine_str, ~r/[ ]+/)
    winning = String.split(winning_str, ~r/[ ]+/)
    common = mine -- mine -- winning

    length(common)
  end

  def process_cards(matches, cards_count, n) do
    if n == length(matches) do
      cards_count
    else
      cards_count_new =
        cards_count
        |> Enum.with_index()
        |> Enum.map(fn {_, i} ->
          if i > n and i <= n + Enum.at(matches, n) do
            Enum.at(cards_count, i) + Enum.at(cards_count, n)
          else
            Enum.at(cards_count, i)
          end
        end)

      process_cards(matches, cards_count_new, n + 1)
    end
  end

  def part1(input) do
    input
    |> Enum.map(fn l -> total_matches(l) end)
    |> Enum.map(fn n -> if n > 0, do: 2 ** (n - 1), else: 0 end)
    |> Enum.sum()
  end

  def part2(input) do
    matches = input |> Enum.map(fn l -> total_matches(l) end)
    cards_count = List.duplicate(1, length(input))

    process_cards(matches, cards_count, 0)
    # |> IO.inspect()
    |> Enum.sum()
  end
end

{:ok, contents} = File.read("input.txt")
lines = String.split(contents, "\n", trim: true)

IO.write("Part 1:")
IO.puts(Day04.part1(lines))

IO.write("Part 2:")
IO.puts(Day04.part2(lines))
