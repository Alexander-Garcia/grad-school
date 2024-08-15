function count(arry1, arry2) {
  if (arry1.length !== arry2.length) {
    return false;
  }

  const frequencyOfNums = {};
  const frequencyOfSquares = {};
  for (let i = 0; i < arry1.length; i++) {
    frequencyOfNums[arry1[i]] = (frequencyOfNums[arry1[i]] || 0) + 1;
    frequencyOfSquares[arry2[i]] = (frequencyOfSquares[arry2[i]] || 0) + 1;
  }
  // check if key^2 is in frequency of sums
  for (const key in frequencyOfNums) {
    if (!(key**2 in frequencyOfSquares)) return false;
    if (frequencyOfNums[key] !== frequencyOfSquares[key**2]) return false;
  }
  return true;
}


// console.log(count([1, 2, 3, 2], [9, 1, 4, 4]));
// console.log(count([1, 1, 3, 2], [9, 1, 4, 4]));


function slidingWindow(array, n) {
  let maxSum = 0;
  for (let i = 0; i < n; i++) {
    maxSum += array[i];
  }
  tempSum = maxSum;
  for (let i = n; i < array.length; i++) {
    tempSum = tempSum - array[i - n] + array[i];
    maxSum = Math.max(tempSum, maxSum);
  }
  return maxSum;
}

// console.log('slidingWindow', slidingWindow([2, 6, 9, 2, 1, 8, 5, 6, 3], 3));
//
function mergeSorted(array1, m, array2, n) {
  let array2Pointer = n - 1;
  let array1End = m + n - 1;
  let array1Pointer = m - 1;

  for (let i = array1End; i > -1; i--) {
    if (array2[array2Pointer] >= array1[array1Pointer]) {
      array1[i] = array2[array2Pointer];
      array2Pointer--;
    } else if (array2[array2Pointer] < array1[array1Pointer]) {
      array1[i] = array1[array1Pointer];
    }
    if (i === (array1Pointer + 1)) {
      array1Pointer--;
    }
  }
}

// console.log(mergeSorted([1,2,3,0,0,0], 3, [2,5,6], 3));

