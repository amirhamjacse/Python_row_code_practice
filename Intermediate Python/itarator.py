class MyIterator:
    def __init__(self):
        self.num = 1  # Starting number

    def __iter__(self):
        return self  # Returns the iterator object itself

    def __next__(self):
        if self.num > 5:  # Stop condition
            raise StopIteration
        value = self.num
        self.num += 1
        return value  # Returns the next value

# Using the iterator
it = MyIterator()

for num in it:
    print(num)  # Output: 1 2 3 4 5

its = MyIterator()

for nums in it:
    print(nums)  # Output: 1 2 3 4 5