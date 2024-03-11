#!/usr/bin/node
function factorial (value) {
  if (value < 0) {
    return (-1);
  }
  if (!value || value === 0) {
    return 1;
  }
  return (value * factorial(value - 1));
}

console.log(factorial(Number(process.argv[2])));
