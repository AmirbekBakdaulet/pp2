class PrimeNumberFilter:
    def __init__(self, numbers):
        self.numbers = numbers
    
    is_prime = lambda self, num: num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

    def filter_primes(self):
        prime_numbers = []
        for num in self.numbers:
            if self.is_prime(num):
                prime_numbers.append(num)
            elif num==1:
                prime_numbers.append(num)
        return prime_numbers
numbers = input()
list=[]
for i in numbers.split():
    list.append(int(i))
prime_filter = PrimeNumberFilter(list)
prime_numbers = prime_filter.filter_primes()
print(prime_numbers)

