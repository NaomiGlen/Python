 # # SENSEI way using a for loop (Good for if there are many fields)
        # # Loop over the dictionary with the user data
        # for field in user:
        #     # Test if any of the entered values are empty strings
        #     if len(user[field]) <= 0:
        #         is_valid = False
        #         message = f"{field} is required.".capitalize()

        #         # Take the _ out of the field names
        #         make_pretty = message.maketrans("_", " ")
        #         flash(message.translate(make_pretty))