file_name = 'MyExcel.txt'

file = open(file_name, 'r')

lines = file.readlines()

file.close()

first_line = lines[0].split()
rows = int(first_line[0])
cols = int(first_line[1])

matrix = []

current_line_index = 1

for i in range(rows):
    line_content = lines[current_line_index].strip()
    
    numbers = line_content.split()
    row_data = []
    for num_str in numbers:
        row_data.append(int(num_str))
    
    matrix.append(row_data)
    
    current_line_index = current_line_index + 1

while current_line_index < len(lines):
    command = lines[current_line_index].strip()
    
    if len(command) > 0:
        paren_index = command.find('(')
        func_name = command[:paren_index]
        
        args_str = command[paren_index + 1:-1]
        
        colon_index = args_str.find(':')
        cell1 = args_str[:colon_index]
        cell2 = args_str[colon_index + 1:]
        
        col1_str = ""
        row1_str = ""
        for char in cell1:
            if char.isalpha():
                col1_str = col1_str + char
            else:
                row1_str = row1_str + char
        
        col1 = ord(col1_str[0]) - ord('A')
        row1 = int(row1_str) - 1
        
        col2_str = ""
        row2_str = ""
        for char in cell2:
            if char.isalpha():
                col2_str = col2_str + char
            else:
                row2_str = row2_str + char
            
        col2 = ord(col2_str[0]) - ord('A')
        row2 = int(row2_str) - 1
        
        start_row = min(row1, row2)
        end_row = max(row1, row2)
        start_col = min(col1, col2)
        end_col = max(col1, col2)
            
        values = []
        for r in range(start_row, end_row + 1):
            for c in range(start_col, end_col + 1):
                values.append(matrix[r][c])
            
        result = 0
        if func_name == 'sum':
            result = sum(values)
        elif func_name == 'min':
            result = min(values)
        elif func_name == 'max':
            result = max(values)
            
        print(command + " -> " + str(result))
        
    current_line_index = current_line_index + 1