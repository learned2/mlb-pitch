// Toggle runner on base
function toggleBase(baseId) {
    const base = document.getElementById(baseId);
    base.classList.toggle("active");
  }
  
  document.getElementById("base1").onclick = () => toggleBase("base1");
  document.getElementById("base2").onclick = () => toggleBase("base2");
  document.getElementById("base3").onclick = () => toggleBase("base3");
  
  let stand = 0; // Default: L
  function setStance(value) {
    stand = value;
    document.getElementById("standL").classList.toggle("selected", value === 0);
    document.getElementById("standR").classList.toggle("selected", value === 1);
  }
  
  // Predict API call
  function predictPitch() {
    const payload = {
      stand,
      balls: parseInt(document.getElementById("balls").value),
      strikes: parseInt(document.getElementById("strikes").value),
      inning: parseInt(document.getElementById("inning").value),
      outs_when_up: parseInt(document.getElementById("outs").value),
      on_1b: document.getElementById("base1").classList.contains("active") ? 1 : 0,
      on_2b: document.getElementById("base2").classList.contains("active") ? 1 : 0,
      on_3b: document.getElementById("base3").classList.contains("active") ? 1 : 0,
      score_diff: parseInt(document.getElementById("homeScore").value) - parseInt(document.getElementById("awayScore").value),
      pitcher_id: parseInt(document.getElementById("pitcherId").value)
    };
  
    fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    })
      .then(res => res.json())
      .then(data => {
        console.log("API response:", data);
        const pitch = data.predicted_pitch_type_group || "Unknown";
        const mph = data.avg_velocity ? `${data.avg_velocity} MPH` : "Speed N/A";
        
        document.getElementById("result").innerHTML = `
          <div style="font-size: 24px; font-weight: bold;">${pitch}</div>
          <div style="font-size: 18px; color: #555;">⚡ ${mph}</div>
        `;
        
      })
      .catch(err => {
        console.error("API error:", err);
        document.getElementById("result").innerText = "Error calling API";
      });
  }
  
  // Default stance on load
  setStance(0);
  