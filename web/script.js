// script.js
function toggleBase(baseId) {
    const base = document.getElementById(baseId);
    base.classList.toggle("active");
  }
  
  document.getElementById("base1").onclick = () => toggleBase("base1");
  document.getElementById("base2").onclick = () => toggleBase("base2");
  document.getElementById("base3").onclick = () => toggleBase("base3");
  
  function predictPitch() {
    const payload = {
      stand: parseInt(document.getElementById("stand").value),
      balls: parseInt(document.getElementById("balls").value),
      strikes: parseInt(document.getElementById("strikes").value),
      inning: parseInt(document.getElementById("inning").value),
      outs_when_up: parseInt(document.getElementById("outs").value),
      on_1b: document.getElementById("base1").classList.contains("active") ? 1 : 0,
      on_2b: document.getElementById("base2").classList.contains("active") ? 1 : 0,
      on_3b: document.getElementById("base3").classList.contains("active") ? 1 : 0,
      pitch_count: parseInt(document.getElementById("pitchCount").value),
      score_diff: parseInt(document.getElementById("homeScore").value) - parseInt(document.getElementById("awayScore").value),
      is_home_team: parseInt(document.getElementById("isHome").value),
      batter_id: parseInt(document.getElementById("batterId").value),
      pitcher_id: parseInt(document.getElementById("pitcherId").value),
    };
  
    fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    })
      .then((response) => response.json())
      .then((data) => {
        document.getElementById("result").innerText = `🎯 Most likely pitch: ${data.predicted_pitch_type_group}`;
      })
      .catch((error) => {
        document.getElementById("result").innerText = `❌ Error: ${error}`;
      });
  }
  