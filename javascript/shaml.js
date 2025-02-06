// javascript/shaml.js

/**
 * Attempts to convert the input value to a more appropriate type.
 * @param {any} value - The value to process.
 * @returns {any} - The converted value, or the original value if no conversion is possible.
 */
function sl(value) {
    // If it's already a number or boolean, return it
    if (typeof value === 'number' || typeof value === 'boolean') {
      return value;
    }
  
    // If it's a string, try to convert it
    else if (typeof value === 'string') {
      // Try converting to a number
      const num = Number(value);
      if (!isNaN(num)) {
        return num;
      }
  
      // Try converting to a boolean
      if (value.toLowerCase() === 'true') {
        return true;
      }
      if (value.toLowerCase() === 'false') {
        return false;
      }
  
      // Try parsing as JSON (array or object)
      try {
        // Attempt to parse the string as JSON
        const parsed = JSON.parse(value);
  
        // Recursively process the parsed object
        return processObject(parsed);
      } catch (e) {
        // If it's not a valid JSON, ignore the error
      }
  
      // If no conversion was possible, return the original string
      return value;
    }
  
    // If it's an array, process each element
    else if (Array.isArray(value)) {
      return value.map(sl);
    }
  
    // If it's an object, process its properties
    else if (typeof value === 'object' && value !== null) {
      return processObject(value);
    }
  
    // Otherwise, return the original value
    else {
      return value;
    }
  }
  
  /**
   * Processes an object, recursively applying sl() to its properties.
   * @param {object} obj - The object to process.
   * @returns {object} - The processed object.
   */
  function processObject(obj) {
    // If it's not an object, return it
    if (typeof obj !== 'object' || obj === null) {
      return obj;
    }
  
    // Create a new object to hold the processed properties
    const newObj = {};
  
    // Loop through the properties of the object
    for (const key in obj) {
      if (obj.hasOwnProperty(key)) {
        // Recursively apply sl() to the property value
        newObj[key] = sl(obj[key]);
      }
    }
  
    // Return the processed object
    return newObj;
  }
  
  module.exports = sl;