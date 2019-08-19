import React, { Component } from 'react';
import './App.css';
import axios from 'axios';
import HeroList from './components/HeroList';

class App extends Component{

  constructor(){
    super();
    this.state = {
      heroes: [],
      selected: [],
    };
  };

  componentDidMount(){
    this.getHeroes();
    /* this.getUsers(); */
  };

  getHeroes(){
    axios.get(process.env.REACT_APP_HEROES_SERVICE_URL + '/api/heroes')
         .then(res => {this.setState({heroes: res.data.data.heroes});})
         .catch(err => {console.log(err);});
  };
  
  /* getUsers() {
   *   axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
   *        .then((res) => { this.setState({ users: res.data.data.users }); })
   *        .catch((err) => { console.log(err); });
   * }; */

  render(){
    return (
      <div className="App">
        <HeroList heroes={this.state.heroes}/>
      </div>
    );
  }
}

export default App;
