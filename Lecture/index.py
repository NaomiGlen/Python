def name_of_function(f_name, l_name):
    print(f'Hello my name is {f_name} {l_name}')

# name_of_function("kyle", l_name="Reimers")

some_list=[1,2,3,4,5]
some_list[2] = "Bananas"
# print(some_list)

# for i in range(0,len(some_list),1):
#     print(some_list[i])

# for item in some_list:
#     print(item)

Kyle = {
    'f_name' : 'Kyle',
    'l_name' : 'Reimers',
    'age' : 27,
}

if 'dob' not in Kyle:
    Kyle['dob'] = "April 7th"

Kyle['f_name'] = "Bob"
# print(Kyle)

# for key, value in Kyle.items():
#     print(key,value)


# for key in Kyle:
#     print(key, Kyle[key])

students=[
    {
        'f_name': "Kyle",
        'l_name' : 'Reimers',
        'age' : 27,
        'dob' : 'April 7th'
    },
    {
        'f_name': "Billy",
        'l_name' : 'Adams',
        'age' : 38,
        'dob' : 'January 6th'
    },
    {
        'f_name': "Sonny",
        'l_name' : 'Waters',
        'age' : 23,
        'dob' : 'June 10th'
    },
    {
        'f_name': "John",
        'l_name' : 'Doe',
        'age' : 50,
        'dob' : 'October 31'
    }
]
# print(students[1])
# for key, value in students[1].items():
#     print(key, value)

for one_student in students:
    output = ''
    for key, value in one_student.items():
        output += f'{key} - {value}, '
    print(output)