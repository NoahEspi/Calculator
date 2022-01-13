import cmath,math
def qf(a,b,c):
  try: 
    x1, x2 = (((((-b + math.sqrt((b**2) - (4 * a * c)))/(2 * a))))), (((((-b - math.sqrt((b**2) - (4 * a * c)))/(2 * a)))))
  except:
    x1, x2 = (((((-b + cmath.sqrt((b**2) - (4 * a * c)))/(2 * a))))), (((((-b - cmath.sqrt((b**2) - (4 * a * c)))/(2 * a)))))
  return x1,x2