#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def removeKdigits( num, k):
    """
    算法：贪心+栈
        给定一个n位的数字，要取出其中的k位，那么选取的规则一定是从最高位开始，去向后比较，取出较大的那个数字
        如142190中从前面开始，取4出来剩下12190一定是<42190的，取完1位后变成n-1位，剩下的n-1位取数字的规则也是
        如此，这就形成了相似子结构，并且每次选取一位的策略是贪心的，选取使得当前数字长度下能使结果变得最小的那一位

        该算法利用栈的特性，将遍历过的数字存储起来，尽量在栈中维持一个递增的序列。如果有k个数字的删除名额，新入栈的
        数字如果比栈顶元素小，那么ok，直接入栈，如果栈顶元素比新入栈的元素大，那么就弹出该元素，因为刚才有提到，对比
        两个数字，删掉大的那个数字剩下的数字组成将比较小，这里要用while去循环删除，删得直到栈顶不大于当前新元素，当然了
        最多只能删除k次，这样来维持栈内元素是递增的，当删除掉k个后num还有元素，就直接入栈即可

        或者可能，整个序列本来就是递增的，入栈后就是递增的（栈顶大于新元素时才pop，否则就一直添加），如12345入栈
        后还是12345，这时如果k还不等于0，还有名额删除，由于栈是保持的递增的顺序，所以从栈顶popk次就好了

        要注意'0'入栈时的操作，避免结果中有'00020'这样的非法输出，其实'0'在入栈过程中完全可以看做是一个普通的数字，
        入栈时只是比较两个数字的大小，'0'在比较数字大小时就是一个普普通通的数字罢了，关键在于最后输出的时候，即0不能
        作为栈底，也就是说当栈stack==[]时，若当前数字是'0'，那么不允许入栈，保证栈底元素非0
        或者可以在最后输出的时候，先将str转int取出头部0再转回题目要求的str，但是这样比较麻烦，不如在入栈时就判断

    复杂度分析：
        时间：ON，遍历一次原数字，stack的操作也一定在On内，ON + ON= ON
        空间：ON，栈空间
    """
    if len(num) == k:
        return "0"
    stack = []
    for c in num:
        while stack != [] and int(stack[-1]) > int(c) and k > 0:
            stack.pop()
            k -= 1
        if (stack == [] and c != '0') or stack != []:
            stack.append(c)
    while stack != [] and k > 0:
        stack.pop()
        k -= 1
    if stack == []:
        return '0'
    else:
        return ''.join(stack)
if __name__ == '__main__':
    print(removeKdigits("1100000002002",1))