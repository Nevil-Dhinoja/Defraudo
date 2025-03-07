import React, { useState, useEffect } from "react";
import { NavLink, useNavigate } from "react-router-dom"; // Import useNavigate
import "./Navbar.css";

const Navbar = () => {
	const [isLoggedIn, setIsLoggedIn] = useState(
		!!sessionStorage.getItem("token")
	);
	const navigate = useNavigate(); // Initialize useNavigate

	useEffect(() => {
		setIsLoggedIn(!!sessionStorage.getItem("token"));
	}, []);

	// Logout function with redirection
	const handleLogout = () => {
		sessionStorage.removeItem("token"); // Remove token
		setIsLoggedIn(false); // Update state
		navigate("/"); // Redirect to home page
		window.location.reload(); // Refresh the page to update UI
	};

	return (
		<nav className="navbar">
			<div className="container">
				<a href="/" className="logo">
					<span>Defraudo</span>
				</a>
				<ul className="nav-links">
					<li>
						<NavLink
							to="/"
							className={({ isActive }) => (isActive ? "active-link" : "")}
						>
							<span>Home</span>
						</NavLink>
					</li>

					{isLoggedIn && (
						<>
							<li>
								<NavLink
									to="/transactions"
									className={({ isActive }) => (isActive ? "active-link" : "")}
								>
									<span>Transactions</span>
								</NavLink>
							</li>
							<li>
								<button className="logout-btn" onClick={handleLogout}>
									<span>Logout</span>
								</button>
							</li>
						</>
					)}
					{!isLoggedIn && (
						<>
							<li>
								<NavLink
									to="/register"
									className={({ isActive }) => (isActive ? "active-link" : "")}
								>
									<span>Register</span>
								</NavLink>
							</li>
							<li>
								<NavLink
									to="/login"
									className={({ isActive }) => (isActive ? "active-link" : "")}
								>
									<span>Login</span>
								</NavLink>
							</li>
						</>
					)}
				</ul>
			</div>
		</nav>
	);
};

export default Navbar;
