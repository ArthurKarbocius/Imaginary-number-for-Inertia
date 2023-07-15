#<<<<<<<<<<< Discrete method to solve time tau of elastic spring contraction / expansion when objects initial vleocity is v0 >>>>>>>>>>>>>
import math

# Total iteration number:
N = 10**5
# Object's mass [kg]:
m = 3.5
# Spring's elasticity coefficient [N/m]:
k = 1500
# Maximum spring contraction distance [m]:
x = 0.3
# Spring contraction change distance [m]:
delta = x / N 
# Maximum object's velocity [m/s]:
v0 = x * (k / m)**(1/2)
# Initial velocity and time:
vn = v0
tn_sum = 0

for n in range(N):

# Spring's potential energy at every n step [J]:
        Un = n * k * delta**2 / 2
# Objects's kinetic energy at every n step [J]:       
        Kn = m * vn**2 / 2 - Un
# Total systems energy at every n step [J]:             
        En = Kn - Un
# Object's velocity change at every n step [m/s]:  
        vn = (2 * En / m)**(1/2)
# Time change at every n step and totat time tau, [s]:       
        tn = delta / vn
        tn_sum += tn

if tn_sum == tn_sum:
    print("Discrete sumation tau =", tn_sum ,"seconds")
    print("Integration based tau =", math.pi/2 * (m / k)**(1/2) ,"seconds")
    print()

##<<<<<<<<<<<<<< Discrete method to solve time tau of projectile under influence of gravity force when projectile shot perpendicular to the ground with initial vleocity v0 >>>>>>>>>>>>>

# Total iteration number:
N = 10**5
# Object's mass [kg]:
m = 3.5
# Initial projectile velocity [m/s]:
v0 = 7.672027112
# Free fall accelaration constant, [m/s^2]:
g = 9.81
# Maximum projectile's reach height [m]:
# For v0 =7.672027112 m/s, therefore h =3 m:
h = v0**2 / (2 * g)
# Objects's intial kinetic energy [J]:       
K0 = m * v0**2 / 2
# Minimum distance change [m]:
delta = h / N 
# Initial velocity and time:
vn = v0
Kn = K0
tn_sum = 0

for n in range(N):

# Projectile's potential energy change at every n step [J]:
        Un = m * g * n * delta
# Projectile's kinetic energy change at every n step [J]:       
        Kn = K0 - Un
# Projectile's velocity change at every n step [m/s]:  
        vn = (2 * Kn / m)**(1/2)
# Time change at every n step and total time tau, [s]:       
        tn = delta / vn
        tn_sum += tn

if tn_sum == tn_sum:
    print("Gravity discrete sumation tau =", tn_sum ,"seconds")
    print("Gravity integration based tau =", (2 * h / g)**(1/2) ,"seconds")



## From non-dimensional a=[0, 1] coefficient change:
tau = (2 * h / g)**(1/2)

a = 2/3

t = tau * a
v = v0 * (1 - a)
y = h * a * (2 - a)

print("time =", round(t, 4),"s")
print("velocity =", round(v, 2) ,"m/s")
print("height =", round(y, 3) ,"m")















