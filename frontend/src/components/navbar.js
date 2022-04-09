import React from "react";
import { Link, useHistory } from "react-router-dom";

const Navbar = () => {
	let history = useHistory();

	const scanHandler = () => {
		history.push("/scan");
	};
	const fetchHandler = () => {
		history.push("/req");
	};

	return (
		<div className="navbar">
			<div
				className="navbar__logo"
				onClick={() => console.log("logo clicked")}
			>
				<Link to="/">
					<a className="alink">Brain Tumor Detection</a>
				</Link>
			</div>
		</div>
	);
};

export default Navbar;
