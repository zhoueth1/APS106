def extract_name_from_email(email):
    """
    (str) -> str
    
    Given a string with the format "first_name.last_name@domain.com",
    return a string containing the first and last names separated by a comma.

    Parameters
    ----------
    email : str
        A string with the format "first_name.last_name@domain.com" where
        first_name and last_name are strings of characters with no spaces

    Returns
    -------
    str
        A string with the format "Last_name,First_name" where
        the first and last names are capitalized and separated by a comma
    
    >>> email_to_name("anna.conda@mail.utoronto.ca")
    'Conda,Anna'
    """
    
    # To Do: Complete the function
    return email[email.index('.') + 1:email.index('@')].capitalize() + ',' + email[:email.index('.')].capitalize()

def calculate_site_average(measurements, site):
    """
    (str, str) -> str
 
    Given s, a string representation of comma separated site-measurement
    pairs, return the average of the site measurements to two decimal places.

    Parameters
    ----------
    measurements : str
        A string of comma separated site-measurement pairs where the site
        is a string and the measurement is a float.
    site : str
        A string representing the site for which the average is to be calculated.

    Returns
    -------
    str
        The average of the site measurements to two decimal places or "NULL"
        if there are no measurements for the specified site.
    
    >>> calculate_site_average("A, 4.23, B, 6.77, Control, 7.10, B, 6.55, Control, 7.82, Control, 6.89, A, 3.93", "Control")
    7.27
    """

    # To Do: Complete the function
    split_measurements = measurements.replace(' ','').split(',')
    measurement_dict = {
        '' : {
            '' : 0,
        }
    }


    for i in range(1,len(split_measurements),2):
        if not split_measurements[i-1] in measurement_dict:
            measurement_dict[split_measurements[i-1]] = {
                'acc' : float(split_measurements[i]),
                'counter': 1
            }
        else:
            measurement_dict[split_measurements[i-1]]['acc'] += float(split_measurements[i])
            measurement_dict[split_measurements[i-1]]['counter'] += 1

    if site in measurement_dict:
        return str(round(measurement_dict[site]['acc'] / measurement_dict[site]['counter'], 2))
    else:
        return 'NULL'
    
def generate_summary(measurement_info, site):
    """
    (str, str) -> str
    
    Extract technician name and average of control
    site pH level measurements from string of technician measurements. 
    
    Parameters
    ----------
    measurement_info : str
        A string with the format "firstname.lastname@domain.com, date, sitename, measurement, sitename, measurement, ..."
    site : str
        A string representing the site for which the average is to be calculated.
    
    Returns
    -------
    str
        A string with the format "date,Lastname,Firstname,site,average pH of specified site

    >>> generate_summary("michael.scott@dundermifflin.com, 05/05/05, Chilis, 4.20, SchruteFarm, 6.71, Control, 7.11, SchruteFarm, 6.59, Control, 7.48, Control, 6.86, Chilis, 3.90", "Chilis")
    '05/05/05,Scott,Michael,Chilis,4.05'
    """
    
    # To Do: Complete the function
    split_info = measurement_info.replace(' ', '').split(',')
    name = extract_name_from_email(split_info[0])
    date = split_info[1]
    site_average = calculate_site_average(','.join(split_info[2:]), site)

    return date + ',' + name + ',' + site + ',' + site_average
