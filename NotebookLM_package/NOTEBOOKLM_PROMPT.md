# NotebookLM Prompt

請閱讀我上傳的資料與來源，協助我完成「Red Wine Quality 多元線性回歸分析」作業中的 NotebookLM 研究摘要與網路主流解法比較。

## 作業背景

我的作業要求是選擇一個 Kaggle 上具有 10 至 20 個 features 的公開資料集，使用 Linear Regression 進行預測，並依照 CRISP-DM 流程完成分析。分析必須包含：

- 資料集來源與研究背景
- Feature Selection
- Model Evaluation
- 預測圖，並加入信賴區間或預測區間
- GPT 輔助內容
- NotebookLM 摘要，至少 100 字
- 網路上主流或更優解法的比較

我選擇的資料集是 Kaggle 的 Red Wine Quality：

https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009

## 請你幫我完成的內容

請產生以下兩段內容，文字要適合直接放進大學作業報告中：

### 1. NotebookLM 摘要

請用繁體中文撰寫 100 字以上摘要，說明你根據資料集來源、Wine Quality 相關分析資料、線性回歸與常見機器學習解法所整理出的重點。

摘要需要包含：

- Red Wine Quality 資料集的研究目的
- 常見的重要特徵，例如 alcohol、volatile acidity、sulphates 等
- 為什麼線性回歸適合用來做可解釋的基準模型
- 為什麼此資料集的 R2 不一定會很高
- 可提到更複雜模型可能有更好表現

### 2. 網路主流或更優解法比較

請用繁體中文撰寫一段比較，說明 Wine Quality 類型問題常見的其他解法，例如：

- Random Forest
- Gradient Boosting
- XGBoost
- 分類模型，把 quality 分成低、中、高品質

請比較這些方法與 Linear Regression 的差異，包含：

- Linear Regression 的優點：簡單、可解釋、適合作為 baseline
- Linear Regression 的限制：難以捕捉非線性關係
- Tree-based models 的優點：能處理非線性與特徵交互作用
- 為什麼本作業仍以 Linear Regression 作為主要模型

## 寫作格式要求

- 使用繁體中文
- 口吻正式但自然，像大學生報告
- 不要寫成條列式，請寫成完整段落
- 不要捏造 Kaggle 排名，因為本資料集不是 competition 排名作業
- 請明確提到這是 NotebookLM 研究整理

## 我的模型結果

我的程式使用 Linear Regression 建立兩個模型：

1. 使用全部 11 個 features
2. 使用 SelectKBest 選出前 8 個 features

模型評估結果：

```text
Linear Regression - all features
MAE  = 0.5035
RMSE = 0.6245
R2   = 0.4032

Linear Regression - top 8 selected features
MAE  = 0.5062
RMSE = 0.6265
R2   = 0.3993
```

SelectKBest 選出的 8 個特徵：

```text
fixed acidity
volatile acidity
citric acid
chlorides
total sulfur dioxide
density
sulphates
alcohol
```
