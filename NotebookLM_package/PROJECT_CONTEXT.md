# 專案背景

## 作業題目

本作業要求使用 Kaggle 公開資料集完成多元線性回歸分析，資料集需具有 10 至 20 個 features，並依照 CRISP-DM 流程撰寫報告。

## 選定資料集

- 資料集名稱：Red Wine Quality
- Kaggle 連結：https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009
- 資料類型：回歸分析
- 預測目標：`quality`
- 輸入特徵數：11 個

## 欄位說明

輸入特徵包含：

```text
fixed acidity
volatile acidity
citric acid
residual sugar
chlorides
free sulfur dioxide
total sulfur dioxide
density
pH
sulphates
alcohol
```

目標欄位：

```text
quality
```

## 選擇原因

此資料集具有 11 個輸入特徵，符合本作業要求的 10 至 20 個 features。紅酒品質分數 `quality` 可被視為數值型目標，因此適合使用 Linear Regression 建立預測模型。此外，資料欄位都是化學檢測數值，容易用相關係數、特徵選擇與模型係數進行解釋。

## CRISP-DM 對應

### Business Understanding

目標是根據紅酒的化學檢測數值預測品質分數，協助理解哪些化學特徵可能與品質評分較有關。

### Data Understanding

資料共有 1599 筆樣本與 12 個欄位，其中 11 個為輸入特徵，1 個為目標欄位。程式檢查後沒有缺失值。

### Data Preparation

資料準備包含讀取 CSV、檢查缺失值、切分訓練與測試資料、標準化特徵，以及指定 `quality` 為預測目標。

### Modeling

使用 Linear Regression 建立模型，並以 SelectKBest 進行特徵選擇。

### Evaluation

使用 MAE、RMSE 與 R2 評估模型表現，並輸出實際值與預測值比較圖，以及約 95% 預測區間。

### Deployment

可將模型設計為簡單的紅酒品質預測工具，輸入化學檢測數值後輸出預測品質分數與誤差參考。
