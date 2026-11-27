import { useEffect, useState } from "react";

export default function App() {
  const [msg, setMsg] = useState("Checking backend...");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/health")
      .then((r) => r.json())
      .then((d) => setMsg("Backend says: " + d.status))
      .catch(() => setMsg("Backend not reachable"));
  }, []);

  return (
    <h1 className="p-8 text-2xl font-bold text-blue-700">
      BidWise AI — {msg}
    </h1>
  );
}