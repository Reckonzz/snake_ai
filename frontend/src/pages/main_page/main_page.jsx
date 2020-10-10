import React from "react"

import SnakeGame from "../../components/snake_game/snake_game"

import "./main_page.styles.scss"

class MainPage extends React.Component{
    render(){
        return(
            <div>
                <SnakeGame/>
            </div> 
        )
    }
}

export default MainPage