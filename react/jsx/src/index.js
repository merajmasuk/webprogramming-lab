// import the react and reactdom libraries
import React from "react";
import ReactDOM from "react-dom";

// create a react components
const App = () => {
    const buttonText = 'Click Me!';

    return <div>
        <label className="label" for="name">Enter name:</label>
        <input id="name" type="text" />
        <button style={{ backgroundColor: 'blue', color: 'white' }}>
            {buttonText}
        </button>
    </div>;
};

// take the react component and show on screen
ReactDOM.render(
    <App />,
    document.querySelector('#root')
);
