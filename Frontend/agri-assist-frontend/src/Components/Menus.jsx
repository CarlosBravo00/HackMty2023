import React from "react";
import { Item } from "./Item";
import "./style.css";

export const Menu = () => {
  return (
    <div className="MENU">
      <div className="overlap-group">
        <img className="leaf" alt="Leaf" src="https://c.animaapp.com/uCZJ3HAz/img/leaf-1@2x.png" />
        <div className="overlap">
          <img className="user" alt="User" src="https://c.animaapp.com/uCZJ3HAz/img/user-1@2x.png" />
        </div>
        <Item className="ITEM-instance" divClassName="design-component-instance-node" property1="default" text="FAQ" />
        <div className="div">How it works?</div>
        <div className="text-wrapper-2">Our team</div>
      </div>
    </div>
  );
};
