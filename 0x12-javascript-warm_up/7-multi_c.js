#!/usr/bin/node
let i = 0;
const param = process.argv;
if (isNaN(param[2]) || param[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  const val = parseInt(param[2]);
  while (i < val) {
    console.log('C is fun');
    i++;
  }
}
