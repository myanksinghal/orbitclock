
import os
import random
from PIL import Image, ImageDraw, ImageFont

import datetime

# Setting #################################################################

# Setting 1: Kindle resolution
res_x = 1448
res_y = 1072

# Setting 2: Clock location
clockx = res_x/2 - 250
clocky = res_y/2 - 120

#Setting 3: Bodies Mass
mass1 = 9.0
mass2 = 5.0
mass3 = 12.0
# Gravitational constant
G = 300
dt = 1

# Setting ##############################################################

if 'pos_vel.txt' not in os.listdir('.'):
    body1_x, body1_y = res_x * random.random(), res_y * random.random()
    body2_x, body2_y = res_x * random.random(), res_y * random.random()
    body3_x, body3_y = res_x * random.random(), res_y * random.random()
    body1_x_vel, body1_y_vel = (random.random()-0.5)*2, (random.random()-0.5)*2
    body2_x_vel, body2_y_vel = (random.random()-0.5)*2, (random.random()-0.5)*2
    body3_x_vel, body3_y_vel = (random.random()-0.5)*2, (random.random()-0.5)*2

else:
    with open('pos_vel.txt', 'r') as f:
        lines = f.readlines()
        body1_x, body1_y = float(lines[0]), float(lines[1])
        body2_x, body2_y = float(lines[2]), float(lines[3])
        body3_x, body3_y = float(lines[4]), float(lines[5])
        body1_x_vel, body1_y_vel = float(lines[6]), float(lines[7])
        body2_x_vel, body2_y_vel = float(lines[8]), float(lines[9])
        body3_x_vel, body3_y_vel = float(lines[10]), float(lines[11])



# Calculate forces for all body pairs
def calculate_force(x1, y1, x2, y2, m1, m2):
    dx = x2 - x1
    dy = y2 - y1
    distance = (dx**2 + dy**2)**0.5
    force = G * m1 * m2 / (distance**2 + 1e-3)
    return force * dx / (distance + 1e-3), force * dy / (distance + 1e-3)

# Body 1
ax1, ay1 = calculate_force(body1_x, body1_y, body2_x, body2_y, mass1, mass2)
ax1_3, ay1_3 = calculate_force(body1_x, body1_y, body3_x, body3_y, mass1, mass3)
# Attraction to clock center
clock_dx = res_x/2 - body1_x
clock_dy = res_y/2 - body1_y
clock_dist = (clock_dx**2 + clock_dy**2)**0.5 + 1e-5
clock_force =  clock_dist / (clock_dist**2 + 100)
ax1_clock = clock_force * clock_dx / clock_dist
ay1_clock = clock_force * clock_dy / clock_dist
body1_x_vel += (ax1 + ax1_3 + ax1_clock) * dt / mass1
body1_y_vel += (ay1 + ay1_3 + ay1_clock) * dt / mass1

# Body 2
ax2, ay2 = calculate_force(body2_x, body2_y, body1_x, body1_y, mass2, mass1)
ax2_3, ay2_3 = calculate_force(body2_x, body2_y, body3_x, body3_y, mass2, mass3)
clock_dx = res_x/2 - body2_x
clock_dy = res_y/2 - body2_y
clock_dist = (clock_dx**2 + clock_dy**2)**0.5 + 1e-5
clock_force =  clock_dist / (clock_dist**2 + 100)
ax2_clock = clock_force * clock_dx / clock_dist
ay2_clock = clock_force * clock_dy / clock_dist
body2_x_vel += (ax2 + ax2_3 + ax2_clock) * dt / mass2
body2_y_vel += (ay2 + ay2_3 + ay2_clock) * dt / mass2

# Body 3
ax3, ay3 = calculate_force(body3_x, body3_y, body1_x, body1_y, mass3, mass1)
ax3_2, ay3_2 = calculate_force(body3_x, body3_y, body2_x, body2_y, mass3, mass2)
clock_dx = res_x/2 - body3_x
clock_dy = res_y/2 - body3_y
clock_dist = (clock_dx**2 + clock_dy**2)**0.5 + 1e-5
clock_force =  clock_dist / (clock_dist**2 + 100)
ax3_clock = clock_force * clock_dx / clock_dist
ay3_clock = clock_force * clock_dy / clock_dist
body3_x_vel += (ax3 + ax3_2 + ax3_clock) * dt / mass3
body3_y_vel += (ay3 + ay3_2 + ay3_clock) * dt / mass3

# Update positions
body1_x += body1_x_vel * dt
body1_y += body1_y_vel * dt
body2_x += body2_x_vel * dt
body2_y += body2_y_vel * dt
body3_x += body3_x_vel * dt
body3_y += body3_y_vel * dt

# Save updated positions and velocities
with open('pos_vel.txt', 'w') as f:
    f.write(f"{body1_x}\n{body1_y}\n{body2_x}\n{body2_y}\n{body3_x}\n{body3_y}\n")
    f.write(f"{body1_x_vel}\n{body1_y_vel}\n{body2_x_vel}\n{body2_y_vel}\n{body3_x_vel}\n{body3_y_vel}\n")

    # Check if any body is 1.5 times out of bounds
if (body1_x > res_x * 1.5 or body1_y > res_y * 1.5 or
    body2_x > res_x * 1.5 or body2_y > res_y * 1.5 or
    body3_x > res_x * 1.5 or body3_y > res_y * 1.5):
    if os.path.exists('pos_vel.txt'):
        os.remove('pos_vel.txt')

# Check if 2 or more bodies are out of bounds
out_of_bounds_count = 0
if body1_x > res_x or body1_y > res_y:
    out_of_bounds_count += 1
if body2_x > res_x or body2_y > res_y:
    out_of_bounds_count += 1
if body3_x > res_x or body3_y > res_y:
    out_of_bounds_count += 1

if out_of_bounds_count >= 2:
    if os.path.exists('pos_vel.txt'):
        os.remove('pos_vel.txt')

body1_radius = mass1 * 2
body2_radius = mass2 * 2
body3_radius = mass3 *2
rgb_black = (0, 0, 0)

# Create black background
image = Image.new('RGB', (res_x, res_y), rgb_black)

draw = ImageDraw.Draw(image)

# Draw bodies
draw.ellipse([body1_x - body1_radius, body1_y - body1_radius, 
              body1_x + body1_radius, body1_y + body1_radius], 
             fill=(255, 255, 255))
draw.ellipse([body2_x - body2_radius, body2_y - body2_radius, 
              body2_x + body2_radius, body2_y + body2_radius], 
             fill=(255, 255, 255))
draw.ellipse([body3_x - body3_radius, body3_y - body3_radius, 
              body3_x + body3_radius, body3_y + body3_radius], 
             fill=(255, 255, 255))


# Drawing clock face --------------------------

rgb_white = (255,255,255)
# Loading font 
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("futura medium bt.ttf", 52)
font_large = ImageFont.truetype("futura medium bt.ttf", 180)

datetime.datetime.now()

# Generating clock overlay ------------------------
# Generating texts
current_time = datetime.datetime.now()
clock_str = str(current_time)[11:16]
date_str = current_time.strftime("%Y %b. %d")

draw.text((clockx, clocky), clock_str, fill=rgb_white, font=font_large)
draw.text((clockx+156, clocky+192), date_str, fill=rgb_white, font=font)


# Saving image
#image = image.transpose(Image.ROTATE_90)
image.convert("L").save('time_latest.png', format='PNG')