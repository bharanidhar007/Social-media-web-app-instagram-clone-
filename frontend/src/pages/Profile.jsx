
import React, {useEffect, useState} from 'react'; import { useParams } from 'react-router-dom'; import API from '../api'
export default function Profile({me}){
  const {username} = useParams(); const [profile,setProfile]=useState(null)
  useEffect(()=>{ load() },[username])
  async function load(){ try{ const url = me? 'profiles/me/': `profiles/${username}/`; const r=await API.get(url); setProfile(r.data);}catch(e){ console.error(e)} }
  async function toggleFollow(){ try{ await API.post(`profiles/${username}/follow/`); load(); }catch(e){console.error(e)} }
  if(!profile) return <div>Loading...</div>
  return (<div className="bg-white p-4 rounded shadow"><div className="flex items-center space-x-4 mb-3"><div className="w-20 h-20 bg-gray-200 rounded-full"></div><div><div className="font-bold text-lg">{profile.username}</div><div className="text-sm text-gray-600">{profile.bio}</div></div></div>{!me && <button onClick={toggleFollow} className="bg-blue-600 text-white px-3 py-1 rounded">Follow/Unfollow</button>}</div>)
}
