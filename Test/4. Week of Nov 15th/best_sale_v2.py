#Main
def read_line_text(directory):
    
    with open(directory) as file:
        return file.readlines()

def name_id_locator(textLines):
    
    name_list = []
    id_list = []
    for line in textLines:
        comma_index = line.find(",")
        name_list.append(line[:comma_index])
        id_list.append(int(line[(comma_index+1):(comma_index+4)]))
    
    return name_list, id_list

def sale_by_month(sale_info_lines, year, id_list):
    
    sales = [0.0] * len(id_list)
    
    for line in sale_info_lines:
        id = int(line[:3])
        id_index = id_list.index(id)
        id_comma_index = line.find(",", 0, 5)
        month_comma_index = line.find(",", 5)
        month_slash_index = line.find("/")
        # line_month = int(line[(month_comma_index+1) : month_slash_index]) #This is for if yours find best by month
        year_slash_index = line.find("/", month_slash_index+1) #Best by year
        line_year = int(line[(year_slash_index+1):].replace("\n", "")) #Best by year
        
        #if (line_month == month):
        if (line_year == year):
            sale = float(line[(id_comma_index + 1):(month_comma_index)])
            sales[id_index] = sales[id_index] + sale
            
    return sales
            


def best_sale_id_locator(sale):
    
    sale_list = []
    for sale_price in sale:
        sale_list.append(sale_price)
    sale_list.sort(reverse=True)
    
    return sale.index(sale_list[0])

def main():
    
    year = int(input("Please enter the desired year: "))
    employee_info_lines = read_line_text("info.txt")
    sale_info_lines = read_line_text("sales.txt")
    
    names, ids = name_id_locator(employee_info_lines)
    sales_list = sale_by_month(sale_info_lines, year, ids)
    best_sale_id = best_sale_id_locator(sales_list)
    best_sale_name = names[best_sale_id]
    print("The highest sales for month", year, "was made by", best_sale_name)
    
main()
    
    
    
    
            

