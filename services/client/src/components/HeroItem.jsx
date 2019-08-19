import React from 'react';

const HeroItem = (props) => {
  if (props.onClick){
    return (
      <button onClick={() => props.onClick({'id' : props.hero.id,
                                            'name' :props.hero.name})}>
        {props.hero.name}
      </button>)
  } else {
    return <h4>{props.hero.name}</h4>
  }
};

export default HeroItem;
