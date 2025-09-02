
import React, {useState} from 'react'; import API from '../api'; import { Link, useNavigate } from 'react-router-dom'
export default function Login({setToken}){
  const [username,setUsername]=useState(''); const [password,setPassword]=useState(''); const nav=useNavigate(); const [err,setErr]=useState('')
  async function submit(e){ e.preventDefault(); try{ const r=await API.post('auth/jwt/create/',{username,password}); setToken(r.data.access); nav('/'); }catch(e){ setErr('Login failed') } }
  return (<div className="max-w-md mx-auto bg-white p-6 rounded shadow"><h2 className="text-xl mb-4">Login</h2>{err && <div className="text-red-600 mb-2">{err}</div>}<form onSubmit={submit} className="space-y-3"><input value={username} onChange={e=>setUsername(e.target.value)} placeholder="username" className="w-full p-2 border rounded"/><input type="password" value={password} onChange={e=>setPassword(e.target.value)} placeholder="password" className="w-full p-2 border rounded"/><button className="w-full bg-blue-600 text-white p-2 rounded">Login</button></form><div className="mt-3">No account? <Link to="/register" className="text-blue-600">Register</Link></div></div>)
}
