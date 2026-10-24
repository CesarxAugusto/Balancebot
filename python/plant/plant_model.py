import numpy as np
import math

# z = [x, d_x, theta, d_theta]
# params = [m_b, l, I_b, m_w, I_w, r, g]
def get_dynamics(z, tor, params):
    # unpacking the z and params
    x, d_x, theta, d_theta = z[0], z[1], z[2], z[3]
    m_b, l, I_b, m_w, I_w, r, g = params[0], params[1], params[2], params[3], params[4], params[5], params[6]

    #building the M matrix
    m_11 = m_w + m_b + (I_w/r**2)
    m_12 = m_b*l*math.cos(theta)
    m_21 = m_12
    m_22 = I_b + m_b*(l**2)
    m_matrix = np.array([[m_11, m_12], [m_21, m_22]])

    #building the F vector
    f1 = tor/r + m_b*l*(d_theta**2)*(math.sin(theta))
    f2 = tor + m_b*g*l*(math.sin(theta))
    f_vector = np.array([f1, f2])

    accels = np.linalg.solve(m_matrix, f_vector)
    dz = [d_x, accels[0], d_theta, accels[1]]

    return dz