每月租金

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "A simple bar chart with embedded data.",
  "data": {
    "values": [
      {"district": "嘉定", "median_rental_by_month": 4500},
      {"district": "奉贤", "median_rental_by_month": 2900},
      {"district": "宝山", "median_rental_by_month": 4900},
      {"district": "崇明", "median_rental_by_month": 2600},
      {"district": "徐汇", "median_rental_by_month": 7000},
      {"district": "普陀", "median_rental_by_month": 6300},
      {"district": "杨浦", "median_rental_by_month": 5500},
      {"district": "松江", "median_rental_by_month": 5000},
      {"district": "浦东", "median_rental_by_month": 6500},
      {"district": "虹口", "median_rental_by_month": 6000},
      {"district": "金山", "median_rental_by_month": 2800},
      {"district": "长宁", "median_rental_by_month": 7000},
      {"district": "闵行", "median_rental_by_month": 6000},
      {"district": "青浦", "median_rental_by_month": 5200},
      {"district": "静安", "median_rental_by_month": 6900},
      {"district": "黄浦", "median_rental_by_month": 9500}
    ]
  },
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "y": {
      "field": "district",
      "type": "nominal",
      "axis": {"labelAngle": 0},
      "sort": {"field": "median_rental_by_month"}
    },
    "x": {"field": "median_rental_by_month", "type": "quantitative"}
  }
}
```