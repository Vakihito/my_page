import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './goals.css'

class Goal {
  constructor(title, format) {
    this.title = title;
    this.format = format;
    this.todo = "bla bla";
    this.not_todo = "something"
  }
}


const l_goals_title = [
  new Goal("goal_1", "weak"),
  new Goal("goal_2", "month"),
  new Goal("goal_3", "month"),
  new Goal("goal_6", "year"),
  new Goal("goal_6", "year")
]

function CreateSingleGoal(goal_object) {
  return (
    <div className='container'>
      <div className='row'>
        <div className='col'>
          <div id="goal" className="goal rounded bg-white shadow text-black">
            <h6 className='goal_format' >{goal_object.format}</h6>
            <h2 className='goal_title' >{goal_object.title}</h2>
          </div>
        </div>
        <div className='col-8 container-fluid'>
          <div className='row'>
            <div class="col-12">
              <div id="todo" className="todo rounded bg-white shadow text-black">
                <h4 className='todo_text rounded' >What should I do ?</h4>
                <h6 className='goal_todo' >{goal_object.todo}</h6>
              </div>
            </div>
          </div>
          <div className='row'>
            <div class="col-12">
              <div id="nottodo" className="not-todo rounded bg-white shadow text-black">
                <h4 className='nottodo_text rounded' >What will happen if I don't</h4>
                <h6 className='goal_nottodo' >{goal_object.not_todo}</h6>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  )
}

function GoalList() {
  let l_goals = []
  for (let i = 0; i < l_goals_title.length; i++) {
    const cur_gol_title = l_goals_title[i];
    const cur_gol_comp = CreateSingleGoal(cur_gol_title);
    l_goals.push(cur_gol_comp);
  }

  return l_goals
}

function Goals() {
  const goals_list = GoalList()
  return (<>
    <div id="dotsDiv" className="container container_flex_sb">
      <div className="row goal_list">
        {goals_list}
      </div>
    </div>
  </>)
}

export default Goals;