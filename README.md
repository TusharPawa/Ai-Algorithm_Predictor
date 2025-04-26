# 🤖 AI Algorithm Predictor  
**An AutoML Tool to Automatically Predict the Best Algorithm for Your Dataset**

> *Solving the confusion of model selection by predicting the most accurate ML algorithm with automated training and comparison.*

---
⬇️⬇️ Click the following Project Demo Button to explore the full working demo of the project ⬇️⬇️  
## 🔗 [🚀↗️Project Demo](https://www.youtube.com/watch?v=q0upOqxN18Y)

---

## 📽️ Website Demo Overview

<p align="center">
  <video src="https://github.com/user-attachments/assets/ade51797-51ac-462b-ad39-4ce2d59640c1" controls width="90%"></video>
</p>

---

## 🧪 Input vs Output

### 📌 Input and Output Sections

<div style="width:100%; display:table; table-layout:fixed;">

<table style="width:100%; border-collapse: collapse; font-size: 16px;">
<thead>
<tr style="background-color: #f2f2f2;">
<th align="center" style="width:50%;">📥 Input Description</th>
<th align="center" style="width:50%;">📤 Output Preview</th>
</tr>
</thead>
<tbody>

<tr>
<td style="vertical-align:top; padding:15px;">
<h3>📂 Data Importing</h3>
Import any CSV or Excel dataset. The app automatically detects format and starts preprocessing your data instantly.
</td>
<td align="center" style="padding:15px;">
<img src="https://github.com/TusharPawa/Ai-Algorithm_Predictor/blob/main/Outputs/Data_Importing.jpg?raw=true" width="90%"/>
</td>
</tr>

<tr>
<td style="vertical-align:top; padding:15px;">
<h3>📊 Data Profiling</h3>
Generates an automated data profiling report with detailed column-wise summaries, missing values, distributions, and correlation heatmaps.
</td>
<td align="center" style="padding:15px;">
<video src="https://github.com/user-attachments/assets/86e8566e-e783-4339-a2e5-ded150efeb97" controls width="90%"></video>
</td>
</tr>

<tr>
<td style="vertical-align:top; padding:15px;">
<h3>🧹 Data Cleaning</h3>
Performs automatic data cleaning including missing value handling, data type correction, and feature renaming to ensure consistent modeling.
</td>
<td align="center" style="padding:15px;">
<img src="https://github.com/TusharPawa/Ai-Algorithm_Predictor/blob/main/Outputs/Data_Cleaning.jpg?raw=true" width="90%"/><br><br>
<img src="https://github.com/TusharPawa/Ai-Algorithm_Predictor/blob/main/Outputs/Data_Cleainng_2.jpg?raw=true" width="90%"/>
</td>
</tr>

<tr>
<td style="vertical-align:top; padding:15px;">
<h3>🧠 Data Modeling</h3>
Automatically selects the target column and applies all steps: train-test split, encoding, scaling, embedding, and model pipeline setup.
</td>
<td align="center" style="padding:15px;">
<img src="https://github.com/TusharPawa/Ai-Algorithm_Predictor/blob/main/Outputs/Data_Modeling.jpg?raw=true" width="90%"/>
</td>
</tr>

<tr>
<td style="vertical-align:top; padding:15px;">
<h3>🤖 Algorithm Prediction</h3>
Selects the best performing algorithm using PyCaret’s comparison and benchmarking tool.
</td>
<td align="center" style="padding:15px;">
<img src="https://github.com/TusharPawa/Ai-Algorithm_Predictor/blob/main/Outputs/Algorithm_Prediction.jpg?raw=true" width="90%"/>
</td>
</tr>

<tr>
<td style="vertical-align:top; padding:15px;">
<h3>📋 Comparison Table</h3>
Tabular view of multiple ML model scores including R2, RMSE, MAE for easy comparison.
</td>
<td align="center" style="padding:15px;">
<img src="https://github.com/TusharPawa/Ai-Algorithm_Predictor/blob/main/Outputs/Comparision_Table.jpg?raw=true" width="90%"/>
</td>
</tr>

<tr>
<td style="vertical-align:top; padding:15px;">
<h3>📊 Comparison Graph</h3>
A visual graph showcasing top model performances to quickly identify the best algorithm.
</td>
<td align="center" style="padding:15px;">
<img src="https://github.com/TusharPawa/Ai-Algorithm_Predictor/blob/main/Outputs/Comparison_Graph.jpg?raw=true" width="90%"/>
</td>
</tr>

</tbody>
</table>
</div>

---

## 💡 Key Features

- 📂 Import any CSV/XLSX data and begin processing  
- 📊 Automated data profiling with visual and statistical summaries  
- 🧹 Intelligent data cleaning and transformation pipeline  
- 🧠 Auto selection and training of top ML algorithms using PyCaret  
- 📈 Visual and tabular model performance comparison  
- ✅ Designed for recruiters, analysts, and ML learners  

---

## 🧪 Tech Stack

| Technology                   | Purpose |
|------------------------------|---------|
| 🎯 **Streamlit**             | Frontend framework |
| 🧮 **PyCaret**               | Automated ML and model comparison |
| 📊 **Pandas Profiling**      | Generate data profiling reports |
| 📈 **Plotly Express**        | Visualization of ML results |
| 🧹 **Pandas**                | Data preprocessing |
| 🔗 **streamlit-pandas-profiling** | Integrate profiling with Streamlit |

---

## 🛠️ Installation & Run

```bash
git clone https://github.com/yourusername/Ai-Algorithm_Predictor.git
cd Ai-Algorithm_Predictor
pip install -r requirements.txt
streamlit run app.py
