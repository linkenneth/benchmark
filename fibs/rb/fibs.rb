def fibs(n)
  if (n <= 1)
    1
  else
    fibs(n - 1) + fibs(n -2)
  end
end

puts fibs(ARGV[0].to_i)
