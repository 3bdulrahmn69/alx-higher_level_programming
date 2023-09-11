#!/usr/bin/node
if (parseInt(process.argv[2])) {
  const size = parseInt(process.argv[2]);
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let x = 0; x < size; x++) {
      row += '#';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
