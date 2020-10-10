import React from "react"

import RestartButton from "./restart_button/restart_button"
import Score from "./score/score"

import "./panel.styles.scss"

const Panel = (props) => {
    return (
        <div>
            <RestartButton handleClick = {props.restartGame}/>
            <Score score = {props.score}/>
        </div>
    )
}

export default Panel
