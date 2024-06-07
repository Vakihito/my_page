import React, { useState } from 'react';
import '@popperjs/core/dist/umd/popper.min.js';
import 'bootstrap/dist/css/bootstrap.min.css';
import './counter.css';
import { Dropdown } from 'react-bootstrap';


const counter_format = {
  date_format: null, // months, days, years
  number_of_dots_fill: 0, // number of weaks in a year
  number_of_dots_empty: 0, // number of weaks in a year
};

function weeksBetween(date1, date2, milisecondsBTW) {
  console.log("date2", date2)
  console.log("date1", date1)
  // Get the difference in milliseconds
  const diffInMilliseconds = Math.abs(date2 - date1);
  const diffInWeeks = diffInMilliseconds / milisecondsBTW;
  return Math.round(diffInWeeks);
}

function CreateDotsList(NumberDotsFill, NumberDotsEmpty) {
  
  
  let dots = []
  for (let i = 0; i < NumberDotsFill; i++) {
    dots.push(<i className="bi-circle-fill p-1 icon grey-text" key={"icon-f-" + i}></i>);
  }
  for (let i = 0; i < NumberDotsEmpty; i++) {
    dots.push(<i className="bi-circle p-1 icon grey-text" key={"icon-e-" + i}></i>);
  }
  console.log('dots : ', dots.length)
  return (dots)
}

function DateFormatDropdown(start_day, end_day, setNumberDotsFill, setNumberDotsEmpty) {
  
  const today = new Date();

  let dropdown_itens = ['Days', 'Weaks', 'Month', 'Years']
  const [DateFormat, setDateFormat] = useState("Select date format");
  const [DropdownClass, setDropdownClass] = useState('with-caret custom-dropdown-toggle text-black');

  const handleClick = (event) => {
    counter_format.date_format = event.currentTarget.getAttribute('date-item')
    setDateFormat(counter_format.date_format)
    if (counter_format.date_format === null) {
      setDropdownClass('with-caret custom-dropdown-toggle text-black')
    }
    else {
      setDropdownClass('no-caret custom-dropdown-toggle text-black')
    }
    let milisecondsBTW = 86400000
    if (counter_format.date_format === "Days") {
      milisecondsBTW = 86400000 
    }else if(counter_format.date_format === "Weaks"){
      milisecondsBTW = 86400000 * 7
    }else if(counter_format.date_format === "Month"){
      milisecondsBTW = 86400000 * 31
    }else if(counter_format.date_format === "Years"){
      milisecondsBTW = 86400000 * 364
    }
    console.log('milisecondsBTW : ',  milisecondsBTW)
    console.log('mcounter_format.date_format : ',  counter_format.date_format)
    counter_format.number_of_dots_fill = weeksBetween(start_day,today, milisecondsBTW);
    counter_format.number_of_dots_empty = weeksBetween(today,end_day, milisecondsBTW);
    setNumberDotsFill(counter_format.number_of_dots_fill);
    setNumberDotsEmpty(counter_format.number_of_dots_empty);
  }

  let mapped_itens = dropdown_itens.map((item, index) => (<Dropdown.Item date-item={item} key={index} onClick={handleClick} className="dropdown-item">{item}</Dropdown.Item>))


  return (
    <Dropdown>
      <Dropdown.Toggle className={DropdownClass} id="dropdown-basic">
        {DateFormat}
      </Dropdown.Toggle>
      <Dropdown.Menu className='w-75'>
        {mapped_itens}
      </Dropdown.Menu>
    </Dropdown>
  )
}

function TimeLeft(NumberDotsEmpty) {

  let text_value = "Time left"
  if (counter_format.date_format !== null){
    text_value = `${counter_format.number_of_dots_empty} ${counter_format.date_format} left`
  }

  return (
    <div className="border rounded border-grey text-box-width mt-4">
      <p className="text-left time-left text-dark align-text-top">{text_value}</p>
    </div>
  )
}

export default function Counter(props) {
  console.log("start_day : ",props.start_day) 
  console.log("end_day : ",props.end_day) 
  const [NumberDotsFill, setNumberDotsFill] = useState(0);
  const [NumberDotsEmpty, setNumberDotsEmpty] = useState(0);

  const drop_down = DateFormatDropdown(props.start_day, props.end_day, setNumberDotsFill, setNumberDotsEmpty)
  const dots = CreateDotsList(NumberDotsFill, NumberDotsEmpty)
  const time_left = TimeLeft(NumberDotsEmpty)
  return (
    <>
      <div id="dotsDiv" className="container p-3 rounded bg-white wd-90 shadow ">
        <div className="row">
          <div className="col-8 text-start">
            {dots}
          </div>
          <div className="col-4 container d-flex flex-column">
            <div className="row">{drop_down}</div>
            <div className="row d-flex justify-content-center">{time_left}</div>
          </div>
        </div>
      </div>
    </>
  );
}
