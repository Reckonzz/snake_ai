import React from 'react'

import "./score.styles.scss"

const Score = (props) => {
    return (
        <div>
            <div>Score: {props.score} </div> 
        </div> 
    )
}

export default Score