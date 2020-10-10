from brain import Brain
from dqn import Dqn
import numpy as np 
import matplotlib.pyplot as plt

learningRate = 0.0001 
maxMemory = 60000
gamma = 0.9
batchSize = 32 
nLastStates = 4 

epsilon = 0.0002
minEpsilon = 0.05 

filepathToSave = 'model2.h5'

brain = Brain((20, 20, nLastStates), lr = learningRate)
model = brain.model

DQM = Dqn(maxMemory, gamma)

def resetStates():
    currentState = np.zeros((1,20,20, nLastStates))

    for i in range(nLastStates):
        currentState[0, :, : i] = # the initial state of the map

    return currentState, currentState

epoch = 0 
nCollected = 0 
maxNCollected = 0
totNCollected = 0 
scores = list() 

while True: 
    epoch += 1 
    env.reset()
    currentState, nextState = resetStates() 
    gameOver = False 
    while not gameOver: 
        if np.random.rand() <= epsilon: 
            action = np.random.randint(0,3)
        else: 
            qvalues = model.predict(currentState)[0]
            action = np.argmax(qvalues)
            
            frame, reward, gameOver = env.step(action)

            frame = np.reshape(frame, (1, 20, 20, 1))
            nextState = np.append(nextState, frame, axis = 3)
            nextState = np.delete(nextState, 0, axis = 3)

            DQN.remember([currentState, action, reward, nextState], gameOver)
            inputs, targets = DQN.getBatch(model, batchSize)
            model.train_on_batch(inputs, targets)

            if env.collected: 
                nCollected += 1 
            
            currentState = nextState 
        
        epsilon -= epsilonDecayRate
        epsilon = max(epsilon, minEpsilon) 

        if nCollected > maxNCollected and nCollected > 2: 
            model.save(filepathToSave)
            maxNCollected = nCollected 
        
        if epoch % 100 == 0 and epoch != 0: 
            scores.append(totNCollected / 100)
            totNCollected = 0 
            plt.plot(scores)
            plt.xlabel('Epoch / 100')
            plt.ylabel('Average Collected')
            plt.show()

        print('Epoch: ' + str(epoch) + ' Current Best: ' + str(maxNCollected) + 'Epsilon: {:.5f}'.format(epsilon))

