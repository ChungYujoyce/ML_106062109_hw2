#%%
import math
import operator
import random

def loadDataset(dataset, split, trainingSet=[], testSet=[]):
    newdata = []
    for x in range(len(dataset)-1):
        for i in range(0,len(dataset[x]),4):
            #print(dataset[x][i:i+3])
            if dataset[x][i] == "I":
                newdata.append(dataset[x][i:len(dataset[x])-1])
                break
            else:
                attribute = float(dataset[x][i:i+3])
                newdata.append(attribute)
            #print(type(newdata))
            #dataset = float(dataset[x, i: i+3])
        if x%50 < 30: # if random.random() < split:
            trainingSet.append(newdata)
            #print(trainingSet)
        else:
            testSet.append(newdata)
            #print(trainingSet)
        newdata=[]

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)
 
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
 
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1 
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]
 
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

def main():
    # preparing data
    #iris = datasets.load_iris()
    trainingSet=[]
    testSet=[]
    split = 0.67
    
    f = open('iris.data.txt', "r")
    lines = f.readlines()
    dataset = list(lines)
  
    loadDataset(dataset, split, trainingSet, testSet)
    
    print('Train set:' + repr(len(trainingSet)))
    print('Test set:' + repr(len(testSet)))
    # generate predictions
    predictions=[]
    print("Input the K:")
    k = int(input()) # user choose a number for the K_NN classifier
    print("---------------Iris dataset result:--------------")
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    
    print("Input which object you want to predict:")
    print("If you want to stop the prediction, please type \"-1\"when entering k's value, thank you~")
    while(1):
        print("Input the K:")
        k = int(input()) 
        if k == -1:
            break
        test_ob = [float(input()), float(input()), float(input()), float(input())]
        ob_result = ""
        print("-------------Here is your object predict result:-------------")
        ob_predictions=[]
        ob_neighbors = getNeighbors(trainingSet, test_ob, k)
        ob_result = getResponse(ob_neighbors)
        ob_predictions.append(ob_result)        
        print("The object is predicted as:", ob_result)
    
    print("thank you~")
main()