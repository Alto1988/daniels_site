import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import AboutStyles from "./base_routing.styles";
import { About } from "./about";
import { Contact } from "./contact";
import NavbarStyles from "./navbar.styles";

export const ArtNavHome = () => {
  /**
   * IF YOU MAKE ANY CHANGES A FULL RELOAD IS REQUIRED THE SITE WILL BREAK JUST REFRESH THE PAGE
   * TODO:
   * - Make the navbar a lot better than this
   * - Not sure what style the navcbar should be, talk to daniel first.
   */

  return (
    <Router>
      <NavbarStyles>
        <ul>
          <li>
            <Link to="/" id="top-right">
              Home
            </Link>
          </li>
          <li>
            <Link to="/about" id="top-middle">
              About
            </Link>
          </li>
          <li>
            <Link to="/contact" id="top-left">
              Contact
            </Link>
          </li>
        </ul>
      </NavbarStyles>
      <Switch>
        <AboutStyles>
          <Route path="/about" component={About} />
          <Route path="/contact" component={Contact} />
        </AboutStyles>
      </Switch>
    </Router>
  );
};
