class IDException(Exception):
    def __init__(self, message = 'Please start your ID with "01"'):
        self.message = message
        super().__init__(self.message)

def add_id(id_list, employee_id):
    if not employee_id.startswith('09'):
        raise IDException('Please start your ID with "01"')
    else:
        id_list.append(employee_id)
        return id_list
list = []    
id = add_id(list, '09245678')
print(id)