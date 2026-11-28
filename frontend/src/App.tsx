import { useEffect, useState } from "react";

export default function App() {
  const [msg, setMsg] = useState("Checking backend...");

  useEffect(() => {
    fetch("/health")
      .then(async (r) => {
        const text = await r.text();
        if (!r.ok) throw new Error("HTTP " + r.status + ": " + text);
        const d = JSON.parse(text);
        setMsg("Backend says: " + (d.status ?? text));
      })
      .catch((e) => setMsg("Backend not reachable: " + String(e)));
  }, []);

  return (
    <h1 className="p-8 text-2xl font-bold text-blue-700">
      BidWise AI — {msg}
    </h1>
  );
}