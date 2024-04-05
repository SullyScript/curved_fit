# ECOR 1042 Lab 6 - Template for curve_fit function



# Remember to include docstring and type annotations for your functions



# Update "" with your name (e.g., Cristina Ruiz Martin)

__author__ = ""



# Update "" with your student number (e.g., 100100100)

__student_number__ = ""



# Update "" with your team (e.g. T-102, use the notation provided in the example)

__team__ = ""


#==========================================#

# Place your curve_fit function after this line

def curve_fit(characters: list[dict], attribute: str, degree: int) -> str:
    """
    """
    import numpy as np
    
    attribute_list = []
    health_list = []

    for character in characters:
        if character[attribute] not in attribute_list:
            attribute_list.append(character[attribute])
            health_list.append([character["Health"]])
        
        else:
            index = attribute_list.index(character[attribute])
            health_list[index].append(character["Health"])
    
    for i in range(len(health_list)):
        health_list[i] = np.mean(health_list[i])

    if len(attribute_list) <= degree:
        deg = len(attribute_list) - 1
    
    else:
        deg = degree
    
    attribute_list = np.array(attribute_list, dtype=float)
    health_list = np.array(health_list, dtype=float)

    coefficients = np.polyfit(attribute_list, health_list, deg)

    expression = "y = "
    
    for h in range(len(coefficients)):
        power = len(coefficients) - h - 1
        coef_str = f"{coefficients[h]:.2f}"
        
        if power > 1:
            expression += f"{coef_str}x^{power} + "
        
        elif power == 1:
            expression += f"{coef_str}x + "
       
        else:
            expression += coef_str

    expression = expression.rstrip(" + ")

    return expression


# Do NOT include a main script in your submission