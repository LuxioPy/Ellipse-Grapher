import matplotlib.pyplot as plt # This imports the libary for plotting the graph
import math #imports the library for generating random numbers
import random # importing the libary for generating random numbers
import numpy as np #imports the library for numerical operations

#defines the function to plot the four points on the ellipse
def plot_ellipse(a, b):
      x = float(input("Enter x value: "))#gets x value from user
      if abs(x) > a:
        print("Error: x must between -a ")
      y = b * math.sqrt(1 - (x**2 / a**2))#finds y value from x and b
      y = -y #Reflects, the 
    
      plt.plot(x, y, 'ro')
      plt.annotate("({:.2f}, {:.2f})".format(x, y), (x, y))
      y = b * math.sqrt(1 - (x**2 / a**2))
      
      plt.plot(x, y, 'ro')
      plt.annotate("({:.2f}, {:.2f})".format(x, y), (x, y))
  
      x = 0
      y = b
      plt.plot(x, y, 'ro')
      plt.annotate("({:.2f}, {:.2f})".format(x, y), (x, y))
      y = -y
      plt.plot(x, y, 'ro')
      plt.annotate("({:.2f}, {:.2f})".format(x, y), (x, y))
  
      x = a
      y = 0
      plt.plot(x, y, 'ro')
      plt.annotate("({:.2f}, {:.2f})".format(x, y), (x, y))
      x = -x
      plt.plot(x, y, 'ro')
      plt.annotate("({:.2f}, {:.2f})".format(x, y), (x, y))
  

def main():
  while True:
      a = float(input("Enter a value: "))
      b = float(input("Enter a value: "))
      major_axis = max(a, b)
      minor_axis = min(a, b)
      
      foci = math.sqrt(major_axis**2 - minor_axis**2)
      plt.plot(foci, 0, 'bo')
      plt.annotate("({:.2f}, {:.2f})".format(foci, 0), (foci, 0))
      plt.plot(-foci, 0, 'bo')
      plt.annotate("({:.2f}, {:.2f})".format(-foci, 0), (-foci, 0))
      if a == b:
          print("Congrats! You made a circle")
      else:
          print("Major axis: ", major_axis)
          print("Minor axis: ", minor_axis)
      if b >= a:
        a, b = b, a
      e = math.sqrt(1 - (b**2 / a**2))
      print(f"Eccentricity: {e:.2f}")

      t = np.linspace(0, 2 * np.pi, 100)
      plt.plot(a * np.cos(t), b * np.sin(t))
      plt.axis('equal')
      plot_ellipse(a, b)
      plt.show()

if __name__ == '__main__':
    main()
