import React, { useState } from "react";
import TransactionForm from "../components/TransactionForm";
import TransactionList from "../components/TransactionList";
import '../components/TransactionForm.css';

const TransactionPage = () => {
	const [refresh, setRefresh] = useState(false);
	const token = sessionStorage.getItem("token"); // Assuming authentication token is stored

	const refreshTransactions = () => setRefresh(!refresh);

	return (
		<div
			style={{
				display: "flex",
				flexDirection: "column",
				justifyContent: "center",
				alignItems: "center",
			}}
		>
			<h1>Transaction Page</h1>
			<TransactionForm
                style={{}}
				onTransactionSuccess={refreshTransactions}
				token={token}
			/>
			<TransactionList token={token} key={refresh} />
		</div>
	);
};

export default TransactionPage;