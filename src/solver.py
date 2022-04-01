# NAMA  : SAUL SAYERS
# NIM   : 13520094
# KELAS : K-01 STRATEGI ALGORITMA

# MERUPAKAN FILE ALGORITMA PUZZLESOLVER UNTUK TUCIL 3 STRATEGI ALGORITMA

import numpy as np
import os.path
from queue import PriorityQueue
import random


class Node:      
    """ This class is what we use to represent the
        nodes in this program.

        Attributes:
            - prev (array of string) : list of the 
            moves to reach this node.
            - matrix (numpy 2d-array) : the matrix
            of integers where we store the puzzle.
            - cost (int) : the cost of the node.
    """    

    def __init__(self,prev,cost):
        """ Constructor of the Node Class

        Args:
            - prev (array of string) : list of the 
            moves to reach this node.
            - cost (int) : the cost of the node.
        """        

        self.prev = prev
        self.matrix = np.arange(16).reshape((4,4)) # To convert from a 1d array to a 2d numpy array
        self.cost = cost

    def generateMatrix(self) :
        """ this method is used to randomly 
            generate the matrix of the node.
        """        

        numList = [i for i in range (16)]
        random.shuffle(numList)
        self.matrix = np.array(numList).reshape((4,4)) # To convert from a 1d array to a 2d numpy array

    def readFile(self):
        """ This method is used to fill the matrix
            from an external txt file.
        """       

        numList = []
        while True:  # Looping until filename exists
            filename = input("Input filename here (dengan .txt): ")
            path = "test/" + filename
            if (os.path.isfile(path)):
                break
            else :
                print("Filename doesnt exist! Please re-input filename.")
        file = open(path)
        for i in range(4) :
            numList.extend([int(number) for number in file.readline().split()]) # Read each line and convert to int
        for i in range(len(numList)):
            if numList[i] == 16: # Handle if blank as 16 then change to 0
                numList[i] = 0
        self.matrix = np.array(numList).reshape((4,4)) # To convert from a 1d array to a 2d numpy array

    def printMatrix(self):
        """ This method is used to print 
            the matrix of the node.
        """       

        print("---------------------")
        for arr in self.matrix :
            for angka in arr :
                print("|",end="")
                if angka == 0 :
                    print("   ",end=" ")
                elif angka < 10 :
                    print(" ",angka,end=" ")
                else :
                    print("",angka,end=" ")
            print("|")
            print("---------------------")

    def locateBlank(self):
        """ This method is used to get
            the X of the matrix.

        Returns:
            int : the X of the matrix
        """     

        result = np.where(self.matrix == 0)
        return (result[0][0] + result[1][0])%2

    def kurang_i(self):
        """ This method is used to get
            the kurang(i) of the matrix

        Returns:
            array of integers : each index i of the
            array refers to the value of kurang(i).
        """       

        temp = self.matrix
        temp = temp.flatten()
        arr = [0 for i in range (16)]
        for i in range(len(temp)-1):
            count = 0 # Count untuk mendapatkan kurang_i untuk tiap i
            for j in range (i+1, len(temp)):
                if (temp[j] < temp[i] and temp[j] != 0) or (temp[i] == 0):
                    count += 1
            arr[temp[i]] = count
        return arr

    def isSolved(self):
        """ This method is used to check whether
            the matrix is in final state or not.

        Returns:
            boolean : True if matrix is solved,
            False if otherwise.
        """        

        list = [i for i in range (1,16)]
        list.append(0)
        list = np.array(list).reshape((4,4))
        return (self.matrix==list).all()

    def countSyarat(self):
        """ This method is used to count the condition 
            which is the sum of kurang(i) plus X.

        Returns:
            integer : the sum of kurang(i) + X
        """        
        return sum(self.kurang_i()) + self.locateBlank()

    def countCost(self):
        """ This method is used to count 
            the cost of the matrix.

        Returns:
            int : the cost of the matrix
        """      

        temp = self.matrix.flatten()
        count = 0
        for i in range(16) :
            if (temp[i] != (i+1) and temp[i] != 0):
                count += 1
        return count

    def isSolvable(self) :
        """ This method is used to check whether
            the puzzle is solveable or not.

        Returns:
            Boolean : If the condition is even then
            solvable so return True, False if otherwise
        """      

        if (self.countSyarat())%2 == 0:
            return True
        else:
            return False

    def moveBlankLeft(self) :
        """ This method is used to return a
            matrix where the blank is moved left

        Returns:
            numpy 2d-array : the matrix
            of integers where we store the puzzle.
        """      

        result = np.where(self.matrix == 0)
        x = result[0][0] 
        y = result[1][0]
        hasil = self.matrix.copy()
        hasil[x,y-1] = self.matrix[x,y]
        hasil[x,y] = self.matrix[x,y-1]
        
        return hasil
    
    def moveBlankRight(self) :
        """ This method is used to return a
            matrix where the blank is moved right

        Returns:
            numpy 2d-array : the matrix
            of integers where we store the puzzle.
        """      

        result = np.where(self.matrix == 0)
        x = result[0][0] 
        y = result[1][0]
        hasil = self.matrix.copy()
        hasil[x,y+1] = self.matrix[x,y]
        hasil[x,y] = self.matrix[x,y+1]
        return hasil
    
    def moveBlankUp(self) :
        """ This method is used to return a
            matrix where the blank is moved up

        Returns:
            numpy 2d-array : the matrix
            of integers where we store the puzzle.
        """     

        result = np.where(self.matrix == 0)
        x = result[0][0] 
        y = result[1][0]
        hasil = self.matrix.copy()
        hasil[x-1,y] = self.matrix[x,y]
        hasil[x,y] = self.matrix[x-1,y]
        return hasil
    
    def moveBlankDown(self) :
        """ This method is used to return a
            matrix where the blank is moved down

        Returns:
            numpy 2d-array : the matrix
            of integers where we store the puzzle.
        """     

        result = np.where(self.matrix == 0)
        x = result[0][0] 
        y = result[1][0]
        hasil = self.matrix.copy()
        hasil[x+1,y] = self.matrix[x,y]
        hasil[x,y] = self.matrix[x+1,y]
        return hasil

    def __lt__(self, other):
        """ Function overloading of the node
            for the lower than operator. Set to
            True so the newest node will be checked last.

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """        
        return False

