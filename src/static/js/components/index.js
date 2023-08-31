import React from "react";
import ReactDOM from "react-dom";
import Knob from "./knob";
  
let knob = document.getElementById("react-knob");
let knobVal = parseInt(knob.getAttribute("initialValue"));
ReactDOM.render(<Knob initialValue={knobVal} type={1}/>, knob);

