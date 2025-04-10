# ⚾ MLB Pitch Predictor
> Predict pitch type and velocity using live game situations, machine learning, and custom-designed game logic.

## 🎥 Live Demo

[🔗 Try it here](https://your-app-url.com)  
or  
[📦 Watch the video demo](https://your-demo-video-link)

![screenshot](demo/screenshot.png)


## 🔧 Features

- Predict the most likely pitch type (Fastball, Breaking, Offspeed, Other)
- Estimate pitch velocity (MPH) based on pitcher and context
- Clickable, interactive baseball diamond (Figma-designed)
- Context-aware scoreboard (Balls, Strikes, Outs)
- Dropdown with real pitcher names
- Hosted on GitHub Pages + Flask API on Render

## ⚔️ Challenges Overcome

- ⚙️ Matching game situation data (score, inning, base runners) to real-world model input
- 🔄 Retraining model to remove noisy features like pitch count
- 🎯 Dealing with heavy class imbalance (fastballs overrepresented)
- 🔄 Correcting base runner features that were always zero initially
- 🔍 Interpreting model predictions with confidence levels
- 🎨 Integrating artwork, UI, and interactivity from Figma mockup into usable JS/HTML

## 📈 Model Optimization

- ✅ Removed `pitch_count` to reduce noise
- ✅ Cleaned and re-engineered base runner inputs
- ✅ Used `class_weight='balanced'` to reduce Fastball bias
- ✅ Grouped pitch types into 4 major categories
- ✅ Accuracy improved from 31% → 61% (classification)
- ✅ Fastball group accuracy: ~71%

## 💻 How to Use It

1. Open the web app
2. Enter the current game situation (balls, strikes, runners on base, inning)
3. Select a pitcher by name
4. Click "Predict Pitch"
5. View the most likely pitch type + estimated velocity

## 💡 Future Improvements

- Add pitch probabilities (visualized with bars or rings)
- Model pitch location (Zone-based heatmap)
- Pitch-by-pitch simulation (sequence prediction)
- Expanded pitcher database and seasonal stats
- Mobile UI support

## 🙏 Credits

- Inspired by MLB Statcast + sabermetrics
- Data from Baseball Savant via pybaseball
- Design and UI prototyped in Figma

