var fs = require("fs");

fs.readSync(process.argv[2])

function quickSort(A) {
  if (A.length <= 1) {
    return A;
  }
  pivotIndex = Math.floor(Math.random() * A.length)
  pivot = A[pivotIndex];
  A[pivotIndex] = undefined;
  less = [];
  greater = [];

}
