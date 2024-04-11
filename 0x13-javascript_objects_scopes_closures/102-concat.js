#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
    console.log('Usage: node concatFiles.js <sourceFile1> <sourceFile2> <destinationFile>');
    process.exit(1);
}

const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

const file1Content = fs.readFileSync(sourceFile1, 'utf8');
const file2Content = fs.readFileSync(sourceFile2, 'utf8');

const concatenatedContent = file1Content + file2Content;

fs.writeFileSync(destinationFile, concatenatedContent);

console.log(`Files ${sourceFile1} and ${sourceFile2} concatenated and written to ${destinationFile}`);
