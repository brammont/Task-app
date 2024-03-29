import {
  BrowserRouter,
  Navigate,
  Route,
  Routes
} from 'react-router-dom'
import { TaskFormPage } from './pages/TaskFormPage';
import { TaskPage } from './pages/TaskPage';
import { Navigation } from './components/Navigation';
function App() {
  return (
    <BrowserRouter>
      <Navigation/>
      <Routes>
        <Route path='/' element={<Navigate to="/tasks" />} />
        <Route path='/tasks' element={<TaskPage />} />
        <Route path='/tasks-create' element={<TaskFormPage/>}/>
      </Routes>
    </BrowserRouter>
    
  );
}

export default App;