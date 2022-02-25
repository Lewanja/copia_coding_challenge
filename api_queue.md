# QUEUE API 

## EXERCISE

 *Write a python queue API using an array for storing elements. Your API should include a constructor method which takes as argument the initial capacity of the queue, enqueue and dequeue method, and a method which returns the number of elements stored. Implement dynamic resizing to support storing an arbitrarily large number of elements.*

 ### Solution

Python as an object oriented programming languages uses classes to perform tasks.
In this project,  APIArray class is defined with `api_elements` attribute to define the queue and `capacity` to define the size of the queue. An API short for Application programming interface, allows to programs to communicate to each other. The APIs of this program are enqueue and dequeue.

```python
class ApiArray:
    api_elements = [1, 2, 3, 4, 5, 6]
    capacity = int(input('Enter the capacity you require:'))
```

The constructor used `def __init__(self):` and objects defined `self.api_elements = [1, 2, 3, 4, 5, 6]` which defines the queue and `self.capacity = int(input('Enter the capacity you require:'))` which defines the length the queue should take.

```python
def __init__(self):
        
        self.api_elements = [1, 2, 3, 4, 5, 6]
        self.capacity = int(input('Enter the capacity you require:'))
```

`Enqueue()` function  adds items to a queue. It is similar to `item.append()` when working with lists. A value is added when the queue is not full. To check whether the list is at maximum capacity, an if statement is implemented.

```python
    if self.length_api_elements() >= self.capacity:
        print(f'The api_elements queue{self.api_elements} is full')
        return f'Api_elements queue{self.api_elements} at capacity'
    else:
        api_value = int(input('Enter an API element:'))
        self.api_elements.append(api_value)
        print(f'The api_elements queue{self.api_elements}')
        return api_value
```

Items are removed from the queue following **First In First Out(FIFO)** principle. An if statement is implemented to check whether the queue is empty. If the queue contains values `self.api_elements.pop(0)` removes first item in the list.

```python
    def dequeue(self):
        if self.length_api_elements == 0:
            print(f'Api elements queue{api_elements} is empty.')
        else:
            deleted_element = self.api_elements.pop(0)
            return deleted_element
```

To output the values of the queue, the function below is implemented

```python
    def length_api_elements(self):
        return len(self.api_elements)


api = ApiArray()
length = api.enqueue()
dele = api.dequeue()
print(length)
print(dele)
```

### To Run:

`python api_queue.py`

##### Expected output
When queue is below capacity:

```sh
Enter the capacity you require:7
Enter an API element:88
The api_elements queue[1, 2, 3, 4, 5, 6, 88]    
The added element into api_elements queue is:88 
The deleted element into api_elements queue is:1
```

When beyond capacity:

```sh
Enter the capacity you require:3
The api_elements queue[1, 2, 3, 4, 5, 6] is full
Api_elements queue[1, 2, 3, 4, 5, 6] at capacity
The deleted element into api_elements queue is:1
```
