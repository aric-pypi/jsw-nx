def set():
    print('set nx.')

# each with index
def each(arr, fn):
    for i in range(len(arr)):
        fn(arr[i], i)