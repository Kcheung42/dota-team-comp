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
      suggested: [],
    };
  };

  componentDidMount(){
    this.getHeroes();
    /* this.getUsers(); */
  };

  onClick = (e) => {
    const selected = this.state.selected
    var exists = (array, e) => {
      return selected.reduce((acc, v) => {
        if (v['id'] === e['id']){
          return true
        }else{
          return acc
        }
      }, false)
    }
    if (selected.length < 5 && exists(selected, e) === false){
      this.setState({selected: [...this.state.selected, e]})
      axios.get(process.env.REACT_APP_HEROES_SERVICE_URL + '/api/recommendations', {
        params: {
          ID: "1,2,3,4"
        }
      }).then(response => {
        this.setState({suggested: response.data.data.heroes});})
        .catch(error => {console.log(error);})
    };
  };

  onClickRemove = (e) => {
    const selected = this.state.selected
    if (selected.length > 0) {
      this.setState({selected: selected.filter((hero) => hero.id !== e['id'])})
    }
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
        <h1>Selected</h1>
        <HeroList heroes={this.state.selected}
                  onClick={this.onClickRemove}/>
        <h1>Heroes</h1>
        <HeroList heroes={this.state.heroes}
                  onClick={this.onClick}/>
        <h1>Suggested</h1>
        <HeroList heroes={this.state.suggested}
                  onClick={this.onClick}/>
      </div>
    );
  }
}

export default App;
