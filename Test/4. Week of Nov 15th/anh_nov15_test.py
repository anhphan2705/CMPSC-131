def file_read_lines(directory):
    try:
        with open(directory) as file:
            return file.readlines()
    except FileNotFoundError:
        print("File not found!")
        
def id_name_init(info):
    
    id_name = {}
    for line in info:
        comma_index = line.find(',')
        id = int(line[(comma_index+1) :].replace("\n", ""))
        name = line[: comma_index]
        
        id_name.update({id:name})
        
    return id_name

def id_sale_init(sales_info, year):
    
    id_sale = {}
    for line in sales_info:
        #Find the format
        comma_id_index = line.find(',')
        comma_sale_index = line.find(',', (comma_id_index+1))
        slash_month_index = line.find('/')
        slash_year_index = line.find('/', (slash_month_index+1))
        #Save the info
        id = int(line[: comma_id_index])
        sale = float(line[(comma_id_index+1) : comma_sale_index])
        year_line = int(line[(slash_year_index+1) :].replace("\n", ""))
        
        if (year_line == year):
            if id in id_sale:
                id_sale.update({id:(id_sale.get(id) + sale)})
            else:
                id_sale.update({id:sale})
                
    return id_sale

def best_seller_id_finder(id_sale):
    
    return max(id_sale, key=id_sale.get)
        
def main():
    
    year = int(input("Please enter the desired year: "))
    info_file = file_read_lines("info.txt")
    sale_file = file_read_lines("sales.txt")
    if (info_file != None) and (sale_file != None):
        id_name_dict = id_name_init(info_file)
        id_sale_dict = id_sale_init(sale_file, year)
        best_seller_id = best_seller_id_finder(id_sale_dict)
        print(f"The highest sale was made by {id_name_dict.get(best_seller_id)}")
    else:
        print("Something went wrong! File not found or doesn't contain any data")
    
main()