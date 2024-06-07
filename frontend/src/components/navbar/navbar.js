import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function navBarTitle(nav_bar_text) {
  return (<a class="navbar-brand ml-1" href="#">{nav_bar_text}</a>)
}

function navBarLinks() {
  return (<div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav ml-0">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#">Disabled</a>
      </li>
    </ul>
  </div>)
}

function navBarSearch() {
  return (<div class="input-group">
  <input type="text" class="form-control" placeholder="Search" aria-label="Search" aria-describedby="button-addon2" />
  <button class="btn btn-outline-secondary" type="button" id="button-addon2">Button</button>
</div>)
}



export default function Navbar() {
  const nav_bar_title = navBarTitle("Goals")
  const nav_bar_links = navBarLinks()
  const nav_bar_search = navBarSearch()

  return (
    <>
      <nav class="container-fluid nav-complete navbar navbar-expand-lg navbar-light bg-light">
        <div class=" col">
          {nav_bar_title}
        </div>
        <div class="col-5">
          {nav_bar_links}
        </div>
        <div class="col-3"></div>
        <div class="col-3">
          {nav_bar_search}
        </div>
        
      </nav>
    </>
  );
}
