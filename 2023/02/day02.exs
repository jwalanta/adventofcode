defmodule Day02 do

  # split input line to "n <color>" list
  def split(line) do
    line
    |> String.split(": ")
    |> Enum.at(1)
    |> String.replace("; ", ", ")
    |> String.split(", ")
  end

  # find max value of each colors
  def find_max(list, max_colors \\ %{"red" => 0, "green" => 0, "blue" => 0}) do
    data = hd(list)
    [nstr, color] = String.split(data, " ")
    {n, _} = Integer.parse(nstr)

    case length(list) do
      1 -> Map.put(max_colors, color, max(max_colors[color],n))
      _ -> find_max(tl(list), Map.put(max_colors, color, max(max_colors[color],n)))
    end

  end

  def find_max_and_check_fit(line, n) do
    m = find_max(split(line))
    cond do
      m["red"] <= 12 and  m["green"] <= 13 and  m["blue"] <= 14  -> n + 1
      true -> 0
    end
  end

  def find_power(line) do
    line
    |> split()
    |> find_max()
    |> Map.values()
    |> Enum.reduce(fn a, b -> a * b end)
  end

  def part1(input) do
    input
    |> Enum.with_index()
    |> Enum.map(fn {e, i} -> find_max_and_check_fit(e, i) end)
    |> Enum.sum()
  end

  def part2(input) do
    input
    |> Enum.map(fn e -> find_power(e) end)
    |> Enum.sum()
  end

end


{:ok, contents} = File.read("input.txt")
lines = String.split(contents, "\n", trim: true)

IO.write("Part 1:")
IO.puts(Day02.part1(lines))

IO.write("Part 2:")
IO.puts(Day02.part2(lines))
