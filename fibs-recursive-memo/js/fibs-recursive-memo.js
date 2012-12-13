/* Use like so:
 *     node fibs-recursive-memo.js [n]
 * where n is the nth Fibonnaci number you wish to calculate. */
memo = { '0' : 1, '1' : 1 }
/* Generates the nth Fibonacci number. */
function fibs(n) {
  if (memo[n]) {
    return memo[n];
  } else {
    memo[n] = fibs(n - 1) + fibs(n - 2);
    return memo[n];
  }
}

console.log(fibs(parseInt(process.argv[2])));
