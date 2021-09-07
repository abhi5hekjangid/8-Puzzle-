# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 11:16:35 2021

@author: abhis
"""
import numpy as np
from tile import Tiles
from time import time
import random
import math

class Simulated_Annealing:
    def __init__(self,initial,goal):
        self.initial_state=initial
        self.goal_state=goal
        
        print("Start State: ")
        print(self.initial_state[0:3])
        print(self.initial_state[3:6])
        print(self.initial_state[6:9])
        
        print("Goal State: ")
        print(self.goal_state[0:3])
        print(self.goal_state[3:6])
        print(self.goal_state[6:9])  
        print()
    
    def solve(self,heuristic,Temp):
        curr_state=Tiles(self.initial_state,None,self.goal_state,0,None,0,heuristic)
        goal_found=False
        path=[]
        path.append(curr_state.move)
        
        
        while Temp>1:
            if goal_found  :
                break
            successors=curr_state.successors_curr_state() 
            
            if len(successors)>0:
                random_succ = random.choice(successors)     
            else:
                random_succ=curr_state
            
            delta_E=curr_state.hvalue-random_succ.hvalue
            
            Temp-=1
            
            if delta_E>0:
                curr_state=random_succ
            else:
                if math.exp(-delta_E/Temp)>random.uniform(0,1):
                    curr_state=random_succ          
            
            
            if curr_state.path_cost<len(path):
                path[curr_state.path_cost]=curr_state.move
            else:
                path.append(curr_state.move)
                
            goal_found= curr_state.check_puzzle()
            
            if curr_state.hvalue==0:
                goal_found=True
            
        
        if goal_found:
            curr_state.print_puzzle() 
            print("\nSub Optimal path: ")
            for i in range(1,len(path)):                    
                if i==len(path)-1:
                    print(path[i])
                else:                        
                    print(path[i],"->",end=" ")
            print("Sub Optimal Path Cost: ",curr_state.path_cost)        
            print("Total No of States checked are: ",Tiles.state_count)
            print("Total No of States to optimal path: ",curr_state.path_cost+1)  
        else:
            print("Goal not found")            
            print("Total number of states explored before termination are ",Tiles.state_count)
        
   
        
def main():
    
    #initial=[1,2,3,5,6,0,7,8,4]
    #goal=[1,2,3,5,8,6,0,7,4]
    
    with open("input.txt", "r") as f:    
    	
        data=f.read().split("\n\n\n")
        inp,goal = data[0],data[1]
        initial=[int(y) for x in inp.split("\n") for y in x.split(",")]
        goal=[int(y) for x in goal.split("\n") for y in x.split(",")]
        
        
    t0=time()
    algo=Simulated_Annealing(initial,goal)
    algo.solve("h2",1000)
    t1=time()-t0
    
    print("time taken by Simulated Annealing is",t1)
    
if __name__=="__main__":
    main()
    