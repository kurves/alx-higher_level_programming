#!/usr/bin/node
const [arg1, arg2] = process.argv.slice(2);

if (arg1 && arg2) {
  console.log(arg1 +  'is' + arg2);
} else if(arg1) {
  console.log(arg1 + 'is undefine');
}else {
  console.log('undefined is undefined');
}
