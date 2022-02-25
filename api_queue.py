class ApiArray:
    def __init__(self) -> None:
        
        self.api_elements = [1, 2, 3, 4, 5, 6]
        self.capacity = int(input('Enter the capacity you require:'))

    
    def enqueue(self):
        if self.length_api_elements() >= self.capacity:
            print(f'The api_elements queue{self.api_elements} is full')
            return f'Api_elements queue{self.api_elements} at capacity'
        else:
            api_value = int(input('Enter an API element:'))
            self.api_elements.append(api_value)
            print(f'The api_elements queue{self.api_elements}')
            return f'The added element into api_elements queue is:{api_value}'


    def dequeue(self):
        if self.length_api_elements == 0:
            print(f'Api elements queue{self.api_elements} is empty.')
        else:
            deleted_element = self.api_elements.pop(0)
            return f'The deleted element into api_elements queue is:{deleted_element}'


    def length_api_elements(self):
        return len(self.api_elements)


api = ApiArray()
length = api.enqueue()
dele = api.dequeue()
print(length)
print(dele)
