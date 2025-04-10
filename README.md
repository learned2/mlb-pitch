# ⚾ MLB Pitch Predictor
> Predict pitch type and velocity using live game situations, machine learning, and custom-designed game logic.

## 🎥 Live Demo

[🔗 Try it here](https://your-app-url.com)  
or  
[📦 Watch the video demo](https://your-demo-video-link)

![screenshot](demo/demo_screenshot.png)


## 🔧 Features

- Predict the most likely pitch type (Fastball, Breaking, Offspeed, Other)
- Estimate pitch velocity (MPH) based on pitcher and context
- Clickable, interactive baseball diamond (Figma-designed)
- Context-aware scoreboard (Balls, Strikes, Outs)
- Dropdown with real pitcher names
- Hosted on GitHub Pages + Flask API on Render

## How the Machine Learning Model Works

The pitch prediction system uses a supervised machine learning classifier trained on 2024 Statcast data using scikit-learn and XGBoost.

### Pitch Type Group Classification

The model predicts one of four grouped pitch categories:

- **Fastball** — includes Four-Seam Fastball, Two-Seam Fastball, Sinker, Cutter, Split-Finger Fastball
- **Breaking** — includes Slider, Sweeper, Curveball, Knuckle Curve
- **Offspeed** — includes Changeup, Screwball
- **Other** — includes Knuckleball, Eephus, Forkball

#### Features Used for Prediction:
- Batter stance (left or right)
- Count (balls and strikes)
- Inning
- Number of outs
- Runners on base (1st, 2nd, and 3rd)
- Score differential (pitcher's team score minus opponent's)
- Pitcher ID

To improve generalization, the model was trained using `class_weight='balanced'` to correct for pitch type imbalance (fastballs were overrepresented). Through feature engineering and careful model tuning, overall classification accuracy improved from 31% to 53%.

Additional features such as `pitch_count`, `batter_id`, and `is_home_team` were removed during optimization due to low contribution or noise.

---

### Pitch Velocity Estimation

Rather than training a regression model, average pitch speeds (MPH) were precomputed using historical Statcast data.

For every `(pitcher_id, pitch_type_group)` pair, the mean `release_speed` was calculated and stored. When the model predicts a pitch type, the corresponding average velocity is retrieved and displayed in the app.

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

