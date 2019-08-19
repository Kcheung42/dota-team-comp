import React from 'react';
import HeroItem from './HeroItem'

const HeroList = (props) => {
  return (
    <div>
      {props.heroes.map(hero =>
        <HeroItem
          key={hero.id}
          hero={hero}
          onClick={props.onClick}
        />)}
    </div>
  );
};

export default HeroList;
