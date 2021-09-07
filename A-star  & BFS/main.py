# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 19:08:16 2021

@author: abhis
"""
from tile import Tiles
from queue import PriorityQueue
from time import time

class Solution:
    def __init__(self,initial_state,goal_state):
        self.initial_state=initial_state
        self.goal_state=goal_state
        
        print("Start State: ")
        print(self.initial_state[0:3])
        print(self.initial_state[3:6])
        print(self.initial_state[6:9])
        
        print("Goal State: ")
        print(self.goal_state[0:3])
        print(self.goal_state[3:6])
        print(self.goal_state[6:9])    
                

                
    def BFS(self,heuristic):
        flag=0
        path=[]
        queue=PriorityQueue()
        initial_node=Tiles(self.initial_state,None,self.goal_state,0,None,0,heuristic)
        second_arg=0
        
        if initial_node.check_puzzle():
            print("Final Goal found by BFS")
            
        queue.put((initial_node.hvalue,second_arg,initial_node))
        
        visited=[]
        
        while not(queue.empty()):
            node=queue.get()
            node=node[2]
            visited.append(node.curr_state)
            
            if node.path_cost<len(path):
                path[node.path_cost]=node.move
            else:
                path.append(node.move)
            
            if node.check_puzzle():
                flag=1
                print("Final Goal found by BFS")              
                node.print_puzzle()   
                print("\nOptimal Path Cost: ",node.path_cost)
                print("Optimal path: ")
                for i in range(1,len(path)):                    
                    if i==len(path)-1:
                        print(path[i])
                    else:                        
                        print(path[i],"->",end=" ")
                    
                print("Total No of States checked are: ",Tiles.state_count)
                print("Total No of States to optimal path: ",node.path_cost+1)  
                return   
            successors=node.successors_curr_state()             
            for succ in successors:
                if succ.curr_state not in visited:
                    second_arg+=1                    
                    queue.put((succ.hvalue,second_arg,succ))          
        
        if queue.empty() and flag==0:
            print("Goal not found")
            print("Total number of states explored before termination are ",Tiles.state_count)
        return
    
    def A_star(self,heuristic):
        flag=0
        queue=PriorityQueue()
        initial_node=Tiles(self.initial_state,None,self.goal_state,0,None,0,heuristic)
        second_arg=0
        path=[]
        
        if initial_node.check_puzzle():
            print("Final Goal found by A-star")        
        
        f_of_n=initial_node.hvalue+initial_node.path_cost
        queue.put((f_of_n,second_arg,initial_node))
        visited=[]
        
        while not(queue.empty()):
            node=queue.get()            
            node=node[2]
            visited.append(node.curr_state)
           
            
            if node.path_cost<len(path):
                path[node.path_cost]=node.move
            else:
                path.append(node.move)
                
            if node.check_puzzle():
                flag=1
                print("Final Goal found by A-star")
                node.print_puzzle()                
                
                print("\nOptimal Path Cost: ",node.path_cost)                
                print("Optimal path: ")
                for i in range(1,len(path)):                    
                    if i==len(path)-1:
                        print(path[i])
                    else:                        
                        print(path[i],"->",end=" ")
                    
                print("Total No of States explored are: ",Tiles.state_count)
                print("Total No of States to optimal path: ",node.path_cost+1)  
                return    
            successors=node.successors_curr_state()           
            
            for succ in successors:
                if succ.curr_state not in visited:
                    second_arg+=1                    
                    f_of_n=succ.hvalue+succ.path_cost                    
                    queue.put((f_of_n,second_arg,succ))            
        
        if queue.empty() and flag==0:
            print("Goal not found")
            print("Total number of states explored before termination are ",Tiles.state_count)
        return
        
def main():
    initial=[1,2,3,5,6,0,7,8,4]
    goal=[1,2,3,5,8,6,0,7,4]
    
    algo=Solution(initial,goal)    
    
    #put "h1" for no of misplaced tiles hueristic function
    #put "h2" for manhattan distance
    
    
    
    print("\nBFS Algoritham")
    t0=time()
    algo.BFS("h2")
    t1=time()-t0
    print("time taken by BFS is",t1)
    
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    '''
    
    print("\nA-Star Algoritham")
    t0=time()
    algo.A_star("h2")
    t1=time()-t0
    print("time taken by A-star is",t1)
    ''' 

    
    
if __name__ =="__main__":    
    main()