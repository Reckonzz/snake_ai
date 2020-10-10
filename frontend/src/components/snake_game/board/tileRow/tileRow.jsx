import React from "react"

import Tile from "./tile/tile"
import "./tileRow.styles.scss"

const TileRow = (props) => {
    return(
        <div className="tile-row">
            {props.tiles.map((el,idx) => <Tile key={idx} state={el} gameOver={props.gameOver}/>)}
        </div>
    )
}

export default TileRow