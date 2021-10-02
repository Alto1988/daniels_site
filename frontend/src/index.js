import React from "react";
import ReactDOM from "react-dom";

export default function App() {
  return (
    <div>
      <h1>This is the entry point.</h1>
    </div>
  );
}

const root = document.getElementById("root");

ReactDOM.render(<App />, root);
