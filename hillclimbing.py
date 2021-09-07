  # -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 23:03:11 2021

@author: abhis
"""

from tile import Tiles
from time import time
import random

class Hill_Climbing:
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
    def solve(self,type_algo,heuristic):
        curr_state=Tiles(self.initial_state,None,self.goal_state,0,None,0,heuristic)
        goal_found=False
        path=[]
        path.append(curr_state.move)
        while goal_found==False:
            successors=curr_state.successors_curr_state()            
            
            if type_algo=="greedy":
                curr_state=self.greedy(curr_state,successors)          
            elif type_algo=="first":
                curr_state=self.first_succ(curr_state,successors)   
            elif type_algo=="stochastic":
                curr_state=curr_state=self.stochastic_random_walk(curr_state,successors)        
            
            if curr_state.path_cost<len(path):
                path[curr_state.path_cost]=curr_state.move
            else:
                path.append(curr_state.move)
            
            goal_found= curr_state.check_puzzle()
            
            if curr_state.hvalue==0:
                goal_found=True
        if goal_found:
            curr_state.print_puzzle()   
            print("\nOptimal path: ")
            for i in range(1,len(path)):                    
                if i==len(path)-1:
                    print(path[i])
                else:                        
                    print(path[i],"->",end=" ")
            print("Optimal Path Cost: ",curr_state.path_cost)        
            print("Total No of States checked are: ",Tiles.state_count)
            print("Total No of States to optimal path: ",curr_state.path_cost+1)  
        else:
            print("Goal not found")
            print("Total number of states explored before termination are ",Tiles.state_count)
    def greedy(self,curr_state,successors):
        best_successor=curr_state       
        
        for succ in successors:            
            if succ.hvalue < curr_state.hvalue:
                best_successor=succ                
        return best_successor
    
    def first_succ(self,curr_state,successors):
       
        for succ in successors:            
            if succ.hvalue < curr_state.hvalue:
                return succ                
        return curr_state
    
    def stochastic_random_walk(self,curr_state,successors):
        good_successors=[]
        best_hvalue=curr_state.hvalue
        for succ in successors:
            if succ.hvalue<best_hvalue:
                good_successors.append(succ)
        
        if len(good_successors)>0:
            random_succ = random.choice(good_successors)       
            return random_succ
        else:
            return curr_state
        
def main():
    with open("input.txt", "r") as f:    
    	
        data=f.read().split("\n\n\n")
        inp,goal = data[0],data[1]
        initial=[int(y) for x in inp.split("\n") for y in x.split(",")]
        goal=[int(y) for x in goal.split("\n") for y in x.split(",")]
    
    t0=time()
    hill=Hill_Climbing(initial,goal)
    hill.solve("first","h3")
    t1=time()-t0
    
    print("time taken by Hill Climbing is",t1)
if __name__=="__main__":
    main()
    