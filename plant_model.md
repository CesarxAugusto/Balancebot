# Assumptions
    1. Motion is in a vertical plane only. The robot balances and moves is in a
straight line only.
    2. The two wheels act as one equivalent wheel;
    3. The wheel rolls without slipping on flat ground and never leaves it;
    4. Body and wheel are rigid. Everything above the axle (chassis, battery, electronics, motors) is one body;
    5. No friction and no air drag;
    6. The motor is an ideal torque source;
    7. Gravity is constant;

# Sign Conventions
Here is a list of sign conventions that are important for this project:
x: the axle position, positive forward, measured from a reference mark x = 0;
θ: the tilt from vertical, positive when the body leans forward.
φ: the wheel's rotation angle, positive when the wheel rolls forward.
τ: the motor torque on the wheel, positive when it pushes the wheel in the forward-rolling direction.
Vertical heights are positive upward, measured from the axle.

# Parameters
m_b: body mass, in kg;
l: distance from the axle O of the body's center of mass, m;
I_b: body moment of inertia about its own center of mass, kgm²;
m_w: total mass of the wheel, in kg;
I_w: total moment of inertia of the wheels about the axle, kgm²;
r: wheels radius, in m;
g: gravitational acceleration, 9.81 in m/s²

# Degrees of freedom

The wheel angle is not independent, as with no slip φ = x/r. So two numbers locate everything: x and θ. 
z = [x, d_x, θ, d_θ]. 
input: τ.
