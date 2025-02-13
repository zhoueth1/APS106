import math 

def heater_hysteresis_thresh_controller(t_measured, curr_state, t_desired, alpha):
    """
    (float, bool, float, float) -> bool

    Determines the next state of the heater using hysteresis thresholding.

    Parameters
    ----------
    t_measured : float
        The latest measured temperature.
    curr_state : bool
        The current state of the heater (True for ON, False for OFF).
    t_desired : float
        The desired target temperature.
    alpha : float
        The hysteresis buffer range (+/- alpha) around the desired temperature.

    Returns
    -------
    bool
        The next state of the heater:
        - True: The heater should be ON.
        - False: The heater should be OFF.

    Notes
    -----
    The hysteresis threshold helps avoid rapid toggling of the heater by introducing
    a buffer around the desired temperature. The heater turns:
    - OFF when the current temperature is greater than or equal to `desired_temp + alpha`.
    - ON when the current temperature is less than or equal to `desired_temp - alpha`.

    Examples
    --------
    >>> heater_hysteresis_thresh_controller(33.2, True, 40.0, 5.0)
    True

    >>> heater_hysteresis_thresh_controller(28.4, True, 27.5, 1.0)
    True

    >>> heater_hysteresis_thresh_controller(50.6, True, 40.0, 10.0)
    False

    >>> heater_hysteresis_thresh_controller(30.8, False, 40.0, 2.9)
    True
    """
    if abs(t_measured - t_desired) <= alpha:
        return curr_state
    
    if t_measured < (t_desired - alpha):
        return True
    
    if t_measured > (t_desired + alpha):
        return False

def newton_raphson_sqrt(n, epsilon):
    """
    (float, float) -> float

    Compute the square root of a number using the Newton-Raphson method.

    Parameters
    ----------
    n : float
        The number to compute the square root of.
    epsilon : float
        The tolerance value for convergence.
    
    Returns
    -------
    float
        The approximate square root of the number `n`.
    
    Notes
    -----
    The Newton-Raphson method is an iterative method to find the roots of a function.
    The function returns the approximated value rounded to 3 decimal places.

    Examples
    --------
    >>> newton_raphson_sqrt(4.0, 0.001)
    2.0

    >>> newton_raphson_sqrt(2.0, 0.1)
    1.417
    """
    x_i = n

    while abs((x_i ** 2) - n) >= epsilon:
        x_i = (x_i + (n/x_i))/2
    
    return round(x_i,3)

def get_sensor_measurement(t, c0, c1, c2, c3, c4):
    """
    (float, float, float, float, float, float) -> float
    
    Simulates a sensor value reading based on a mathematical equation.

    Parameters
    ----------
    t : float
        The time parameter.
    c0 : float
        Coefficient for the linear term.
    c1 : float
        Coefficient for the square root term.
    c2 : float
        Coefficient for the sine term.
    c3 : float
        Coefficient for the cosine term with frequency 8t.
    c4 : float
        Constant offset.

    Returns
    -------
    float
        The simulated sensor value calculated using the formula:
        s(t) = c0 * t + c1 * sqrt(t) + c2 * sin(t) + c3 * cos(8t) + c4
        The returned value is rounded to 3 decimal points.
    """
    measurement = c0*t + c1*newton_raphson_sqrt(abs(t),0.0005) + c2*math.cos(t) + c3*math.sin(8*t) + c4
    return round(measurement,3)

def thresh_crossing_counter(temp_desired, hyst_alpha, t_start, t_stop, c0, c1, c2, c3, c4):
    """
    (float, float, float, float, float, float, float, float, float) -> int
    
    Counts the number of times a simulated sensor measurement crosses a 
    hysteresis threshold.

    Parameters
    ----------
    temp_desired : float
        The desired target temperature.
    get_sensor_measurement  hyst_alpha : float
        The hysteresis buffer range (+/- alpha) around the desired temperature.
    t_start : float
        The starting time for the simulation.
    t_stop : float
        The stopping time for the simulation.
    c0 : float
        Coefficient for the linear term in the sensor equation.
    c1 : float
        Coefficient for the square root term in the sensor equation.
    c2 : float
        Coefficient for the sine term in the sensor equation.
    c3 : float
        Coefficient for the cosine term with frequency 8t in the sensor equation.
    c4 : float
        Constant offset in the sensor equation.
    
    Returns
    -------
    int
        The number of times the sensor measurement crosses the hysteresis threshold.
    
    >>> thresh_crossing_counter(0.0, 0.2, 0.0, 10.01, -0.1, 2.0, 10.0, -5.0, -1.0)
    10
    """
    print(temp_desired, hyst_alpha, t_start, t_stop, c0, c1, c2, c3, c4)
    t_step = 0.01 # amount to increment the time after each sensor reading
    
    ## Initialize the state
    # To initialize, simply compare to the desired temperature because 
    # we don't yet know the current state to use the hysteresis threshold
    initial_temp = get_sensor_measurement(t_start,c0,c1,c2,c3,c4)
    state = initial_temp <= temp_desired
    print(initial_temp)
    
    # initialize the crossing counter
    cross_count = 0

    # start time counter
    t = t_start + t_step

    # To Do - Complete the function below
    while t < t_stop:
        curr_temp = get_sensor_measurement(t,c0,c1,c2,c3,c4)
        new_state = heater_hysteresis_thresh_controller(curr_temp,state,temp_desired,hyst_alpha)

        # print(curr_temp, temp_desired - hyst_alpha)
        if state != new_state:
            cross_count += 1

        state = new_state
        t += t_step
    
    return cross_count

print(thresh_crossing_counter(5.0, 1.0, 100.0, 210.01, 0.0, 0.0, 1.0, 0.0, 5.0))