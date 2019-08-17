import React, { Component } from 'react';
import './App.css';
import axios from 'axios';

class App extends Component{

  constructor(){
    super();
    this.getHeroes();
    this.state = {
      selected: []
    }
  }

  getHeroes(){
    axios.get(`${process.env.REACT_APP_HEROES_SERVICE_URL}/heroes`)
         .then((res) => {console.log(res);})
           .catch((err) => {console.log(err);});
  }

  render(){
    return (
      <div className="App">
        Hello World!
      </div>
    );
  }
}

export default App;
