import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Menu } from './Components/Menus';
import { MainPage } from './Components/MainPage';

function App() {
  return (
    <div className="App">
      <Menu />
      <MainPage />
    </div>
  );
}

export default App;
