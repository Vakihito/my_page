import './App.css';
import Profile from '/workspace/src/components/user/user.js';
import Counter from '/workspace/src/components/counter/counter.js';
import Navbar from '/workspace/src/components/navbar/navbar.js';
import 'bootstrap/dist/css/bootstrap.min.css';
import Goals from '/workspace/src/components/goals/goals'

function App() {
  const start_day = new Date('2024-01-01');
  const end_day = new Date('2025-07-21');
  return (
    <div className="App">
      <Navbar></Navbar>
      <header className="App-header mt-2">
        <Profile></Profile>
        <Counter start_day={start_day} end_day={end_day}></Counter>
        <Goals></Goals>
      </header>
    </div>
  );
}

export default App;
