import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import AboutStyles from "./base_routing.styles";
import { About } from "./about";
import { Contact } from "./contact";
import "../CSS/navbar.css";

function ArtNavHome() {
  /**
   * TODO:
   * - Make the navbar a lot better than this
   * - Not sure what style the navcbar should be, talk to daniel first.
   */
  return (
    <Router>
      <NavBar>
        <NavItem to="/">Home</NavItem>
        <NavItem to="/about">About</NavItem>
        <NavItem to="/contact">Contact</NavItem>
      </NavBar>
      <Switch>
        <AboutStyles>
          <Route path="/about" component={About} />
          <Route path="/contact" component={Contact} />
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

export default ArtNavHome;
