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
  const small_name = props.hero.id + '_sb.png'
  const small_img = require('../assets/' + small_name)

  /* Not in Development */
  /* const large_name = props.hero.id + '_full.png'
   * const large_img = require('../assets/' + large_name) */

  if (props.hero.win_rate != null){
    text = props.hero.name + " %"  + Number((props.hero.win_rate * 100).toFixed(1))
  } else {
    text = props.hero.name
  }

  if (props.onClick){
    return (
      <button className='Hero-button'
              onClick={() => props.onClick({'id' : props.hero.id,
                                            'name' :props.hero.name})} >
        <img alt=""
             src={small_img}/>
      </button>)
  } else {
    return <h4>{props.hero.name}</h4>
  }
};

export default HeroItem;

{/* onMouseOver={e => e.currentTarget.src = large_img}
    onMouseOut={e => e.currentTarget.src = small_img} */}
