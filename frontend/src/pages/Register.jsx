
import React, {useState} from 'react'; import API from '../api'; import { useNavigate } from 'react-router-dom'
export default function Register(){
  const [username,setUsername]=useState(''); const [email,setEmail]=useState(''); const [password,setPassword]=useState(''); const nav=useNavigate(); const [err,setErr]=useState('')
  async function submit(e){ e.preventDefault(); try{ await API.post('auth/register/',{username,email,password}); nav('/login'); }catch(e){ setErr('Register failed') } }
  return (<div className="max-w-md mx-auto bg-white p-6 rounded shadow"><h2 className="text-xl mb-4">Register</h2>{err && <div className="text-red-600 mb-2">{err}</div>}<form onSubmit={submit} className="space-y-3"><input value={username} onChange={e=>setUsername(e.target.value)} placeholder="username" className="w-full p-2 border rounded"/><input value={email} onChange={e=>setEmail(e.target.value)} placeholder="email" className="w-full p-2 border rounded"/><input type="password" value={password} onChange={e=>setPassword(e.target.value)} placeholder="password" className="w-full p-2 border rounded"/><button className="w-full bg-green-600 text-white p-2 rounded">Register</button></form></div>)
}
