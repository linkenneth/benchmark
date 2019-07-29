def quicksort A
  if len(A) <= 1
    return A
  end
  pivot_index = rand(0...A.length)
  pivot = A.delete_at(pivot_index)
  less, greater = [], []
  A.each do |x|
    if x <= pivot
      less.push x
    else
      greater.push x
  end
  return quicksort(less) + [pivot] + quicksort(greater)
end

if __FILE__ == $PROGRAM_NAME
  # read file
end
