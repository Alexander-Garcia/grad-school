// ONLY works on sorted array
// Big O -> O(log n)
function binarySearch(arr, element) {
  let start = 0;
  let end = arr.length - 1;
  let middle = Math.floor((start + end) / 2);

  while(arr[middle] !== element && start <= end) {
    if (arr[middle] > element) {
      end = middle - 1;
    } else {
      start = middle + 1;
    }
    middle = Math.floor((start + end) / 2);
  }
  return arr[middle] === element ? middle : -1;
}

console.log(binarySearch([1, 2, 3, 4, 5], 3)); // 2
console.log(binarySearch([1, 2, 3, 4, 5], 10)); // 2
