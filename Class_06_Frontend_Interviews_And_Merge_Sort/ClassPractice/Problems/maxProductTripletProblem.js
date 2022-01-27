/* 
Given an integer array, give the maximum product of a triplet in an array.

Examples:
Input = [10, 3, 5, 6, 20]
Output = 1200 (product of 10, 6, and 20)

Input:  [-10, -3, -5, -6, -20]
Output: -90

Input:  [1, -4, 3, -6, 7, 0]
Output: 168

Source: https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/
*/

const factors1 = [10, 3, 5, 6, 20] // 1200
const factors2 = [-10, -3, -5, -6, -20] // -90
const factors3 = [1, -4, 3, -6, 7, 0] // 168

function mergeSort(arr) {
    if (arr.length > 1) {
        let m = Math.floor(arr.length / 2);
        let l = arr.slice(0, m);
        let r = arr.slice(m, arr.length);
        mergeSort(l);
        mergeSort(r);

        let i = 0;
        let j = 0;
        let k = 0;

        while (i < l.length && j < r.length) {
            if (l[i] < r[j]) {
                arr[k] = l[i];
                i++;
            } else {
                arr[k] = r[j]
                j++;
            }
            k++;
        }

        while (i < l.length) {
            arr[k] = l[i];
            i++;
            k++;
        }

        while (j < r.length) {
            arr[k] = r[j];
            j++;
            k++;
        }
    }
    return arr;
}

function findBestProduct(arr) {
    arr = mergeSort(arr);
    topArr = arr.slice(arr.length - 3, arr.length);
    bottomArr = topArr.slice(arr.slice(0,2));
    topProduct = topArr[0] * topArr[1] * topArr[2];
    altProduct = bottomArr[0] * bottomArr[1] * topArr[topArr.length - 1];

    if (topProduct > altProduct) {
        return (topProduct);    
    } else {
        return (altProduct);
    }
}

console.log(findBestProduct(factors1));
console.log(findBestProduct(factors2));
console.log(findBestProduct(factors3));