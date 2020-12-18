my_int = 9
my_float =4.8
my_str="hello"
my_list= [1,2]
my_set = {400, None, "text", True}
my_dict = {"my dog":"sheepdog", "my pc":"dell"}

super_list=[my_int, my_float,my_str,my_list,my_set, my_dict,]
for n in super_list:
    print(f'{n} is {type(n)}')