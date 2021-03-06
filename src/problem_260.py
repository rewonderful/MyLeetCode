#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def singleNumber(nums):
    """
    算法：bit位运算法
    思路：
        首先联想136题中异或运算XOR的作用
        N^0 = N
            N^N = 0
            A^B^A = (A^A)^B = 0^B = B
        但是本题中要找两个数，那么就可以想一下，可以依照某种规则，将数组中的元素划分为两组，在每一组中寻找那个单独的目标x和y

            一个理想的方式就是根据某一位是0还是1来划分，因为二进制下，不论任何数，某一位一定不是0就是1，自然就分成两组了
        所以可以先将所有元素异或xor一遍，得到一个bit，因为重复的元素N^N=0，所以最后的bit一定=X^Y，bit = X^Y,这个bit中
        的每一位都标识了这个位置上X，Y的取值是否相同
            如bit = 101，则代表X，Y的第一位不同，第二位相同，第三位不同。
            那么就可以根据bit来将元素划分为两组，且X，Y一定分别在其中一组中，取bit的某一位的1，其他位为0。
            一种简单的方式就是bit&-bit,就会取出最末尾的1，并且其他位置为0，以此为依据进行分组
            随后再次遍历数组，
            如果num&bit == 0，说明num这一位是0，划分到A组，A组内元素也要异或来运算取出重复元素，剩下的就是单独的那个
        不重复数字
            否则划分到B组，也是进行异或运算
            最后经历两次遍历后就可以求出这两个分别的值
    ------------------------------------------------------------------------------------------------------------------------------------
    假设数组中两个不同的数字为 A 和 B；
        1. 通过遍历整个数组并求整个数组所有数字之间的 XOR，根据 XOR 的特性可以得到最终的结果为 AXORB = A XOR B；
        2. 通过某种特定的方式，我们可以通过 AXORB 得到在数字 A 和数字 B 的二进制下某一位不相同的位；因为A 和 B 是不相同的，
        所以他们的二进制数字有且至少有一位是不相同的。我们将这一位设置为 1，并将所有的其他位设置为 0，我们假设我们得到的这
        个数字为 bitFlag；
        3. 那么现在，我们很容易知道，数字 A 和 数字 B 中必然有一个数字与上 bitFlag 为 0；因为bitFlag 标志了数字 A 和数字 B
        中的某一位不同，那么在数字 A 和 B 中的这一位必然是一个为 0，另一个为 1；而我们在 bitFlag 中将其他位都设置为 0，那么该
        位为 0 的数字与上 bitFlag 就等于 0，而该位为 1 的数字与上 bitFlag 就等于 bitFlag
        4.现在问题就简单了，我们只需要在循环一次数组，将与上 bitFlag 为 0 的数字进行 XOR 运算，与上 bitFlag 不为 0 的数组进
        行独立的 XOR 运算。那么最后我们得到的这两个数字就是 A 和 B。
    复杂度分析：
        时间：ON，两次ON遍历
        空间：O1，常数级
    """
    bit = 0
    for num in nums:
        bit ^= num
    bit &= -bit
    #或者bit =bit &(~(bit-1))
    ans = [0, 0]
    for num in nums:
        if num & bit == 0:
            ans[0] ^= num
        else:
            ans[1] ^= num
    return ans
def singleNumber1(self, nums):
    """
    算法：哈希表
    思路：
        统计一下，统计值==1的加入答案
    复杂度分析：
        时间：ON，
        空间：ON
    """
    record = {}
    result = []
    for num in nums:
        record.setdefault(num, 0)
        record[num] += 1
    for k, v in record.items():
        if v == 1:
            result.append(k)
    return result