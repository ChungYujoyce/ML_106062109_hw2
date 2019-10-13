# ML_Programming_Assignment_1
## K_NN Classifier implementation 
##### Using python
#### There are some functions:
### 1. Handle Data
* LoadDataSet
    1. load iris.data.txt file 
        * Since it's a string list, I have to consume the characters 3 at once and change it to float
        * str type can't do assignment
        * List type can't supply type change
    2. According to the train/test percentage, split the dataset 
        * A ratio of 60/40 is applied in this code 
        * However, a 67/33 for train/test is a standard ratio used
### 2. Similarity
* euclideanDistance
    1. Calculate the Euclidean Distance
        * Get the total number of numeric factors -> length
        * Use formula pow((a-b),2) and sum them up
        * Get the square root of the summation

### 3. Neighbors
* getNeighbors
    1. User input k
    2. Use aready exists euclideanDistance function to get the similarity from training instances and testing instances
        * All training_examples for using for one test_example
        * `distance.append` pairs of `(training_example[x], distance)`
        * `sort(key=operator.itemgetter(1))` will give: 
        A *function* that grabs the *index=1* item from a list-like object
        
    3. Get K closest neighbors and return then


### **4. Response** !!!
* getResponse
    1.  Allowing each neighbor to vote for their class attribute, and take the majority vote as the prediction.
        * Assumes that the class is the last attribite for each neighbor
        * 
        * In python3, use `dict.items()` instead of `dict.iteritems()`
    2. 

### 5. Accuracy
* getAccuracy
    1. Calculate the accuracy by comparing the predict results and actual results
        * Called "classification accuracy"
           
### 6. Main()
Problem 1:

 
Problem 2:

    1. print the number of trainset , testset 
    2. For each test case:
        1. Get all its neighbors distance
        2. Get the votes by its neighbors
        3. Do the prediction 
    3. Print the accuracy, number of wrong-predicted cases and correct-predicted cases