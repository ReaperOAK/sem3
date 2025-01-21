def sort_list(lst):
    return sorted(lst)

def enqueue(queue, item):
    queue.append(item)
    return queue

def dequeue(queue):
    if len(queue) == 0:
        return "Queue is empty"
    return queue.pop(0)

def display_queue(queue):
    return queue

def menu():
    print("Select operation:")
    print("1. Sort a list")
    print("2. Enqueue (Add to queue)")
    print("3. Dequeue (Remove from queue)")
    print("4. Display queue")
    print("5. Exit")

queue = []

while True:
    menu()
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '1':
        lst = list(map(int, input("Enter numbers separated by space: ").split()))
        sorted_lst = sort_list(lst)
        print(f"Sorted list: {sorted_lst}")
    elif choice == '2':
        item = int(input("Enter item to enqueue: "))
        queue = enqueue(queue, item)
        print(f"Queue after enqueue: {queue}")
    elif choice == '3':
        result = dequeue(queue)
        print(f"Dequeued item: {result}")
        print(f"Queue after dequeue: {queue}")
    elif choice == '4':
        print(f"Current queue: {display_queue(queue)}")
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter a valid choice.")