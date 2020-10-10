import React from "react"
import TileRow from "./tileRow/tileRow"

import "./board.styles.scss"

class Board extends React.Component{
    constructor(props){
        super(props)
    }
    render(){
        return(
            <div className="board">
                {this.props.squares.map((e,idx) => <TileRow gameOver = {this.props.gameOver} key={idx} tiles={e}/>)}
            </div>
        )
    }
}

export default Board