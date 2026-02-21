import { JsonRpcProvider, Interface } from "ethers";
import dotenv from "dotenv";

dotenv.config();

const RPC_HTTP_URL = process.env.RPC_HTTP_URL;
const TRADER_ADDRESS = process.env.TRADER_ADDRESS?.toLowerCase();

// PancakeSwap V2 Router (BSC)
const ROUTER = "0x10ED43C718714eb63d5aA57B78B54704E256024E".toLowerCase();

const ROUTER_ABI = [
  "function swapExactTokensForTokens(uint amountIn,uint amountOutMin,address[] calldata path,address to,uint deadline)",
  "function swapExactETHForTokens(uint amountOutMin,address[] calldata path,address to,uint deadline)",
  "function swapExactTokensForETH(uint amountIn,uint amountOutMin,address[] calldata path,address to,uint deadline)",
  "function swapTokensForExactTokens(uint amountOut,uint amountInMax,address[] calldata path,address to,uint deadline)",
  "function swapETHForExactTokens(uint amountOut,address[] calldata path,address to,uint deadline)",
  "function swapTokensForExactETH(uint amountOut,uint amountInMax,address[] calldata path,address to,uint deadline)"
];

if (!RPC_HTTP_URL || !TRADER_ADDRESS) {
  console.error("❌ Isi RPC_HTTP_URL dan TRADER_ADDRESS di file .env dulu");
  process.exit(1);
}

console.log("🚀 Starting BSC wallet monitor (logs-based)...");
console.log("👀 Monitoring trader:", TRADER_ADDRESS);
console.log("🧠 Router:", ROUTER);

const provider = new JsonRpcProvider(RPC_HTTP_URL);
const iface = new Interface(ROUTER_ABI);

let lastBlock = 0;

async function scanLoop() {
  try {
    const current = await provider.getBlockNumber();
    if (!lastBlock) {
      lastBlock = current - 1;
      console.log("✅ Connected. Current block:", current);
    }

    // scan block by block (safe, simple)
    for (let b = lastBlock + 1; b <= current; b++) {
      const block = await provider.getBlock(b, true);
      if (!block || !block.transactions) continue;

      for (const tx of block.transactions) {
        if (!tx?.to || !tx?.from) continue;
        if (tx.from.toLowerCase() !== TRADER_ADDRESS) continue;
        if (tx.to.toLowerCase() !== ROUTER) continue;

        let decoded;
        try {
          decoded = iface.parseTransaction({ data: tx.data, value: tx.value });
        } catch {
          continue;
        }

        console.log("\n🔥 Trader Swap (mined) Detected!");
        console.log("Block:", b);
        console.log("Tx Hash:", tx.hash);
        console.log("Function:", decoded.name);
        console.log("Args:", decoded.args);
      }
    }

    lastBlock = current;
  } catch (e) {
    console.error("⚠️ scan error:", e?.message ?? e);
  } finally {
    setTimeout(scanLoop, 2500); // BSC cepat; polling 2.5 detik
  }
}

scanLoop();

import { getBalances } from "./balance.js";

await getBalances();

import { getPortfolio } from "./portfolio.js";

await getPortfolio();