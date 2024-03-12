import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState, useEffect} from 'react';
export function Navigation() {
   const [isAuth, setIsAuth] = useState(false);
   useEffect(() => {
     if (localStorage.getItem('access_token') !== null) {
        setIsAuth(true); 
      }
    }, [isAuth]);
     return ( 
      <div>
      <Navbar bg="dark" variant="dark">
        <Navbar.Brand href="/">Paper Betting</Navbar.Brand>            
        <Nav className="me-auto"> 
          <Nav.Link href="/">Home</Nav.Link>
        </Nav>
        <Nav>
          <Nav.Link href="/logout">Logout</Nav.Link>  
          <Nav.Link href="/login">Login</Nav.Link>
        </Nav>
      </Navbar>
     </div>
     );
}