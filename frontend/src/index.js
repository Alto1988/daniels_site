import React from "react";
import ReactDOM from "react-dom";
import { ArtNavHome } from "./components/Navigation/navbar";

export default function App() {
  return (
    <div>
      <ArtNavHome />
    </div>
  );
}

const root = document.getElementById("root");

ReactDOM.render(<App />, root);
