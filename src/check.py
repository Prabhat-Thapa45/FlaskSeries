from src.execute_sql import query_handler_no_fetch


def check_flower_by_name(results: tuple, flower_name: str) -> bool:
    """Checks if the given flower_name is available in results if yes returns True else False
    Args:
        results (tuple): a tuple consisting of dict type as elements from rows of sql tables.
            e.g: for table with one row ({'id': 1, 'flower_name': 'Rose', 'price': 6.5, 'quantity': 21},)
        flower_name (str): name of a flower
    returns:
        boolean 
    """
    for items in results:
        for key in list(items.items())[1]:
            if items[key] == flower_name:
                return True
            else:
                return False


def int_convertor(value: str) -> int:
    """Converts str type to int type
    Args:
        value (str): strings to be converted to int type
    return:
        int
    raises:
        ValueError: if value is str that cannot be converted into int
    """
    try:
        return int(value)
    except ValueError:
        return 0


def validate_purchase_input(quantity, bouquet_size, available_in_stock, username, flower_name, price):
    if quantity == 0:
        return ["No items were added into your cart", "danger",  bouquet_size]
    if available_in_stock < quantity:
        return [f"We can't meet your demand, we only have {available_in_stock} of them in stock", "danger", 
                bouquet_size]
    elif bouquet_size >= quantity > 0:
        bouquet_size -= quantity
        query = "INSERT INTO orders(username, flower_name, quantity, price) VALUES(%s, %s, %s, %s)"
        values = (username, flower_name, quantity, price)
        query_handler_no_fetch(query, values)
        return ["Item added to cart", "success", bouquet_size]
    elif bouquet_size < quantity:
        return ["You have exceeded bouquet size", "danger", bouquet_size]
    elif quantity < 0:
        return ["Order quantity cannot be less than zero", "danger", bouquet_size]
