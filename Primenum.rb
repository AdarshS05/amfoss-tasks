print "n= "
n = gets.chomp.to_i

for a in 2..(n - 1)
  k = 0
  for i in 2..(a / 2)
    if (a % i == 0)
      k = k + 1
    end
  end
  if k <= 0
    puts a
  end
end
