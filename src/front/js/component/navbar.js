import React from "react";
import { Link } from "react-router-dom";
import "../../styles/home.css";


export const Navbar = () => {
	return (
		<nav className="navbar">
			<div className="container">
				<Link to="/">
					<h1 className="navbar-brand mb-0 h1 py-3">Tokio Blue</h1>
				</Link>
				<div className="ml-auto">
					<Link to="/demo">
						<button className="btn btn-primary">Check the Context in action</button>
					</Link>
				</div>
			</div>
		</nav>
	);
};
