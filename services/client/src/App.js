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

  /* ID: [...this.state.selected, e].map((hero) => hero.id).join(',') */

  update_suggestion = () => {
    if (this.state.selected.length > 0){
      axios.get(process.env.REACT_APP_HEROES_SERVICE_URL + '/api/recommendations', {
        params: {
          ID: this.state.selected.map((hero) => hero.id).join(',')
        }
      }).then(response => {
        this.setState({suggested: response.data.data.heroes.sort((a,b) => {return b.win_rate - a.win_rate})}, () => {console.log(this.state.suggested)});
      })
           .catch(error => {console.log(error);})
    }
  }

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
      this.setState(
        {selected: [...this.state.selected, e]},
        /* After state is set */
        () => {
          if (this.state.selected.length === 5){
            this.setState({suggested: []})
          } else {
            this.update_suggestion()
          }
        }
      );
    };
  };

  onClickRemove = (e) => {
    const selected = this.state.selected
    if (selected.length > 0) {
      this.setState(
        {selected: selected.filter((hero) => hero.id !== e['id'])},
        /* After state is set */
        () => {
          if(this.state.selected.length === 0){
            this.setState({suggested: []})
          }else{
            this.update_suggestion()
          }
        }
      );
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
        <h1 className='h1'>Selected</h1>
        <HeroList heroes={this.state.selected}
                  onClick={this.onClickRemove}/>
        <h1 className='h1'>Heroes</h1>
        <HeroList heroes={this.state.heroes}
                  onClick={this.onClick}/>
        <h1 className='h1'>Suggested</h1>
        <HeroList heroes={this.state.suggested}
                  onClick={this.onClick}/>
      </div>
    );
  }
}

export default App;
