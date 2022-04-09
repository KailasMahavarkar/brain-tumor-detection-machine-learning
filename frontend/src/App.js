import "../src/css/main.css";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Scanpage from "./components/scanpage";
import Navbar from "./components/navbar";

const AnyRoute = () => {
    return (
        <>
            Bad Request | Page Not Found
        </>
    )
}

function App() {
	return (
		<Router>
            <Route exact path="*" component={Navbar} />
			<Switch>
				<Route exact path="/" component={Scanpage} />

                {/* for other routes */}
                <Route exact path="*" component={AnyRoute} />
			</Switch>
		</Router>
	);
}

export default App;
