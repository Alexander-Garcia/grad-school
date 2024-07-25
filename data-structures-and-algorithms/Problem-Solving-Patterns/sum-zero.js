function sumZero(arry) {
  let left = 0;
  let right = arry.length - 1;
  while (left < right) {
    let sum = arry[left] + arry[right];
    if (sum === 0) {
      return [arry[left], arry[right]];
    } else if (sum > 0) {
      right--;
    } else if (sum < 0) {
      left++;
    }
  }
}

console.log(sumZero([-3, -2, -1, 0, 1, 2, 3])); // [-3, 3]
