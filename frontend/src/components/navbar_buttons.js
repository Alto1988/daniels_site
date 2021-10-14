import React from "react";
import { Button } from "@mui/material";

function navBarButton(props) {
  return (
    <Button color="primary" variant="contained">
      {props.children}
    </Button>
  );
}

export default navBarButton;
