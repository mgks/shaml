const sl = require('./shaml');

// String to number
console.log(sl("123"));
console.log(sl("45.67"));

// String to boolean
console.log(sl("true"));
console.log(sl("false"));

// String to array/object
console.log(sl("[1, 2, '3']"));
console.log(sl('{"name": "Alice", "age": "30"}')); // Corrected JSON syntax

// Accessing value
console.log(sl(123));
console.log(sl(123.45));
console.log(sl(true));
console.log(sl(false));
console.log(sl([1, 2, "3"]));
console.log(sl({"name": "Alice", "age": "30"}));

console.log(sl(null));
console.log(sl("hello"));

// Dot notation test (with correct JSON syntax)
const config = sl('{"name": "Alice", "age": "30"}');
console.log(config.name);
console.log(config.age);