#####################################################
# APS106 Winter 2024 - Lab 6 - Chemical Eqn Checker #
#####################################################

######################################################
# PART 1 - Molecular Formula to Dictionary Converter #
######################################################
import re

def molecule_formula(compound_formula):
    """
    (str) -> dictionary

    When passed a string of the compound formula, returns a dictionary 
    with the elements as keys and the number of atoms of that element as values.
    
    Parameters
    ----------
    compound_formula : str
        A string representing a chemical compound formula. The formula
        is a combination of element symbols and numbers. The element
        symbols are a single uppercase letter, followed by zero or more
        lowercase letters. The numbers are integers.
    
    Returns
    -------
    dictionary
        A dictionary with the elements as keys and the number of atoms of
        that element as values.

    Examples
    --------
    >>> molecule_formula("C2H6O1")
    {'C': 2, 'H': 6, 'O': 1}

    >>> molecule_formula("C1H4")
    {'C': 1, 'H': 4}
    """
    ## To Do: Complete the function
    splitted = re.split(r'(\d+)', compound_formula)
    
    result = {}
    for i in range(1 ,len(splitted), 2):
        if splitted[i-1] not in result:
            result[splitted[i-1]] = int(splitted[i])
        else:
            result[splitted[i-1]] += int(splitted[i])
    
    return result

######################################################
# PART 2 - Chemical Expression to Element Dictionary #
######################################################
    
def expression_formula(expr_coeffs, expr_molecs):
    """
    (tuple (of ints), tuple (of dictionaries)) -> dictionary
    
    Calculate the total number of atoms of each element in a chemical expression.
    
    Parameters
    ----------
    expr_coeffs : tuple
        A tuple containing integers that represent the coefficients for molecules
        within the expression. The order of the coefficients correspond to the order
        of molecule dictionaries.
    expr_molecs : tuple
        A tuple containing dictionaries that define the molecules within the expression.
        The molecule dictionaries have the form {'atomic symbol' : number of atoms}.
        The order of the coefficients correspond to the order of molecule dictionaries.
    
    Returns
    -------
    dictionary
        A dictionary containing all elements within the expression as keys and the
        corresponding number of atoms for each element within the expression as values.

    Examples
    --------
    
    >>> # expression: 2NaCl + H2 + 5NaF
    >>> expression_formula((2,1,5), ({"Na":1, "Cl":1}, {"H":2}, {"Na":1, "F":1}))
    {'Na': 7, 'Cl': 2, 'H': 2, 'F': 5}
    
    """
    ## To Do: Complete the function

    result = {}

    for i in range(len(expr_coeffs)):
        for key in expr_molecs[i]:
            if key in result:
                result[key] += expr_coeffs[i] * expr_molecs[i][key]
            else:
                result[key] = expr_coeffs[i] * expr_molecs[i][key]
    
    return result

########################################################
# PART 3 - Identify Unbalanced Atoms in a Chemical Eqn #
########################################################

def identify_unbalanced_atoms(reactant_atoms, product_atoms):
    """
    (Dict,Dict) -> Set
    
    Identify the elements that are not balanced between two dictionaries 
    that represent two sides of a chemical equation.
    
    Parameters
    ----------
    reactant_atoms : Dict
        A dictionary containing the elements and the number of atoms of
        each element on the reactant side of a chemical equation.
    product_atoms : Dict
        A dictionary containing the elements and the number of atoms of
        each element on the product side of a chemical equation.

    Returns
    -------
    Set
        A set containing all the elements that are not balanced between
        the two dictionaries.

    
    Examples
    --------
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 1, "Cl" : 2})
    {'Na'}
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 2, "Cl" : 2})
    set()
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "F" : 2, "Cl" : 2})
    {'F', 'Na'}
    """
    ## To Do: Complete the function
    result = set()

    #gotta find keys of both sets

    for key in reactant_atoms:
        if key not in product_atoms or (reactant_atoms[key] != product_atoms[key]):
            result.add(key)

    for key in product_atoms:
        if key not in reactant_atoms:
            result.add(key)
    
    return result if len(result) > 0 else set()

###############################################
# PART 4 - Check Chemical Equation Balance    #
###############################################

def check_eqn_balance(reactants, products):
    """
    (tuple,tuple) -> Set
    
    Check if a chemical equation is balanced. Return any unbalanced
    elements in a set.
    
    Both inputs are nested tuples. The first element of each tuple is a tuple
    containing the coefficients for molecules in the reactant or product expression.
    The second element is a tuple containing strings of the molecules within
    the reactant or product expression. The order of the coefficients corresponds
    to the order of the molecules. The function returns a set containing any
    elements that are unbalanced in the equation.
    
    Parameters
    ----------
    reactants : tuple
        A two-element nested tuple containing the coefficients for molecules 
        in the reactant expression and the molecules themselves. 
    products : tuple
        A two-element nested tuple containing the coefficients for molecules
        in the product expression and the molecules themselves.

    Returns
    -------
    Set
        A set containing any elements that are unbalanced in the equation.
    
    Examples
    --------
    >>> # balanced equation: C3H8 + 5O2 <-> 4H2O + 3CO2
    >>> check_eqn_balance(((1,5), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))
    set()

    >>> # unbalanced equation: C3H8 + 2O2 <-> 4H2O + 3CO2
    >>> check_eqn_balance(((1,2), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))
    {'O'}
    """
    ## To Do: Complete the function

    reactant_list = []
    for reactant in reactants[1]:
        reactant_list.append(molecule_formula(reactant))
    
    product_list = []
    for product in products[1]:
        product_list.append(molecule_formula(product))
    
    return identify_unbalanced_atoms(
        expression_formula(
            reactants[0],
            reactant_list
        ),
        expression_formula(
            products[0],
            product_list
        )
    )
