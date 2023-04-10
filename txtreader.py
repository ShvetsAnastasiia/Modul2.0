import datetime

def read_data_from_file(filename):
    """
    Reads data from a text file with product information.

    Args:
        filename (str): the name of the file to read from.

    Returns:
        data (list): a list of product information in the format "product name, date, price".
    """
    with open(filename, 'r') as f:
        data = [line.strip().split(', ') for line in f]
    return data

def get_price_changes_for_product(product_name, data):
    """
    Returns the price changes for a specific product in the last month.

    Args:
        product_name (str): the name of the product to get price changes for.
        data (list): a list of product information in the format "product name, date, price".

    Returns:
        price_changes (list): a list of tuples containing the date and price for the product's price changes
            in the last month.
    """
    today = datetime.date.today()
    one_month_ago = today - datetime.timedelta(days=30)

    price_changes = []
    for product, date_str, price_str in data:
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        price = float(price_str)
        if product == product_name and date >= one_month_ago:
            price_changes.append((date, price))
    return price_changes

if __name__ == '__main__':
    filename = 'data.txt'
    data = read_data_from_file(filename)
    product_name = 'Product A'
    price_changes = get_price_changes_for_product(product_name, data)
    print(f'Price changes for {product_name} in the last month:')
    for date, price in price_changes:
        print(f'{date}: {price}')
