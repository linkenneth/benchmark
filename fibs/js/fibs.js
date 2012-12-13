/* Use like so:
 *     node fibs.js [n]
 * where n is the nth Fibonnaci number you wish to calculate. */

/* Generates the nth Fibonacci number. */
function fibs(n) {
  if (n <= 1) {
    return 1;
  } else {
    return fibs(n - 1) + fibs(n - 2);
  }
}

console.log(fibs(parseInt(process.argv[2])));
