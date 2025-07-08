#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length < 4) {
  console.log(0);
} else {
  const listNum = [];
  for (let i = 2; i < argv.length; i++) {
    const element = parseInt(argv[i]);
    listNum.push(element);
  }

  listNum.sort((a, b) => b - a);
  console.log(listNum[1]);
}
