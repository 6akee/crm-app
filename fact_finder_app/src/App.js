import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div className="Search-box">
          <input
            type="text"
            placeholder="Enter Movie or Show name"
            className="Search-input"
          />
          <button className="Search-button">Search</button>
        </div>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn App
        </a>
      </header>
    </div>
  );
}

export default App;
