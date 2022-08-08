import React from 'react';
import { BrowserRouter, Route, Routes } from "react-router-dom";
//import Navigation from "./components/navigation";
//import { Home, Menu1, Menu2, Menu3, Menu4 } from "./pages";

export default function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/"></Route>
        <Route path="/menu1"></Route>
        <Route path="/menu2"></Route>
        <Route path="/menu3"></Route>
        <Route path="/menu4"></Route>
      </Routes>
    </BrowserRouter>
  );
}

