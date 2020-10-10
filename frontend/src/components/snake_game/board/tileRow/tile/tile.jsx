import React from "react"

import "./tile.styles.scss"

const Tile = (props) => {
    return (
        <div className={`tile ${props.gameOver && props.state != 1 ? "greyed": ""} ${props.state ? props.state === 1 ? "tile-black": "tile-green" :""}`}></div>
    ) 
}

export default Tile