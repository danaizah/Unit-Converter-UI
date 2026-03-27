import "./Converter.css"
import { useState } from "react"

export default function Converter() {
  const [value, setValue] = useState("")
  const [fromUnit, setFromUnit] = useState("km")
  const [toUnit, setToUnit] = useState("miles")
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)

  const units = ["km", "miles", "kg", "lbs", "c", "f"]

  const handleConvert = async () => {
    setError(null)
    try {
      const res = await fetch("http://localhost:5000/convert", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          value: parseFloat(value),
          from_unit: fromUnit,
          to_unit: toUnit
        })
      })
      const data = await res.json()
      if (data.error) setError(data.error)
      else setResult(data.result)
    } catch {
      setError("Could not reach the server.")
    }
  }

  return (
    <div className="wrapper">
      <h1>Unit Converter</h1>
      <input
        type="number"
        value={value}
        onChange={e => setValue(e.target.value)}
        placeholder="Enter value"
      />
      <select value={fromUnit} onChange={e => setFromUnit(e.target.value)}>
        {units.map(u => <option key={u}>{u}</option>)}
      </select>
      <span> → </span>
      <select value={toUnit} onChange={e => setToUnit(e.target.value)}>
        {units.map(u => <option key={u}>{u}</option>)}
      </select>
      <button onClick={handleConvert}>Convert</button>
      {result !== null && <p>Result: {result}</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  )
}