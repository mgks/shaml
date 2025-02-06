# shaml

Shaml (short for Shameless) is a multi-language library that simplifies data handling by automatically converting input values to more appropriate types. It aims to reduce boilerplate code for type checking and conversion across various programming languages, providing a consistent and intuitive API.

## Installation

```bash
npm install shaml
```

## Basic Usage

```javascript
const sl = require('shaml');

const number = sl("123"); // Converts to number 123
console.log(number);
```

For detailed documentation and usage examples, please refer to the [GitHub repository](https://github.com/mgks/shaml).