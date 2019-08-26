import React from 'react';

const HeroLabel = (props) =>{
  if (props.win_rate){
    return props.win_rate
  } else {
    return props.name
  }
}

const HeroItem = (props) => {

  let text
  const file_name = props.hero.id + '_sb.png'
  const logo = require('../assets/' + file_name)

  if (props.hero.win_rate != null){
    text = props.hero.name + " %"  + Number((props.hero.win_rate * 100).toFixed(1))
  } else {
    text = props.hero.name
  }

  if (props.onClick){
    return (
      <button onClick={() => props.onClick({'id' : props.hero.id,
                                            'name' :props.hero.name})} >
        <img alt="" src={logo}/>
      </button>)
  } else {
    return <h4>{props.hero.name}</h4>
  }
};

export default HeroItem;
