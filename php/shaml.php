<?php

/**
 * Attempts to convert the input value to a more appropriate type.
 *
 * @param mixed $value The value to process.
 *
 * @return mixed The converted value, or the original value if no conversion is possible.
 */
function sl($value)
{
    if (is_int($value) || is_float($value) || is_bool($value)) {
        return $value; // Already a number or boolean
    } elseif (is_string($value)) {
        // Attempt string to number conversion
        if (is_numeric($value)) {
            return $value + 0; // Convert to number (int or float)
        }

        // Attempt string to boolean conversion
        if (strtolower($value) === 'true') {
            return true;
        }
        if (strtolower($value) === 'false') {
            return false;
        }

        // Attempt string to array/object conversion (JSON)
        $json = json_decode($value, true);
        if (json_last_error() === JSON_ERROR_NONE) {
            return $json;
        }

        return $value; // Return original string
    } elseif (is_array($value)) {
        // Attempt to convert the array items to sl values
        return array_map('sl', $value);
    }

    return $value; // Return original value if no conversion is possible
}