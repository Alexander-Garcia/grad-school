// Worst time O(n^2)
// best O(n)
// Works well if data is coming in on already sorted data
function insertionSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    let currentValue = arr[i];
    let j;
    for (j = i - 1; j >= 0 && arr[j] > currentValue; j--) {
        arr[j + 1] = arr[j];
    }
    arr[j + 1] = currentValue;
  }
  return arr;
}

console.log('insertionSort([3, 2, 1, 4, 5])', insertionSort([3, 2, 1, 4, 5])); // [1, 2, 3, 4, 5]
