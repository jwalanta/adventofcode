defmodule Day01 do
  defp digit?(c) when c >= "0" and c <= "9", do: c
  defp digit?(_), do: ""

  defp extract_numbers(str) do
    str
    |> String.graphemes()
    |> Enum.map(&digit?/1)
    |> Enum.join("")
  end

  defp replace(str) do
    # replacing string with number but keep first and last letter
    # so that it can ue re-used for other numbers
    str
    |> String.replace("one", "o1ne")
    |> String.replace("two", "t2wo")
    |> String.replace("three", "t3hree")
    |> String.replace("four", "f4our")
    |> String.replace("five", "f5ive")
    |> String.replace("six", "s6ix")
    |> String.replace("seven", "s7even")
    |> String.replace("eight", "e8ight")
    |> String.replace("nine", "n9ine")
  end

  defp get_num(str) do
    extracted_number_str = extract_numbers(str)
    num = String.first(extracted_number_str) <> String.last(extracted_number_str)
    {num_int, _} = Integer.parse(num)
    num_int
  end

  def part1(input) do
    input
    |> Enum.map(&get_num/1)
    |> Enum.sum()
  end

  def part2(input) do
    input
    |> Enum.map(&replace/1)
    |> Enum.map(&get_num/1)
    |> Enum.sum()
  end
end

# read input
{:ok, contents} = File.read("input.txt")
lines = String.split(contents, "\n", trim: true)

IO.write("Part 1:")
IO.puts(Day01.part1(lines))

IO.write("Part 2:")
IO.puts(Day01.part2(lines))
