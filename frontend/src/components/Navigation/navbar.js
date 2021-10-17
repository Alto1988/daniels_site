import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import AboutStyles from "./base_routing.styles";
import { About } from "./about";
import { Contact } from "./contact";
import "../CSS/navbar.css";
import "../CSS/container.css";
import navBarButton from "../navbar_buttons";
import { Button, Input } from "@mui/material";

function ArtNavHome() {
  /**
   * TODO:
   * - Make the navbar a lot better than this
   * - Not sure what style the navcbar should be, talk to daniel first.
   */
  const [value, setValue] = React.useState("");

  const handleChange = (event) => {
    setValue(event.target.value);
    console.log(value);
  };
  return (
    <Router>
      <NavBar>
        <NavItem to="/">Home</NavItem>
        <NavItem to="/about">About</NavItem>
        <NavItem to="/contact">Contact</NavItem>
      </NavBar>
      <div className="category-container">
        <Button variant="contained">Comissions</Button>
        <Button variant="contained">Social Media</Button>
        <Input
          type="text"
          value={value}
          onChange={handleChange}
          placeholder="Search Art Piece"
        />
        <SearchButton value={value}>Search</SearchButton>
      </div>
      <Switch>
        <AboutStyles>
          <Route path="/about" component={About} />
          <Route path="/contact" component={Contact} />
          {/* <Route path="/seach" component={Search} /> */}
        </AboutStyles>
      </Switch>
    </Router>
  );
}

function NavBar(props) {
  return (
    <nav className="navbar">
      <ul className="navbar-nav">{props.children}</ul>
    </nav>
  );
}

function NavItem(props) {
  return (
    <li className="nav-item">
      <Link to={props.to}>{props.children}</Link>
    </li>
  );
}

function SearchButton(props) {
  /**
   * TODO:
   * - From this button we need to make a query to the backend to search for the art piece
   * - Need to figure out which search query we will make to the backend eg: title or by category
   * - Need to make a couple drop down menus for where the buttons are
   * - Also need to start writing some tests for the basic comonents
   */

  return (
    <Button variant="contained" onClick={() => alert(props.value)}>
      {props.children}
    </Button>
  );
}

export default ArtNavHome;
