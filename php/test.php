<?php

require_once 'shaml.php';

// String to number
echo sl("123") . PHP_EOL;
echo sl("45.67") . PHP_EOL;

// String to boolean
echo (sl("true") ? 'true' : 'false') . PHP_EOL;
echo (sl("false") ? 'true' : 'false') . PHP_EOL;

// String to array/object
print_r(sl("[1, 2, '3']"));
echo PHP_EOL;
print_r(sl("{'name': 'Alice', 'age': '30'}"));
echo PHP_EOL;

// Accessing value
echo sl(123) . PHP_EOL;
echo sl(123.45) . PHP_EOL;
echo (sl(true) ? 'true' : 'false') . PHP_EOL;
echo (sl(false) ? 'true' : 'false') . PHP_EOL;
print_r(sl([1, 2, "3"]));
echo PHP_EOL;
print_r(sl(["name" => "Alice", "age" => "30"]));
echo PHP_EOL;

echo sl(null) . PHP_EOL;
echo sl("hello") . PHP_EOL;

$config = sl('{"name": "Alice", "age": "30"}');
echo $config["name"] . PHP_EOL;
echo $config["age"] . PHP_EOL;