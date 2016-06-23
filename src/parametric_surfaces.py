import numpy as np

class parametric_surface:
    """
    Contains a 'gallery' of parametric surfaces:

    - Boy's surface
    - Breathers surface
    """

    def breather(self, u, v, a = 2/5):
        """
        The breather surface:

        Does NOT work properly
        """
        denominator = (a * ((1 - a**2)*np.cosh(a*u)**2 + a**2*np.sin**2(np.sqrt(1-a**2)*v)))

        x = -u + ((1 - a**2) * np.cosh(a*u) * np.sinh(a*u)) / denominator
        y = (2*np.sqrt(1 - a**2)*np.cosh(a*u)*(-np.sqrt(1 - a**2)*np.cos(v)*np.cos(np.sqrt(1-a**2)*v) - np.sin(v)*np.sin(np.sqrt(1 - a**2)*v))) / denominator 
        z = (2*np.sqrt(1 - a**2)*np.cosh(a*u)*(-np.sqrt(1 - a**2)*np.sin(v)*np.cos(np.sqrt(1-a**2)*v) - np.cos(v)*np.sin(np.sqrt(1 - a**2)*v))) / denominator

        return (x, y, z)

    def trefoil(self, u, v, radius = 1):

        x = radius * np.sin(3*u) / (2 + np.cos(v))
        y = radius * (np.sin(u) + 2*np.sin(2*u)) / (2 + np.cos(v + np.pi*2 / 3))
        z = radius * 0.5 * (np.cos(u) - 2*np.cos(2*u)) * (2 + np.cos(v)) * (2 + np.cos(v + np.pi*2/3)) / 4

        return (x, y, z)

    def dini(self, u, v, a=1, b=0.2):
        """
        Dinis surface:
        u = [0, 4pi]
        v = (0, 2]
        """
        x = a * np.cos(u)*np.sin(v)
        y = a * np.sin(u)*np.sin(v)
        z = a * (np.cos(v) + np.log(np.tan(0.5*v))) + b*u

        return (x, y, z)

if __name__ == "__main__":
    test = parametric_surface()
    
    u_val = np.linspace(0, 4*np.pi, 100)
    v_val = np.linspace(0.001, 2, 100)
    for u in u_val:
        for v in v_val:
            print(test.dini(u, v))
