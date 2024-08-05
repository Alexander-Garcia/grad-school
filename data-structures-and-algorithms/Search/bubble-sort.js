// optimized with noSwaps
function bubbleSort(arry) {
  let noSwap;
  for (let i = arry.length; i > 0; i--) {
    noSwap = true;
    for (let j = 0; j < i - 1; j++) {
      if (arry[j] > arry[j + 1]) {
        let temp = arry[j];
        arry[j] = arry[j + 1];
        arry[j + 1] = temp;
        noSwap = false;
      }
    }
    if (noSwap) break;
  }
  return arry;
}

console.log(bubbleSort([3, 2, 1, 5, 4])); // [1, 2, 3, 4, 5]
