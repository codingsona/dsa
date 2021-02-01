def swap_name(in_str):
    new_list = list(in_str)
    new_list[0], new_list[-1] = new_list[-1], new_list[0]
    name_swapped = ('').join(new_list)
    print(name_swapped)

swap_name('sonali')
swap_name('shanti')



