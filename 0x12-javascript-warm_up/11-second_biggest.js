#!/usr/bin/node

// script that searches the second biggest integer in the list of arguments.

let array = [];

const length = process.argv.length;
let i = 2;
if (length === 2 || length === 3)
    console.log(0);
else {
    while (i < length)
    {
	array.push(process.argv[i]);
	i++;
    }
    const sortedArray = array.sort().reverse();
    console.log(sortedArray[1]);
}
