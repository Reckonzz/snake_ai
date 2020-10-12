import numpy as np

class Simulate_snake():
    def __init__(self,waitTime): 
        self.nrows = 10 
        self.ncols = 10
        self.snake_len_start = 2
        self.snake_pos = list()
        self.direction = (1,0)

        self.defReward = -0.3
        self.neg_reward = -100
        self.pos_reward = 10 
        self.lastMove = 0
        self.game_over = False
        self.collected = False

        grid_start = np.zeros((self.nrows, self.ncols))    

        row_mid, col_mid = self.nrows//2-1 , self.ncols//2-1
        for i in range(self.snake_len_start): 
            self.snake_pos.append((col_mid+i, row_mid))
            grid_start[row_mid][col_mid+i] = 1

        self.grid = grid_start
        self.food_pos = self.spawn_food()
        
    def spawn_food(self):
        posx = np.random.randint(0, self.ncols)
        posy = np.random.randint(0, self.nrows)

        while self.grid[posy][posx] == 1:
            posx = np.random.randint(0, self.ncols)
            posy = np.random.randint(0, self.nrows)
        
        self.grid[posy][posx] = 2
        
        return (posx, posy)

    def move_snake(self,next_pos,collected_food):
        self.snake_pos.insert(0, next_pos)

        if not collected_food: 
            self.snake_pos.pop()
        
        # if collected_food: 
        #     print(self.grid)

        self.grid = np.zeros((self.nrows, self.ncols))
        
        for coord in self.snake_pos: 
            x,y = coord 
            self.grid[y][x] = 1 

        if collected_food:
            self.collected = True
            # print("I collected food!!!")
            # x = input("Continue?")
            # print(self.grid)
            self.food_pos = self.spawn_food()
            
        self.grid[self.food_pos[1]][self.food_pos[0]] = 2    
    
    def step(self,action):
        # action = 0 -> left 
        # action = 1 -> right
        # action = 2 -> up
        # action = 3 -> down
        direction = [(-1,0),(1,0),(0,1),(0,-1)]
        self.collected = False 
        reward = self.defReward

        movex, movey = direction[action]

        movex, movey = direction[action]
        if movex and self.direction[0]: 
            movex, movey = self.direction
        if movey and self.direction[1]: 
            movex, movey = self.direction

        self.direction = (movex,movey)

        snake_headx, snake_heady = self.snake_pos[0]  
        
        new_posx, new_posy = snake_headx + movex, snake_heady + movey

        if new_posx < 0 or new_posy <0 or new_posx == self.ncols or new_posy == self.nrows: 
            self.game_over = True 
            reward = self.neg_reward
        elif self.grid[new_posy][new_posx] == 2: 
            reward = self.pos_reward
            self.move_snake((new_posx,new_posy), True)
        else: 
            self.move_snake((new_posx,new_posy), False)

        return self.grid, reward, self.game_over 

    def reset(self): 
        self.grid = np.zeros((self.nrows, self.ncols))
        self.snake_pos = list()

        row_mid, col_mid = self.nrows//2-1 , self.ncols//2-1
        for i in range(self.snake_len_start): 
            self.snake_pos.append((col_mid+i, row_mid))
            self.grid[row_mid][col_mid+i] = 1

        foodx, foody = self.spawn_food()
        self.grid[foody][foodx] = 2

        self.game_over = False 
        

if __name__ == "__main__": 
    game = Simulate_snake(100)
    while(not game.game_over): 
        next_move = input("What is your next move")
        if next_move == "reset": 
            game.reset()
            continue
        else: 
            next_move = int(next_move)
        game.step(next_move)       
        


# class Environment():
    
#     def __init__(self, waitTime):
        
#         self.width = 880
#         self.height = 880
#         self.nRows = 10
#         self.nColumns = 10
#         self.initSnakeLen = 2
#         self.defReward = -0.03
#         self.neg_reward = -1.
#         self.pos_reward = 2.
#         self.waitTime = waitTime
    
        
#     def step(self, action):
#         # action = 0 -> up
#         # action = 1 -> down
#         # action = 2 -> right
#         # action = 3 -> left
#         gameOver = False
#         reward = self.defReward
#         self.collected = False
        
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 return
        
