import React from 'react';
import {createRoot} from 'react-dom/client';
import App from './App.jsx';
import {AudioProvider} from './Audio.jsx';
import './style.css';
createRoot(document.getElementById('root')).render(<AudioProvider><App/></AudioProvider>);
