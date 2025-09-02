
import React, {useEffect, useState} from 'react'; import API from '../api'; import PostCard from '../components/PostCard'
export default function Feed(){ const [posts,setPosts]=useState([]); const [loading,setLoading]=useState(true)
  useEffect(()=>{ load() },[])
  async function load(){ setLoading(true); try{ const r=await API.get('posts/'); setPosts(r.data); }catch(e){} setLoading(false) }
  async function like(id){ try{ await API.post(`posts/${id}/like/`); load(); }catch(e){} }
  return (<div><h2 className="text-xl mb-4">Feed</h2><div className="mb-4"><form onSubmit={async e=>{e.preventDefault(); const fd=new FormData(e.target); try{ await API.post('posts/', fd, { headers: {'Content-Type':'multipart/form-data'} }); e.target.reset(); load(); }catch(err){ console.error(err) }}} className="bg-white p-3 rounded mb-4"><input name="caption" placeholder="Write a caption..." className="w-full p-2 border rounded mb-2" /><input type="file" name="image" className="mb-2" /><button className="bg-indigo-600 text-white px-3 py-1 rounded">Post</button></form></div>{loading ? <div>Loading...</div> : posts.map(p=> <PostCard key={p.id} post={p} onLike={()=>like(p.id)}/> )}</div>)
}
