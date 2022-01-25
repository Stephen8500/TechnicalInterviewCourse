/**
 * 
 * Given an integer array nums, are there elements a, b, and c in nums such that a + b + c = 0? Find all unique triplets in the array which give the sum of zero.

 * Input = [-1, 0, 1, 2, -1, 4]
 * Output = [[-1, 0, 1], [-1, -1, 2]]

 * Input = [0]
 * Output = []
 * 
 * Source: https://leetcode.com/problems/3sum/description/
 * Solution walkthrough: https://fizzbuzzed.com/top-interview-questions-1/
 */

const arr1 = [-1, 0, 1, 2, -1, 4]
const arr2 = [0]

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



console.log(mergeSort(arr1))