class Solver:
    """ This class is what we use to contain
        the nodes and solve the puzzle

        Attributes:
        - checked (array): an array of nodes 
        where the nodes have been checked before
        - queue (prioqueue) : a prioqueue of nodes that
        haven't been checked and use the cost as the priority
        - mapMatrix (dictionary) : a hashmap to check whether
        the node has already been added or not
        - startMatrix (node) : the start of the puzzle or
        the root of the nodes.
        - solusi (node) : the node that is the solution
        to the puzzle.
    """

    def __init__(self):
        """ The constructor for the Solver.
        """        

        self.checked = []
        self.queue = PriorityQueue()
        self.mapMatrix = {}
        self.startMatrix = Node(["-"],0)
        self.solusi = Node(["-"],0)

    def bangkitkanSimpul(self):
        """ The looping part of the solver.
            Here, we continue to get the child
            nodes of the node most prioritized
            in the priority queue.

            For each child node we raise, we put them
            into the priorityqueue with it's cost as
            the priority.  
        """        

        while True:
            # Checking the current node.
            node = self.queue.get()[1]
            self.checked.append(node)
            result = np.where(node.matrix == 0)
            x = result[0][0] 
            y = result[1][0]
            currMove = node.prev
            if node.isSolved(): # If current node is solution, stop.
                self.solusi = node
                break

            # If blank is not at the top, then get the child
            # node where the blank moves up.
            if (x != 0 and node.prev[len(node.prev)-1] != "DOWN"):
                newNode = Node(currMove + ["UP"] , len(node.prev))
                newNode.matrix = node.moveBlankUp()
                newNode.cost += newNode.countCost()
                if newNode.matrix.tobytes() not in self.mapMatrix.keys() :
                    self.mapMatrix[newNode.matrix.tobytes()] = True
                    self.queue.put((newNode.cost, newNode))
                    if newNode.isSolved(): 
                        self.solusi = newNode # If child node is solution, stop.
                        break

            # If blank is not at the buttom, then get the child
            # node where the blank moves down.
            if (x != 3 and node.prev[len(node.prev)-1] != "UP"):
                newNode = Node(currMove + ["DOWN"],len(node.prev))
                newNode.matrix = node.moveBlankDown()
                newNode.cost += newNode.countCost()
                if newNode.matrix.tobytes() not in self.mapMatrix.keys() :
                    self.mapMatrix[newNode.matrix.tobytes()] = True
                    self.queue.put((newNode.cost, newNode))
                    if newNode.isSolved():
                        self.solusi = newNode # If child node is solution, stop.
                        break

            # If blank is not at the most left, then get the child
            # node where the blank moves left
            if (y != 0 and node.prev[len(node.prev)-1] != "RIGHT"):
                newNode = Node(currMove + ["LEFT"],len(node.prev))
                newNode.matrix = node.moveBlankLeft()
                newNode.cost += newNode.countCost()
                if newNode.matrix.tobytes() not in self.mapMatrix.keys() :
                    self.mapMatrix[newNode.matrix.tobytes()] = True
                    self.queue.put((newNode.cost, newNode))
                    if newNode.isSolved():
                        self.solusi = newNode # If child node is solution, stop.
                        break

            # If blank is not at the most right, then get the child
            # node where the blank moves right
            if (y != 3 and node.prev[len(node.prev)-1] != "LEFT"):
                newNode = Node(currMove + ["RIGHT"],len(node.prev))
                newNode.matrix = node.moveBlankRight()
                newNode.cost += newNode.countCost()
                if newNode.matrix.tobytes() not in self.mapMatrix.keys() :
                    self.mapMatrix[newNode.matrix.tobytes()] = True
                    self.queue.put((newNode.cost, newNode))
                    if newNode.isSolved():
                        self.solusi = newNode # If child node is solution, stop.
                        break

    def cetakSolusi(self):
        """ This method is used to print the amount of nodes raised,
            the amount of steps needed to get the solution,
            and print a matrix for each of the step.
        """        

        print("\nSolusi sudah ditemukan!\n")
        print("Banyaknya simpul yang dibangkitkan:", self.queue.qsize() + len(self.checked)) # nodes raised
        print("Banyak steps:", len(self.solusi.prev) - 1 ) # the amount of steps
        temp = self.startMatrix
        for i in range (1,len(self.solusi.prev)): # Move the matrix and print it for each step untill we get the solution
            print("Step ke-" + str(i) +": ")
            if (self.solusi.prev[i] == "RIGHT") :
                print("Command : Move blank right")
                temp.matrix = temp.moveBlankRight()
            if (self.solusi.prev[i] == "UP") :
                print("Command : Move blank up")
                temp.matrix = temp.moveBlankUp()
            if (self.solusi.prev[i] == "LEFT") :
                print("Command : Move blank left")
                temp.matrix = temp.moveBlankLeft()
            if (self.solusi.prev[i] == "DOWN") :
                print("Command : Move blank down")
                temp.matrix = temp.moveBlankDown()
            temp.printMatrix()
            print()
        print("Banyaknya simpul yang dibangkitkan:", self.queue.qsize() + len(self.checked))

    def solve(self):
        """ This method is used to initiate the solving process
            of the puzzle. This method will print the startmatrix,
            the kurang(i), and the X of the startMatrix, 
            then determine whether the puzzle is solvable or not. 

            If the startMatrix is unsolvable, then the method prints so.
            otherwise, the method will continue to the bangkitkanSimpul method.
        """        

        print("\nMatriks awalnya: ")
        self.startMatrix.printMatrix()
        print()
        print("Mencari tiap kurang(i): ")
        arr = self.startMatrix.kurang_i()
        for i in range (1,16):
            if i < 10 :
                print("Kurang("+str(i) +")  =", arr[i])
            else :
                print("Kurang("+str(i) +") =", arr[i])
        print("Kurang(16) =",arr[0])
        print("Total sigma(i) =", sum(arr))
        print("X =", self.startMatrix.locateBlank())
        print("\nHasil Sigma kurang(i) + X:", self.startMatrix.countSyarat())

        if (not self.startMatrix.isSolvable()):
            print("Syarat bernilai ganjil, maka puzzle unsolvable.")
        else:
            print("Syarat bernilai genap, maka puzzle solvable.")
            self.startMatrix.cost = self.startMatrix.countCost()
            self.queue.put((self.startMatrix.cost, self.startMatrix))
            self.mapMatrix[self.startMatrix.matrix.tobytes()] = True
            self.bangkitkanSimpul()