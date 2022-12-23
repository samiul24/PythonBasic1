def myFunc(nums):
    print(nums)
    for i in nums:
        print(i)
        yield i*i

num = myFunc([1,2,3,4,5])
print(next(num))
print(next(num))
print(next(num))