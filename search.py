import json

def search_json(json_data, search_string):
    results = {}
    
    # Convert the search string to lower case
    search_string = search_string.lower()

    for products in json_data:
        # get the user details
        user_details = products['User']
        product = {}
        
        for key, value in products.items():
            if search_string in key.lower():
               # If the search string is avaliable add the key value pair to the product dictonary 
               product[key] = value 
        
        # Add the user's details and their matched products to the results dictionary    
        results[user_details] = product

    
    return results