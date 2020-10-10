import React from "react"

import "./restart_button.styles.scss"

const RestartButton = (props) => {
    return (
        <button type="button" onClick={props.handleClick}>Restart</button>
    )
}

export default RestartButton