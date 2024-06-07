import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import user_image from '/workspace/src/assets/40372914-modified.jpg'
import './user.css';

const user = {
  name: 'Victor Akihito',
  description: 'my 24th year',
  image_path: user_image
};

export default function Profile() {
  return (
    <>
      <img class="rounded-circle user_info m-2" alt="user_image" src={user.image_path}/>
      <h1 className="text-center text-dark">{user.name}</h1>
      <p className="text-secondary">{user.description}</p>
    </>
  );
}
