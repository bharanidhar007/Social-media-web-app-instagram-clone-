
import React, {useState, useEffect} from 'react'
import { Routes, Route, Link, useNavigate } from 'react-router-dom'
import Feed from './pages/Feed'
import Login from './pages/Login'
import Register from './pages/Register'
import Profile from './pages/Profile'
import { setAuthToken } from './api'
export default function App(){
  const [token, setToken]=useState(localStorage.getItem('token')); const navigate=useNavigate();
  useEffect(()=>{ setAuthToken(token) },[token])
  function logout(){ localStorage.removeItem('token'); setToken(null); navigate('/login') }
  return (<div className="max-w-2xl mx-auto">
    <nav className="flex items-center justify-between p-4 border-b bg-white sticky top-0 z-10">
      <Link to="/" className="font-bold">InstaClone</Link>
      <div className="space-x-3">{!token ? <Link to="/login">Login</Link> : <><button onClick={logout}>Logout</button><Link to="/profile/me">Profile</Link></>}</div>
    </nav>
    <main className="p-4"><Routes><Route path="/" element={<Feed token={token}/>}/><Route path="/login" element={<Login setToken={t=>{setToken(t); localStorage.setItem('token', t);}}/>}/><Route path="/register" element={<Register/>}/><Route path="/profile/:username" element={<Profile/>}/><Route path="/profile/me" element={<Profile me/>}/></Routes></main>
  </div>)
}
