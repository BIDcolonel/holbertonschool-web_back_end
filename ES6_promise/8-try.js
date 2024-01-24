export default function divideFunction(numerator, denominator) {
  // Check if denominator is zero
  if (denominator === 0) {
    // Throw an error for division by zero
    throw new Error('cannot divide by 0');
  }
  return numerator / denominator;
}
