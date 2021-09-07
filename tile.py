# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 19:16:33 2021

@author: abhis
"""

class Tiles:    
    state_count=0
    def __init__(self,curr_state,parent,goal_state,path_cost,move,step,hflag):        
        
        self.curr_state=curr_state
        self.goal_state=goal_state
        self.parent=parent        
        self.gen_pathcost(parent,path_cost)
        self.move=move
        
        if hflag=="h1":                      
            self.heu_func_misplaced(curr_state,goal_state)
            
        elif hflag=="h2":
            self.heu_func_manhattan(curr_state,goal_state)
        elif hflag=="h3":
            self.heu_func_misplaced(curr_state,goal_state)
            h1=self.hvalue
            self.heu_func_manhattan(curr_state,goal_state)
            self.hvalue*=h1
        self.state=step
        self.hflag=hflag
        
    def print_puzzle(self): 
        print("Heuristic Value: ", self.hvalue)        
        print(self.curr_state[0:3])
        print(self.curr_state[3:6])
        print(self.curr_state[6:9])
        
    def check_puzzle(self):
        
        if self.curr_state==self.goal_state:
            print("Move is ",self.move)            
            return True
        return False
    
    def heu_func_manhattan(self,curr_state,goal_state):
        self.hvalue=0
        for i in range(1,9):
            dst=abs(self.curr_state.index(i)-self.goal_state.index(i))
            self.hvalue+=int(dst/3)+int(dst%3)
    
    def heu_func_misplaced(self,curr_state,goal_state):        
        count=0
        for i in range(0,9):
            if self.curr_state[i]!=self.goal_state[i] and self.curr_state[i]!=0:
                count=count+1
        
        self.hvalue=count        
    def gen_pathcost(self,parent,path_cost):
        if parent:
            self.path_cost= parent.path_cost+path_cost            
        else:
            self.path_cost=path_cost         
    
    def swap(self,successor,moves):
        index=self.curr_state.index(0)        
        step_no=self.state+1
        
        for dec in moves:
            
            next_state=self.curr_state.copy()
            if dec=='U':
                next_state[index], next_state[index-3] = next_state[index-3], next_state[index]
            elif dec=='D':
                next_state[index], next_state[index+3] = next_state[index+3], next_state[index]
           
            elif dec=='L':
                next_state[index], next_state[index-1] = next_state[index-1], next_state[index]
           
            elif dec=='R':
                next_state[index], next_state[index+1] = next_state[index+1], next_state[index]
            
            #checking if next_state  is solvable or not
            if self.inversion_check(next_state)%2==0:
                self.successor.append(Tiles(next_state,self,self.goal_state,1,dec,step_no,self.hflag))
        
        if self.parent:
            Tiles.state_count+=len(moves)-1    
        else:
            Tiles.state_count=1
    def correct_moves(self,rindex,cindex):
        moves=['L','R','U','D']
        if rindex==0:
            moves.remove('U')
        elif rindex==2:
            moves.remove('D')
        if cindex==0:
            moves.remove('L')
        elif cindex==2:
            moves.remove('R')
        return moves  
    
    def successors_curr_state(self):
        index_zero=self.curr_state.index(0)
        print("Move is ",self.move)        
        print("Zero at index",index_zero) 
        
        if self.state==0:
            print("Initial State")
        else:
            print("Child of state",self.state)
        
        self.print_puzzle()
        print()
        rindex=int(index_zero/3)
        cindex=int(index_zero%3)        
        
        self.successor=[]
        moves=self.correct_moves(rindex,cindex)       
         
        self.swap(self.successor,moves)
        return self.successor
    
    def inversion_check(self,curr_state):     
        inversion=0
        for i in range(1,8):
            for j in range(i+1,9):
                ci= curr_state.index(i)
                cj= curr_state.index(j)
                fi= self.goal_state.index(i)
                fj= self.goal_state.index(j)
                
                if (ci<cj and fi>fj) or (ci>cj and fi<fj):
                    inversion+=1
        return inversion