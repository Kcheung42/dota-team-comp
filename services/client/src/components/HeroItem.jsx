import React from 'react';

const HeroItem = (props) => {
  return (
    <h4>
      {props.hero.name}
    </h4>
  );
};

export default HeroItem;
