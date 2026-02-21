import { JsonRpcProvider, Contract, formatUnits } from "ethers";
import dotenv from "dotenv";
import ERC20_ABI from "./erc20_abi.js";

dotenv.config();

const provider = new JsonRpcProvider(process.env.RPC_HTTP_URL);
const wallet = process.env.TRADER_ADDRESS;

export async function getBalances() {
  // 🏦 Native BNB balance
  const native = await provider.getBalance(wallet);
  console.log("🏦 BNB Balance:", formatUnits(native, 18));

  // Token yang mau dicek
  const tokens = [
    "0xe9e7cea3dedca5984780bafc599bd69add087d56", // BUSD
    "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82", // CAKE
  ];

  for (const t of tokens) {
    const erc = new Contract(t, ERC20_ABI, provider);
    const bal = await erc.balanceOf(wallet);
    const decimals = await erc.decimals();
    const symbol = await erc.symbol();

    console.log(`💼 ${symbol} Balance:`, formatUnits(bal, decimals));
  }
}