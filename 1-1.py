num_list = []
p_list = []
counter_pq = 0
number_of_prime_q = []
list_of_numbers_with_max_pq = []
# this is a change

def prime(number):
    flag = False
    if number > 1:
        # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break
        # check if flag is True
        if flag == False:
            return 'prime'


for i in range(0, 10):
    num_list.append(int(input()))

for number in num_list:
    prime_flag = 1
    counter = 0
    q_list = []
    for index in range(1, number+1):
        quotient, remainder = divmod(number, index)
        if remainder == 0:
            counter += 1  # found a quotient for number
            q_list.append(quotient)
    # print(q_list)
    c = 0
    for q_number in q_list:
        var = prime(q_number)
        if var == 'prime':
            c += 1
    # print(f'number of prime quotients for {number} is: {c}')
    number_of_prime_q.append(c)

# print(number_of_prime_q)
# print(max(number_of_prime_q))
# print(number_of_prime_q.count(max(number_of_prime_q)))

max_counter = number_of_prime_q.count(max(number_of_prime_q))
num_list_max_index = 0
number_of_prime_q_2 = number_of_prime_q
for index in range(0, max_counter):
    max_value = max(number_of_prime_q)
    max_index = number_of_prime_q.index(max_value)
    num_list_max_index += max_index
    list_of_numbers_with_max_pq.append(num_list[num_list_max_index])
    number_of_prime_q = number_of_prime_q[max_index+1:]

# print(list_of_numbers_with_max_pq)
print(f'{max(list_of_numbers_with_max_pq)} {max(number_of_prime_q_2)}')





