
import React from 'react'
export default function PostCard({post, onLike}){
  return (<div className="bg-white rounded shadow p-3 mb-4">
    <div className="flex items-center space-x-3 mb-2"><div className="w-10 h-10 bg-gray-200 rounded-full"></div><div className="font-semibold">{post.author}</div></div>
    {post.image && <img src={post.image} alt="" className="w-full max-h-96 object-cover mb-2"/>}
    <div className="mb-2">{post.caption}</div>
    <div className="flex items-center space-x-3"><button onClick={onLike} className="px-3 py-1 bg-blue-100 rounded">Like ({post.likes_count || 0})</button></div>
  </div>)
}
