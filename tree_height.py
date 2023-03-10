# Egija Kokoreviča 	221RDB288

import sys
import threading



def compute_height(n, parents):
    root = None
    children = [[] for _ in range(n)]
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            children[parent].append(i)

    def get_height(node):
        if not children[node]:
            return 1
        else:
            return 1 + max(get_height(child) for child in children[node])

    return get_height(root)


    


def main():

    '''Printing answer'''

    ievade = input("Ievdi F vai I:")
    if "F" in ievade:
        file = input()

        if "a" in file:
            print("You can't use file names with letter 'a'")
            return
       
        try:
            with open ("test/"+file) as fp:
                n = int(fp.readline())
                parents = list(map(int, fp.readline().split()))

        except FileNotFoundError:
            print("Inprecision in the file name")
            return
       

    
       
            
    if "I" in ievade:  
        try:
                    
            n = int(input()) 
            parents = list(map(int, input().split()))

        except ValueError:
            print("Inprecision in input")
            return  

    print(compute_height(n, parents))




    
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

