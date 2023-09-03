import math

class Circle:
    def  __init__(self,radius):
         self.radius =radius
        
    def Accept(self):
    
        self.radius=float(input("Enter the redius:"))
      
    def CalculateArea(self):
        return math.pi * self.radius ** 2
  
    def CalculateCircumference(self):
     
        return 2 * math.pi * self.radius
    

def main():

    circle = Circle(0)
    circle.Accept()
    area= circle.CalculateArea()
    circumference =circle.CalculateCircumference()
    print(f"Radius: {circle.radius}")
    print(f"Area: {area:.2f}")
    print(f"Circumference: {circumference:.2f}")
    

if __name__=="__main__":
    main()