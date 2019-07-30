def find_number_pairs(numbers, N=10):
    final_list =[]

    for index in range(len(numbers)):
    	if round(N-numbers[index],2) in numbers[index+1:]:
    		final_list.append((numbers[index],round(N-numbers[index],2)))

    return final_list

