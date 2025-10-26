import './App.css'
import { Provider } from './components/ui/provider'

function App() {
  return (
    <Provider>
      <div className="app">
        <h1>Welcome to davipaiva-v2</h1>
        <p>Personal website built with React, Vite, and Chakra UI</p>
      </div>
    </Provider>
  )
}

export default App
