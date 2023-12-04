defmodule Day03 do
  def char_at(lines, r, c) do
    rows = length(lines)
    cols = String.length(Enum.at(lines, 0))

    cond do
      r >= 0 and c >= 0 and r < rows and c < cols ->
        Enum.at(String.graphemes(Enum.at(lines, r)), c)

      true ->
        "."
    end
  end

  def is_symbol?(s) do
    String.contains?("~!@#$%^&*()_+=-?/", s)
  end

  def is_gear?(s) do
    s == "*"
  end

  def get_surroundings(x, y) do
    [
      {x - 1, y - 1},
      {x - 1, y},
      {x - 1, y + 1},
      {x, y - 1},
      {x, y + 1},
      {x + 1, y - 1},
      {x + 1, y},
      {x + 1, y + 1}
    ]
  end

  def number_if_part(engine, row, col, n) do
    is_part =
      Enum.to_list(col..(col + n - 1))
      |> Enum.map(fn c -> get_surroundings(row, c) end)
      |> List.flatten()
      |> Enum.uniq()
      # |> IO.inspect()
      |> Enum.map(fn {r, c} -> is_symbol?(char_at(engine, r, c)) end)

    if Enum.member?(is_part, true) do
      nstr = String.slice(Enum.at(engine, row), col, n)
      {n, _} = Integer.parse(nstr)
      n
    else
      0
    end
  end

  def number_if_gear(engine, row, col, n) do
    Enum.to_list(col..(col + n - 1))
    |> Enum.map(fn c -> get_surroundings(row, c) end)
    |> List.flatten()
    |> Enum.uniq()
    # |> IO.inspect()
    |> Enum.map(fn {r, c} ->
      if is_gear?(char_at(engine, r, c)) do
        nstr = String.slice(Enum.at(engine, row), col, n)
        {n, _} = Integer.parse(nstr)
        {r, c, n}
      else
        {}
      end
    end)
  end

  def find_parts(line, row, engine) do
    Regex.scan(~r/\d+/, line, return: :index)
    |> Enum.map(fn [{c, n}] -> number_if_part(engine, row, c, n) end)
  end

  def find_gears(line, row, engine) do
    Regex.scan(~r/\d+/, line, return: :index)
    |> Enum.map(fn [{c, n}] -> number_if_gear(engine, row, c, n) end)
  end

  def part1(input) do
    input
    |> Enum.with_index()
    # for each line, get list of numbers which are parts
    |> Enum.map(fn {line, r} -> find_parts(line, r, input) end)
    |> List.flatten()
    |> Enum.sum()
  end

  def part2(input) do
    input
    |> Enum.with_index()
    # for each line, check if number is gear
    # and get numbers in the form of {r, c, num}
    |> Enum.map(fn {line, r} -> find_gears(line, r, input) end)
    |> List.flatten()
    # filter out non-gears
    |> Enum.filter(fn x -> tuple_size(x) > 0 end)
    # change {r, c, n} to maps groups in the format {r,c} => [n1, n2, ..]
    |> Enum.group_by(fn {r, c, _} -> {r, c} end, fn {_, _, n} -> n end)
    # gears are valid only if they are a pair
    |> Map.filter(fn {_, v} -> length(v) == 2 end)
    # multiple values and sum everything
    |> Map.values()
    |> Enum.map(fn [x, y] -> x * y end)
    |> Enum.sum()
  end
end

{:ok, contents} = File.read("input.txt")
lines = String.split(contents, "\n", trim: true)

# engine = %{}

# engine =
#   Enum.reduce(Enum.with_index(lines), %{}, fn {line, r}, acc ->
#     Enum.reduce(Enum.with_index(String.graphemes(line)), acc, fn {s, c}, acc ->
#       # IO.puts("#{r} #{c} #{s}")
#       Map.put(acc, {r, c}, s)
#     end)
#   end)

IO.write("Part 1:")
IO.puts(Day03.part1(lines))

IO.write("Part 2:")
IO.puts(Day03.part2(lines))
