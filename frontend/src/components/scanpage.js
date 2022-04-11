import React, { useState } from "react";
import Upload from "rc-upload";
import Loader from "react-loader-spinner";
import {  url } from "../helper";

const Scanpage = () => {
	const [data, setData] = useState();
	const [err, setErr] = useState();
	const [running, setRunning] = useState(false);

	const uploadProps = {
		action: url("/scan"),
		method: "POST",
		multiple: false,
		onStart(file) {
			setRunning(true);
            setData({
                prediction: 0,
				msg: ""
            })
		},
		onSuccess(result) {
			setRunning(false);
			setData({
				prediction: result?.prediction,
				msg: result?.msg,
			});
		},
		onError(err) {
			console.log("onError", err);
		},
		beforeUpload(file, fileList) {
			console.log(file, fileList);
		},
	};

	const DisplayData = () => {
		return (
			<>
				{data ? (
					<section>
						<div className="title">Prediction Result</div>
						<div className="data">{data?.prediction}</div>
					</section>
				) : null}

				{err ? <section>{err}</section> : null}
			</>
		);
	};

	return (
		<div className="container">
			<div className="main">
				<section>
					<div className="upload_container">
						<Upload {...uploadProps}>
							<button className="custom-file-upload">
                                Scan File
							</button>
						</Upload>
					</div>
				</section>

				{running ? (
					<section>
						<Loader
							className="spinner"
							type="ThreeDots"
							color="#7727d8"
							height={100}
							width={100}
						/>
					</section>
				) : (
					<DisplayData />
				)}
			</div>
		</div>
	);
};

export default Scanpage;