#         snakeX = self.snakePos[0][1]
#         snakeY = self.snakePos[0][0]
        
#         if action == 1 and self.lastMove == 0:
#             action = 0
#         if action == 0 and self.lastMove == 1:
#             action = 1
#         if action == 3 and self.lastMove == 2:
#             action = 2
#         if action == 2 and self.lastMove == 3:
#             action = 3
        
#         if action == 0:
#             if snakeY > 0:
#                 if self.screenMap[snakeY - 1][snakeX] == 0.5:
#                     gameOver = True
#                     reward = self.neg_reward
#                 elif self.screenMap[snakeY - 1][snakeX] == 1:
#                     reward = self.pos_reward
#                     self.moveSnake((snakeY - 1, snakeX), True)
#                 elif self.screenMap[snakeY - 1][snakeX] == 0:
#                     self.moveSnake((snakeY - 1, snakeX), False)
#             else:
#                 gameOver = True
#                 reward = self.neg_reward
                
#         elif action == 1:
#             if snakeY < self.nRows - 1:
#                 if self.screenMap[snakeY + 1][snakeX] == 0.5:
#                     gameOver = True
#                     reward = self.neg_reward
#                 elif self.screenMap[snakeY + 1][snakeX] == 1:
#                     reward = self.pos_reward
#                     self.moveSnake((snakeY + 1, snakeX), True)
#                 elif self.screenMap[snakeY + 1][snakeX] == 0:
#                     self.moveSnake((snakeY + 1, snakeX), False)
#             else:
#                 gameOver = True
#                 reward = self.neg_reward
                
#         elif action == 2:
#             if snakeX < self.nColumns - 1:
#                 if self.screenMap[snakeY][snakeX + 1] == 0.5:
#                     gameOver = True
#                     reward = self.neg_reward
#                 elif self.screenMap[snakeY][snakeX + 1] == 1:
#                     reward = self.pos_reward
#                     self.moveSnake((snakeY, snakeX + 1), True)
#                 elif self.screenMap[snakeY][snakeX + 1] == 0:
#                     self.moveSnake((snakeY, snakeX + 1), False)
#             else:
#                 gameOver = True
#                 reward = self.neg_reward 
        
#         elif action == 3:
#             if snakeX > 0:
#                 if self.screenMap[snakeY][snakeX - 1] == 0.5:
#                     gameOver = True
#                     reward = self.neg_reward
#                 elif self.screenMap[snakeY][snakeX - 1] == 1:
#                     reward = self.pos_reward
#                     self.moveSnake((snakeY, snakeX - 1), True)
#                 elif self.screenMap[snakeY][snakeX - 1] == 0:
#                     self.moveSnake((snakeY, snakeX - 1), False)
#             else:
#                 gameOver = True
#                 reward = self.neg_reward
                
#         self.drawScreen()
        
#         self.lastMove = action
        
#         pg.time.wait(self.waitTime)
        
#         return self.screenMap, reward, gameOver
            
            
#     def reset(self):
#         self.screenMap  = np.zeros((self.nRows, self.nColumns))
#         self.snakePos = list()
        
#         for i in range(self.initSnakeLen):
#             self.snakePos.append((int(self.nRows / 2) + i, int(self.nColumns / 2)))
#             self.screenMap[int(self.nRows / 2) + i][int(self.nColumns / 2)] = 0.5
        
#         self.screenMap[self.applePos[0]][self.applePos[1]] = 1
        
#         self.lastMove = 0
        
#         self.drawScreen()

# if __name__ == '__main__':
#      env = Environment(100)
#      gameOver = False
#      start = False
#      action = 0
#      while True:
#           for event in pg.event.get():
#                if event.type == pg.KEYDOWN:
#                     if event.key == pg.K_SPACE and not start:
#                          start = True
#                     elif event.key == pg.K_SPACE and start:
#                          start = False
#                     if event.key == pg.K_UP:
#                          action = 0
#                     elif event.key == pg.K_DOWN:
#                          action = 1
#                     elif event.key == pg.K_RIGHT:
#                          action = 2
#                     elif event.key == pg.K_LEFT:
#                          action = 3
          
#           if start:
#                _, _, gameOver = env.step(action)
               
#           if gameOver:
#                start = False
#                gameOver = False
#                env.reset()
#                action = 0
               
              
