# shaml

Shaml (short for Shameless) is a multi-language library that simplifies data handling by automatically converting input values to more appropriate types. It aims to reduce boilerplate code for type checking and conversion across various programming languages, providing a consistent and intuitive API.

![Static Badge](https://img.shields.io/badge/pip_install-shaml-grey?style=flat-square&logo=python&logoColor=%233776AB&labelColor=%23bde0fc)

![Static Badge](https://img.shields.io/badge/npm_install-shaml-grey?style=flat-square&logo=nodedotjs&logoColor=%235FA04E&labelColor=%23cbedc2)

![Static Badge](https://img.shields.io/badge/composer_require-mgks%2Fshaml-grey?style=flat-square&logo=php&logoColor=%24F5B93E&labelColor=%23c2ccfc)

## Supported Languages

*   Python
*   JavaScript (Node.js)

## Project Structure
```bash
shaml/
    README.md
└── javascript/
    ├── package.json
    ├── shaml.js
    └── README.md
    └── CHANGELOG.md
└── python/
    ├── setup.py
    └── shaml/
        ├── __init__.py
        ├── core.py
        └── __main__.py
    └── CHANGELOG.md
└── php/
    ├── shaml.php
    └── test.php
    └── CHANGELOG.md
```

## Installation

### Python
```bash
pip install shaml
```

### JavaScript (Node.js)
```bash
npm install shaml
```

### PHP
```bash
composer require mgks/shaml
```

## Usage

### Python

```python
from shaml import sl

# String to int/float
number = sl("123")  # Converts to integer 123
price = sl("45.67") # Converts to float 45.67

# String to boolean
flag = sl("True")   # Converts to boolean True
state = sl("False")  # Converts to boolean False

# String to list/dict
data = sl("[1, 2, '3']")  # Converts to list [1, 2, '3']
config = sl("{'name': 'Alice', 'age': '30'}")  # Converts to dict {'name': 'Alice', 'age': '30'}

# Accessing value
print(sl(123))
print(sl(123.45))
print(sl(True))
print(sl(False))
print(sl([1, 2, "3"]))
print(sl({"name": "Alice", "age": "30"}))
print(sl(None))
print(sl("hello"))
```

#### Dot Notation (Python)

If a JSON or dictionary is passed, then you can access each key using dot notation:

```python
from shaml import sl

config = sl("{'name': 'Alice', 'age': '30'}")
print(config.name)  # prints Alice
print(config.age)  # prints 30 as integer
```

### JavaScript (Node.js)

```javascript
const sl = require('shaml');

// String to number
const number = sl("123"); // Converts to number 123
const price = sl("45.67"); // Converts to number 45.67

// String to boolean
const flag = sl("true"); // Converts to boolean true
const state = sl("false"); // Converts to boolean false

// String to array/object
const data = sl("[1, 2, '3']"); // Converts to array [1, 2, '3']
const config = sl("{'name': 'Alice', 'age': '30'}"); // Converts to object {'name': 'Alice', 'age': '30'}

// Accessing value
console.log(sl(123));
console.log(sl(123.45));
console.log(sl(true));
console.log(sl(false));
console.log(sl([1, 2, "3"]));
console.log(sl({"name": "Alice", "age": "30"}));
console.log(sl(null));
console.log(sl("hello"));
```

#### Dot Notation (JavaScript)

If a JSON or object is passed, then you can access each key using dot notation:

```javascript
const sl = require('shaml');

const config = sl("{'name': 'Alice', 'age': '30'}");
console.log(config.name); // prints Alice
console.log(config.age); // prints 30 as number
```

### PHP
```php
<?php

require_once 'vendor/autoload.php';

// String to number
$number = sl("123");
echo $number . PHP_EOL;  // Output: 123
Use code with caution.
```

#### Array Access (PHP)
```php
<?php

require_once 'vendor/autoload.php';

$config = sl('{"name": "Alice", "age": "30"}');
echo $config['name'] . PHP_EOL;  // Output: Alice
echo $config['age'] . PHP_EOL;  // Output: 30
```

## Error Handling

Shaml will try to convert to the best of its ability; otherwise, it will return the original object.

### Python

```python
from shaml import sl

value = sl("hello")
print(value)  # prints hello
```

For debugging purposes, you can enable debug mode:

```python
from shaml import sl

value = sl("hello", debug=True)
```

Then it will return a `ShamelessError` object, which can be used to determine the error:

```python
from shaml import sl

value = sl("hello", debug=True)
if value:
    print("this will not be printed")
else:
    print(value, value.message, value.original_value)  # prints Shameless Error:  with original value hello   with original value hello
```

### JavaScript (Node.js)

```javascript
const sl = require('shaml');

const value = sl("hello");
console.log(value); // prints hello
```

## Configuration Options

### Python

| Option  | Description                                                                 | Default Value |
| ------- | --------------------------------------------------------------------------- | ------------- |
| `debug` | If set to `True`, the function will throw `ShamelessError` exceptions when a conversion fails. | `False`       |

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes.
4.  Write tests to verify your changes.
5.  Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.