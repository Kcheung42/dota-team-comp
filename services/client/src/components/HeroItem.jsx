import React from 'react';

const HeroItem = (props) => {
  return (
    <div>
      <h4 key={props.hero.id}>
        {props.hero.name}
      </h4>
    </div>
  );
};

export default HeroItem;
