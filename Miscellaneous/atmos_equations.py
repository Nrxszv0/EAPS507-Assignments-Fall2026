"""
Contains atmospheric equations
"""
# Load modules
import numpy as np
def potential_temperature(T,p):
    """
    Compute potential temperature for a specific temperature T
    Args:
        T: temperature in Kelvin (K)
        p: pressure in hPa
    Returns:
        theta: potential temperature in Kelvin
    """
    
    p_0 = 1000
    R_d = 287.05
    c_p = 1004
    # Calculate theta with equation
    theta = T * (p_0/p) ** (R_d/ c_p)
    return theta

def saturation_vapor_pressure(Tc):
    """
    Calculate the saturation vapor pressure given temperature
    Args:
        Tc: temperature in C
    Returns:
        e_s: saturation vapor pressure in hPa
    """
    # Calculate saturation vapor pressure with equation and return
    e_s = 6.112 * np.exp(17.67 * Tc / (Tc + 243.5))
    return e_s

def saturation_mixing_ratio(Tc,p):
    """
    Calculates saturation mixing ratio given temperature and pressure.
    Calls saturation_vapor_pressure() to get the saturation vapor pressure
    Args:
        Tc: temperature in C
        p: pressure in hPa
    Returns:
        w_s: saturation mixing ratio in (gkg^-1)
    """
    e = 0.622
    # Get saturation vapor pressure
    es = saturation_vapor_pressure(Tc)
    # Calculate saturation mixing ratio with equation and return
    ws = e * es / (p - es)
    # Convert to g/kg
    ws *= 1000
    return ws


def hypsometric_thickness(Tv, p1, p2):
    """
    Calculates layer thickness given layer-mean virtual temperature, lower-level pressure, an upper-level pressure.
    Args:
        Tv: layer-mean virtual temperature in K
        p1: lower-level pressure in hPa
        p2: upper-level pressure in hPa
    Returns:
        z1_z2: layer thickness in meters
    """
    Rd = 287.05
    g = 9.80665
    # Calculate layer thickness and return
    z2_z1 = (Rd * Tv / g) * np.log(p1 / p2)
    return z2_z1

def geostrophic_wind(dZdx, dZdy, latitude):
    """
    Calculates geostrophic wind components given rate of change of latitude with respect to x and y and current latitude
    Args:
        dZdx: rate of change of height with respect to x
        dZdy: rate of change of height with respect to y
        latitude: latitude
    Returns:
        ug, vg: geostrophic wind components
    """
    omega = 7.2921
    g = 9.80665
    # Compute Coriolis parameter
    f = 2 * omega * np.sin(latitude)
    # Compute geostrophic wind components with the equations
    ug = - (g/f) * dZdy
    vg = (g/f) * dZdx
    return ug,vg