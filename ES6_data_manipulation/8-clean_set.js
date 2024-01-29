export default function cleanSet(set, startString) {
  if (!(set instanceof Set) || !startString || typeof startString !== 'string') return '';

  const setArray = [...set];
  const newSet = setArray
    .filter((item) => item && item.startsWith(startString))
    .map((item) => item.slice(startString.length));

  return newSet.join('-');
}
