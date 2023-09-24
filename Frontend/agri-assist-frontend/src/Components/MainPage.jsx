import React from "react";
import "./style.css";
import { ChatBoxContainer } from "./ChatboxContainer";
import { DataContainer } from "./DataContainer";
export const MainPage = () => {
    return (
        <div className="MainPage">
            <div className="body">
                <div className="container">
                    <DataContainer />
                    <ChatBoxContainer />
                </div>
            </div>
        </div>
    );
};
