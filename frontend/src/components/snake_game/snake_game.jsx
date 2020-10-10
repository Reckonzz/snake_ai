import React from "react"

import Board from "./board/board"
import Panel from "./panel/panel"

import "./snake_game.styles.scss"

class SnakeGame extends React.Component{
    constructor(props){
        super(props)
        this.snakeSpeed = 150
        this.dimension = 15
        //setting up the grid based on the dimension
        let squares = Array(this.dimension).fill().map(()=>Array(this.dimension).fill(0))

        //set snake to start in the middle 
        let mid = Math.floor(this.dimension/2) 
        let snake_starting_pos = [[mid,mid],[mid-1,mid]]

        //generate the snake
        snake_starting_pos.forEach(el => {
            squares[el[1]][el[0]] = 1
        })

        this.state = {
            squares: squares,
            snake_pos: snake_starting_pos,
            direction: {current:[0,1],next:[0,1]},
            score: 0,
            gameOver: false,
        }

        this.init = this.init.bind(this)
        this.moveSnake = this.moveSnake.bind(this)
        this.gen_coord = this.gen_coord.bind(this)
        this.restartGame = this.restartGame.bind(this)
    }

    componentDidMount(){
        this.init()
        setTimeout(()=> this.timer = setInterval(this.moveSnake,this.snakeSpeed),500)
        document.addEventListener("keydown", this.changeDirection)
    }
    
    gen_coord = () => {
        // generate a random coordinate within the grid 
        let snake_pos = this.state.snake_pos.slice()
        let flag = true
        let new_coord
        while(flag){
            new_coord = [Math.floor((Math.random() * this.dimension)),Math.floor((Math.random() * this.dimension))]
            if (!snake_pos.some(el => JSON.stringify(el) === JSON.stringify(new_coord))){
                flag = false
            } 
        }
        return new_coord
    }

    init = () => {
        //generating a random value for the food position 
        let squares = this.state.squares.slice()
        let starting_food_pos = this.gen_coord()
        squares[starting_food_pos[1]][starting_food_pos[0]] = 2
        this.setState({
            squares: squares
        })
    }

    moveSnake = () => {
        let current_snake_pos = this.state.snake_pos.slice()
        let squares = this.state.squares.slice()
        let direction = Object.assign({},this.state.direction)
        let next_direction = direction['next'].slice()
        direction['current'] = next_direction
        let score = this.state.score    
        let gameOver = false
        
        let head = current_snake_pos[0]
        let new_head = [head[0] + next_direction[1],head[1] + next_direction[0]]
        // if the snake hits the edge of the grid, player loses and game ends 
        // else update the position of the snake 
        if (new_head[0] > this.dimension-1 || new_head[1] > this.dimension-1 || new_head[0] < 0 || new_head[1] < 0 || current_snake_pos.some(el => JSON.stringify(el) === JSON.stringify(new_head))){
            clearTimeout(this.timer)
            gameOver = true
        }else{
            let tail = current_snake_pos[current_snake_pos.length - 1]
            squares[tail[1]][tail[0]] = 0
            current_snake_pos = current_snake_pos.map((el, idx)=>{
                if (idx === 0){
                    return el 
                }
                return current_snake_pos[idx-1]
            })
            current_snake_pos[0] = new_head
            if (squares[new_head[1]][new_head[0]] === 2){
                // if the snake eats food then extend its length by 1 
                // generate a new food 
                current_snake_pos.push(tail)
                score += 1 
                let new_food_pos = this.gen_coord() 
                squares[new_food_pos[1]][new_food_pos[0]] = 2
            }
            current_snake_pos.map((el) => squares[el[1]][el[0]] = 1)
        }

        this.setState({
            snake_pos: current_snake_pos,
            squares: squares,
            direction: direction,
            score: score,
            gameOver: gameOver
        })        
    }

    changeDirection = (e) => {
        let new_direction
        let direction = Object.assign({},this.state.direction)
        let current_direction = direction['current'].slice()
        let key = e.keyCode 
        switch(key){
            case 37:
                //left
                new_direction = current_direction[1] ? current_direction:[0,-1]
                break
            case 38:
                //top
                new_direction = current_direction[0] ? current_direction:[-1,0]
                break
            case 39:
                //right
                new_direction = current_direction[1] ? current_direction:[0,1]
                break
            case 40:
                //down
                new_direction = current_direction[0] ? current_direction:[1,0]
                break
            default: 
                //maintain same direction
                new_direction = current_direction
                break
        }
        direction['next'] = new_direction

        this.setState({
            direction: direction
        })
    }

    restartGame(){
        clearTimeout(this.timer)
        let squares = Array(this.dimension).fill().map(()=>Array(this.dimension).fill(0))
        let starting_food_pos = this.gen_coord()
        squares[starting_food_pos[1]][starting_food_pos[0]] = 2
        let mid = Math.floor(this.dimension/2) 
        let snake_starting_pos = [[mid,mid],[mid-1,mid]]
        snake_starting_pos.forEach(el => {
            squares[el[1]][el[0]] = 1
        })
        this.setState({
            squares: squares,
            snake_pos: snake_starting_pos,
            direction: {current:[0,1],next:[0,1]},
            score: 0,
            gameOver: false,
        },() => setTimeout(()=> this.timer = setInterval(this.moveSnake,this.snakeSpeed),500))        
    }

    render(){
        return(
            <div className="snakes-page-container">
                <Board squares={this.state.squares} gameOver={this.state.gameOver}/>
                <Panel restartGame={this.restartGame} score={this.state.score}/> 
            </div> 
        )
    }
}

export default SnakeGame