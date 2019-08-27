import React from 'react';

const HeroItem = (props) => {

  const small_name = props.hero.id + '_sb.png'
  const small_img = require('../assets/' + small_name)

  if (props.onClick){
    return (
      <button className='Hero-button'
              onClick={() => props.onClick({'id' : props.hero.id,
                                            'name' :props.hero.name})} >
        <img alt="" src={small_img}/>
      </button>)
  } else {
    return <h4>{props.hero.name}</h4>
  }
};

export default HeroItem;
