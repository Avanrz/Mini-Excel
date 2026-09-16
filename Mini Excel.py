def f1 (letter):
    return ord(letter.upper()) - ord('A')

def f2 (cell_ref):
    col_letter = ''
    row_number = ''
    for i in cell_ref:
        if i.isalpha():
            col_letter += i
        else:
            row_number += i
    
    col = f1 (col_letter)
    row = int(row_number) - 1
    return row, col

def f3 (command, matrix):
    paren_index = command.find('(')
    func_name = command[:paren_index]
    
    args_str = command[paren_index + 1:-1]
    
    colon_index = args_str.find(':')
    start_cell = args_str[:colon_index]
    end_cell = args_str[colon_index + 1:]
    
    r1, c1 = f2 (start_cell)
    r2, c2 = f2 (end_cell)
    
    start_row = min(r1, r2)
    end_row = max(r1, r2)
    start_col = min(c1, c2)
    end_col = max(c1, c2)
        
    values = []
    for r in range(start_row, end_row + 1):
        for c in range(start_col, end_col + 1):
            values.append(matrix[r][c])
            
    if func_name == 'sum':
        return sum(values)
    elif func_name == 'min':
        return min(values)
    elif func_name == 'max':
        return max(values)

def main():
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
            result = f3 (command, matrix)
            print(command + " -> " + str(result))
            
        current_line_index = current_line_index + 1

main()
