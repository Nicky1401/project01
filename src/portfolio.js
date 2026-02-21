import axios from "axios";
import dotenv from "dotenv";

dotenv.config();

const WALLET = process.env.TRADER_ADDRESS;
const API_KEY = process.env.COVALENT_API_KEY;

const CHAINS = [
  { id: 1, name: "Ethereum" },
  { id: 56, name: "BSC" },
  { id: 137, name: "Polygon" }
];

export async function getPortfolio() {
  try {
    let totalValue = 0;

    for (const chain of CHAINS) {
      const url = `https://api.covalenthq.com/v1/${chain.id}/address/${WALLET}/balances_v2/?key=${API_KEY}`;

      const res = await axios.get(url);

      if (!res.data?.data?.items) continue;

      console.log(`\n🌐 ${chain.name}`);
      console.log("=".repeat(60));

      for (const token of res.data.data.items) {
        if (token.balance > 0 && token.contract_ticker_symbol) {
          const balance =
            token.balance / Math.pow(10, token.contract_decimals);

          const usdValue = token.quote ?? 0;
          totalValue += usdValue;

          console.log(
            `${token.contract_ticker_symbol.padEnd(8)} | ` +
            `Balance: ${balance.toFixed(6).padEnd(12)} | ` +
            (token.quote
              ? `USD: $${usdValue.toFixed(2)}`
              : `USD: No price data`) +
	    ` | Contract: ${token.contract_address}`
          );
        }
      }
    }

    console.log("\n💰 TOTAL PORTFOLIO VALUE:", `$${totalValue.toFixed(2)}`);

  } catch (err) {
    console.error("API Error:", err.response?.data || err.message);
  }
}