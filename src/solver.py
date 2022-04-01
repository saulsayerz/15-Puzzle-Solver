# NAMA  : SAUL SAYERS
# NIM   : 13520094
# KELAS : K-01 STRATEGI ALGORITMA

# MERUPAKAN FILE ALGORITMA PUZZLESOLVER UNTUK TUCIL 3 STRATEGI ALGORITMA

import numpy as np
import os.path
from queue import PriorityQueue
import random

class Node:
    def __init__(self,prev,cost):
        self.prev = prev
        self.matrix = np.arange(16).reshape((4,4))
        self.cost = cost

    def generateMatrix(self) :
        numList = [i for i in range (16)]
        random.shuffle(numList)
        self.matrix = np.array(numList).reshape((4,4))

    def readFile(self):
        numList = []
        while True:
            filename = input("Input filename here (dengan .txt): ")
            path = "test/" + filename
            if (os.path.isfile(path)):
                break
            else :
                print("Filename doesnt exist! Please re-input filename.")
        file = open(path)
        for i in range(4) :
            numList.extend([int(number) for number in file.readline().split()])
        for i in range(len(numList)):
            if numList[i] == 16:
                numList[i] = 0
        self.matrix = np.array(numList).reshape((4,4))

    def printMatrix(self):
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
        result = np.where(self.matrix == 0)
        return (result[0][0] + result[1][0])%2

    def kurang_i(self):
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
        list = [i for i in range (1,16)]
        list.append(0)
        list = np.array(list).reshape((4,4))
        return (self.matrix==list).all()

    def countSyarat(self):
        return sum(self.kurang_i()) + self.locateBlank()

    def countCost(self):
        temp = self.matrix.flatten()
        count = 0
        for i in range(15) :
            if (temp[i] != (i+1)):
                count += 1
        if (temp[15] != 0) :
            count += 1
        return count

    def isSolvable(self) :
        if (self.countSyarat())%2 == 0:
            return True
        else:
            return False

    def moveBlankLeft(self) :
        result = np.where(self.matrix == 0)
        x = result[0][0] 
        y = result[1][0]
        hasil = self.matrix.copy()
        hasil[x,y-1] = self.matrix[x,y]
        hasil[x,y] = self.matrix[x,y-1]
        
        return hasil
    
    def moveBlankRight(self) :
        result = np.where(self.matrix == 0)
        x = result[0][0] 
        y = result[1][0]
        hasil = self.matrix.copy()
        hasil[x,y+1] = self.matrix[x,y]
        hasil[x,y] = self.matrix[x,y+1]
        return hasil
    
    def moveBlankUp(self) :
        result = np.where(self.matrix == 0)
        x = result[0][0] 
        y = result[1][0]
        hasil = self.matrix.copy()
        hasil[x-1,y] = self.matrix[x,y]
        hasil[x,y] = self.matrix[x-1,y]
        return hasil
    
    def moveBlankDown(self) :
        result = np.where(self.matrix == 0)
        x = result[0][0] 
        y = result[1][0]
        hasil = self.matrix.copy()
        hasil[x+1,y] = self.matrix[x,y]
        hasil[x,y] = self.matrix[x+1,y]
        return hasil

    def __lt__(self, other):
        return True

class Solver:
    def __init__(self):
        self.checked = []
        self.queue = PriorityQueue()
        self.mapMatrix = {}
        self.startMatrix = Node(["-"],0)
        self.solusi = Node(["-"],0)
    
    def start(self):
        self.startMatrix.readFile()
        self.startMatrix.cost = self.startMatrix.countCost()

    def bangkitkanSimpul(self):
        while True:
            node = self.queue.get()[1]
            self.checked.append(node)
            result = np.where(node.matrix == 0)
            x = result[0][0] 
            y = result[1][0]
            currMove = node.prev
            if node.isSolved():
                self.solusi = node
                break
            if (x != 0 and node.prev[len(node.prev)-1] != "DOWN"):
                newNode = Node(currMove + ["UP"] , len(node.prev))
                newNode.matrix = node.moveBlankUp()
                newNode.cost += newNode.countCost()
                if newNode.matrix.tobytes() not in self.mapMatrix.keys() :
                    self.mapMatrix[newNode.matrix.tobytes()] = True
                    self.queue.put((newNode.cost, newNode))
                    if newNode.isSolved():
                        self.solusi = newNode
                        break

            if (x != 3 and node.prev[len(node.prev)-1] != "UP"):
                newNode = Node(currMove + ["DOWN"],len(node.prev))
                newNode.matrix = node.moveBlankDown()
                newNode.cost += newNode.countCost()
                if newNode.matrix.tobytes() not in self.mapMatrix.keys() :
                    self.mapMatrix[newNode.matrix.tobytes()] = True
                    self.queue.put((newNode.cost, newNode))
                    if newNode.isSolved():
                        self.solusi = newNode
                        break

            if (y != 0 and node.prev[len(node.prev)-1] != "RIGHT"):
                newNode = Node(currMove + ["LEFT"],len(node.prev))
                newNode.matrix = node.moveBlankLeft()
                newNode.cost += newNode.countCost()
                if newNode.matrix.tobytes() not in self.mapMatrix.keys() :
                    self.mapMatrix[newNode.matrix.tobytes()] = True
                    self.queue.put((newNode.cost, newNode))
                    if newNode.isSolved():
                        self.solusi = newNode
                        break

            if (y != 3 and node.prev[len(node.prev)-1] != "LEFT"):
                newNode = Node(currMove + ["RIGHT"],len(node.prev))
                newNode.matrix = node.moveBlankRight()
                newNode.cost += newNode.countCost()
                if newNode.matrix.tobytes() not in self.mapMatrix.keys() :
                    self.mapMatrix[newNode.matrix.tobytes()] = True
                    self.queue.put((newNode.cost, newNode))
                    if newNode.isSolved():
                        self.solusi = newNode
                        break

    def cetakSolusi(self):
        print("\nSolusi sudah ditemukan!\n")

        print("Banyaknya simpul yang dibangkitkan:", self.queue.qsize() + len(self.checked))
        print("Banyak steps: ", len(self.solusi.prev) - 1 )
        temp = self.startMatrix
        for i in range (1,len(self.solusi.prev)):
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
        print("Matriks awalnya: ")
        self.startMatrix.printMatrix()

        print()
        print("Mencari tiap kurang(i): ")
        arr = self.startMatrix.kurang_i()
        for i in range (1,16):
            print("Kurang("+str(i) +") =", arr[i])
        print("Kurang(16) =",arr[0])
        print("Total sigma(i) =", sum(arr))
        print("X =", self.startMatrix.locateBlank())
        print("\nHasil Sigma kurang(i) + X:", self.startMatrix.countSyarat())

        if (not self.startMatrix.isSolvable()):
            print("Syarat bernilai ganjil, maka puzzle unsolvable.")
        else:
            print("Syarat bernilai genap, maka puzzle solvable.")
            self.queue.put((self.startMatrix.cost, self.startMatrix))
            self.mapMatrix[self.startMatrix.matrix.tobytes()] = True
            self.bangkitkanSimpul()