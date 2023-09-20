IO.puts("n = ")
n = IO.gets("")

for a <- 2..(n - 1) do
	k = 0
	for i{}< - 2..(div(a, 2) + 1) do
		if rem(a, i) == 0 do
			k= k + 1
		end
	end
	if k <= 0 do
		IO.puts(a)
	end
end
