import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


x_cords = [0]
y_cords = [0]

def cord_transformation(x,y):
    #this function inputs x,y coordinates and randomly chooses the transformation based on the probabilty we give them, and then outputs the transformed coordinates.
    rand = np.random.rand()
    if rand <= 1/100:
        x_out, y_out = 0, 0.16*y
    elif rand > 1/100 and rand <= 86/100:
        x_out, y_out = 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
    elif rand > 86/100 and rand <= 93/100:
        x_out, y_out = 0.2*x - 0.26*y, 0.23*x + 0.22*y+1.6
    else:
        x_out, y_out = -0.15*x + 0.28*y -0.028, 0.26*x + 0.24*y +1.05
    x_cords.append(x_out)
    y_cords.append(y_out)

    return x_out, y_out 
for i in range(100000):
    cord_transformation(x_cords[i],y_cords[i])

# x_cords ,y_cords = x_cords[::100], y_cords[::100]
#Video
#Define the Video parameters
frames = round(15000/1)


# init the figure & size for 2D
fig, ax = plt.subplots(figsize = (7,7)) 


#Main function, plots a new plot for every itteration
def update_2D(i):
    ax.clear()
    ax.scatter(x_cords[:i*100], y_cords[:i*100], label ="Generation: {}".format(i*100), s = 1)
    ax.set_title('leaf live drawing')
    ax.legend()


ani = animation.FuncAnimation(fig, update_2D, frames=frames, interval=0.01)
#ani.save('live leaf drawing2.gif', writer='pillow')
plt.show()

plt.scatter(x_cords,y_cords, s=0.15)
ax.set_title('leaf live drawing', fontsize=18)
#plt.xticks(fontsize=15)
#plt.yticks(fontsize=15)
#plt.savefig('leaf live drawing2.png')
plt.show()