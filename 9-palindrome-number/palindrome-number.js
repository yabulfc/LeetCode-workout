/**
 * @param {number} x
 * @return {boolean}
 */
function isPalindrome(x) {
  // Negative numbers are not palindromes
  if (x < 0) return false;

  // Convert number to string
  let str = x.toString();

  // Reverse the string
  let reversed = str.split('').reverse().join('');

  // Compare original and reversed strings
  return str === reversed;
}