// O(n^2)
function selectionSort(arry) {
  let minIndex;
  for (let i = 0; i < arry.length; i++) {
    minIndex = i;
    for (let j = i + 1; j < arry.length; j++) {
      if (arry[j] < arry[minIndex]) {
        minIndex = j;
      }
    }
    if (minIndex !== i) {
        let temp = arry[i]
        arry[i] =  arry[minIndex]
        arry[minIndex] = temp;
    }
  }
  return arry;
}

console.log(selectionSort([5, 3, 4, 1, 2])); // [1, 2, 3, 4, 5]
