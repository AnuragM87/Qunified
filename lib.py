import numpy as np
class SingleQubitTomography:
    def __init__(self, Nh=0, Nv=0, Nl=0, Nd=0):
        self.Nh = Nh
        self.Nv = Nv
        self.Nl = Nl
        self.Nd = Nd
        self.Ph = 0
        self.Pl = 0
        self.Pd = 0
        self.Pv = 0
        self.S0=1
        self.S1=0
        self.S2=0
        self.S3=0
        self.rho=0
#setter and getter for requied values
#-----------------*********-----------------#
    # Getter and Setter for Nh, Nv, Nl, Nd
    def get_Nh(self):
        return self.Nh

    def set_Nh(self, Nh):
        self.Nh = Nh

    def get_Nv(self):
        return self.Nv

    def set_Nv(self, Nv):
        self.Nv = Nv

    def get_Nl(self):
        return self.Nl

    def set_Nl(self, Nl):
        self.Nl = Nl

    def get_Nd(self):
        return self.Nd

    def set_Nd(self, Nd):
        self.Nd = Nd

    # Getter and Setter for Probabilities (Ph, Pl, Pd, Pv)
    def set_Ph(self):
        self.Ph = self.Nh / self.Ntotal() if self.Ntotal() > 0 else 0

    def get_Ph(self):
        return self.Ph

    def set_Pl(self):
        self.Pl = self.Nl / self.Ntotal() if self.Ntotal() > 0 else 0

    def get_Pl(self):
        return self.Pl

    def set_Pd(self):
        self.Pd = self.Nd / self.Ntotal() if self.Ntotal() > 0 else 0

    def get_Pd(self):
        return self.Pd

    def set_Pv(self):
        self.Pv = self.Nv / self.Ntotal() if self.Ntotal() > 0 else 0

    def get_Pv(self):
        return self.Pv

    #setter getter for S0 , S1, S2, S3
    def set_S0(self,S0):
        self.S0=S0
    
    def get_S0(self):
        return self.S0
    
    def set_S1(self,S1):
        self.S1=S1
    
    def get_S1(self):
        return self.S1
    
    def set_S2(self,S2):
        self.S2=S2
    
    def get_S2(self):
        return self.S2
    
    def set_S3(self,S3):
        self.S3=S3
    
    def get_S3(self):
        return self.S3
    

    #set and get rho matrix
    def set_rho(self,rho):
        self.rho=rho
    
    def get_rho(self):
        return self.rho
    #-----------------*********-----------------#
    def inputData(self):
        print(f"Input Data: \nNh={self.get_Nh()}\nNv={self.get_Nv()}\nNl={self.get_Nl()}\nNd={self.get_Nd()}")

    def Ntotal(self):
        return self.Nh + self.Nv

    def probOfVectors(self):
        self.set_Ph()
        self.set_Pl()
        self.set_Pd()
        self.set_Pv()
        Ph = self.get_Ph()
        Pl = self.get_Pl()
        Pd = self.get_Pd()
        Pv = self.get_Pv()
        print(f"Probabilities:\nPh={Ph:.3f}\nPl={Pl:.3f}\nPd={Pd:.3f}\nPv={Pv:.3f}")
        return round(Ph, 3), round(Pl, 3), round(Pd, 3), round(Pv, 3)

    def setAllVectors(self):
        print("Enter the values for Nh, Nv, Nl, Nd")
        inputNh = int(input("Nh: "))
        inputNv = int(input("Nv: "))
        inputNl = int(input("Nl: "))
        inputNd = int(input("Nd: "))
        self.set_Nh(inputNh)
        self.set_Nv(inputNv)
        self.set_Nl(inputNl)
        self.set_Nd(inputNd)
        print("Values set successfully")

    def stokesVector(self):
        self.probOfVectors()
        values = [
            1,
            2 * self.Ph - 1,
            2 * self.Pl - 1,
            2 * self.Pd - 1
        ]
        matrix = np.array(values).reshape(-1, 1)
        return matrix
    
    def rhoMatrix(self,S):
        S0, S1, S2, S3 = S
        self.set_S0(S0)
        self.set_S1(S1)
        self.set_S2(S2)
        self.set_S3(S3)
        rho = 0.5 * np.array([
            [S0 + S3, S1 - 1j * S2],
            [S1 + 1j * S2, S0 - S3]
        ])
        self.set_rho(rho)
        return rho
    
    def expectation_S1(self):
        # Pauli-X matrix
        sigma_x = np.array([[0, 1],
                            [1, 0]])
        expectation = np.trace(np.dot(self.get_rho(), sigma_x))
        return np.real(expectation)  
    
    def expectation_S2(self):
        # Pauli-Y matrix
        sigma_y = np.array([[0, -1j],
                            [1j, 0]])
        expectation = np.trace(np.dot(self.get_rho(), sigma_y))
        return np.real(expectation)
    
    def expectation_S3(self):
        # Pauli-Z matrix
        sigma_z = np.array([[1, 0],
                            [0, -1]])
        expectation = np.trace(np.dot(self.get_rho(), sigma_z))
        return np.real(expectation)
    

class Normalization:
    def __init__(self,vector=None):
        self.vector=vector
        vector=self.enterVector()


    def enterVector(self):
        print("Enter the values for the vector")
        vector=np.array(float(x) for x in input().split())
        return vector
    
    def normalize(self, vector):
        return vector / np.linalg.norm()
    

class StateCheck:
    def __init__(self):
        pass:
        
